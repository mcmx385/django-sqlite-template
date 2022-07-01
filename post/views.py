from django.shortcuts import render
from post.models import Post
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.

def parse_queryobj(obj):
    return json.loads(serializers.serialize('json', [obj, ]))[0]['fields']


def parse_queryset(data):
    return [parse_queryobj(item) for item in data]


def main(request):
    try:
        posts = Post.objects.all()
        results = parse_queryset(posts)
        return JsonResponse({
            'success': True,
            'data': results
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


def search_post(request):
    try:
        title = request.GET.get('title', False)
        if not title:
            raise ValueError('No passing title')

        post = Post.objects.get(title=title)
        if not post:
            raise ValueError('No post with such title')

        post = json.loads(serializers.serialize('json',[post,]))
        post = post[0]['fields']

        return JsonResponse({
            'success': False,
            'data': post
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


# /post/save?userid={userid}&title={title}&content={content}


def save_post(request):
    try:
        userid = request.GET.get('userid', False)
        title = request.GET.get('title', False)
        content = request.GET.get('content', False)
        if not userid or not title or not content:
            raise ValueError('Not providing userid or title or content')

        count = Post.objects.filter(title=title).count()
        if count > 0:
            raise ValueError('Title already existed')

        post = Post(author_id=userid, title=title, content=content)
        post.save()

        return JsonResponse({
            'success': True,
            'data': {
                'id': post.id,
                'title': title,
                'content': content
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@csrf_exempt
# /post/save2?userid={userid}&title={title}&content={content}
def save_post2(request):
    try:
        body = json.loads(request.body.decode('utf-8'))

        userid = body['userid']
        title = body['title']
        content = body['content']
        if not userid or not title or not content:
            raise ValueError('Not providing userid or title or content')

        count = Post.objects.filter(title=title).count()
        if count > 0:
            raise ValueError('Title already existed')

        post = Post(author_id=userid, title=title, content=content)
        post.save()

        return JsonResponse({
            'success': True,
            'data': {
                'id': post.id,
                'title': title,
                'content': content
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@csrf_exempt
def update_post(request):
    try:
        body = json.loads(request.body.decode('utf-8'))

        userid = body['userid']
        title = body['title']
        content = body['content']
        if not userid or not title or not content:
            raise ValueError('Not providing userid or title or content')

        post = Post.objects.filter(author_id=userid, title=title)
        if post.count() == 0:
            raise ValueError('No post with such title')

        post.update(content=content)

        post = serializers.serialize('json', [post[0], ])
        post = json.loads(post)
        post = post[0]['fields']

        return JsonResponse({
            'success': True,
            'data': post
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


# /post/delete/{title}
def delete_post(request, title):
    try:
        Post.objects.filter(title=title).delete()

        return JsonResponse({
            'success': True
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


def examples(request):
    # users = User.objects.all()  # Return all results
    # users = User.objects.first()  # First returned result
    # # Filter results with the parameter
    # User.objects.filter(username='CoreyMS')
    # user = User.objects.filter(username='CoreyMS').first()
    # print(dir(user))
    # user.id or user.pk
    # User.objects.get(id=1)  # select where parameters
    # post = Post(title='title', content='content')
    # post.save()
    # Post.objects.all()  # if Post() saved it shows
    return HttpResponse({})
