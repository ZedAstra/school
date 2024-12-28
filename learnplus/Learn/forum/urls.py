from django.urls import path
from . import views

urlpatterns = [
        path('', views.threads, name='threads'),
        path('thread/<int:thread_id>/', views.thread, name='thread'),
        path('create_thread/', views.create_thread, name='create_thread'),
        path('delete_thread/<int:thread_id>/', views.delete_thread, name='delete_thread'),
        path('reply/', views.reply, name='reply'),
]