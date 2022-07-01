from django.urls import path, re_path as url
from . import views

urlpatterns = [
    path('', views.main, name="View"),
    path('search/', views.search_post, name="View"),
    path(r'save/', views.save_post, name="Save"),
    path(r'save2/', views.save_post2, name="Save"),
    path(r'update/', views.update_post, name="Save"),
    path(r'delete/<title>/', views.delete_post, name="Delete"),
]
