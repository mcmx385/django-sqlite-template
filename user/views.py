from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

# Create your views here.


# /user
def main(request):
    try:
        users = User.objects.all()
        return HttpResponse(users)

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


# /user/id/{userid}
def get_user_by_id(request, userid):
    try:
        user = User.objects.get(id=userid)
        if not user:
            raise ValueError('No user with such userid')
        return HttpResponse(user)

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


# /user/name/{username}
def get_user_by_name(request, username):
    try:
        user = User.objects.filter(username=username).first()
        if not user:
            raise ValueError('No user with such username')
        return JsonResponse({
            'success': True,
            'data': {
                'id': user.id,
                'username': user.username
            }
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
