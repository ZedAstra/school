import re
from django.test import TestCase
from django.contrib.auth.models import User

from student import models as student_models
from forum import models as forum_models

# Create your tests here.

class Tests(TestCase):
    
    def test_create_thread(self):
        user = User.objects.create(username='test', password='test')
        student = student_models.Student.objects.create(user=user)
        self.client.force_login(user)
        response = self.client.post('/forum/create_thread/', {
            'question': 'test',
            'titre': '_test_'
        })
        thread = forum_models.Sujet.objects.get(titre='_test_')
        self.assertTrue(thread is not None)
    
    def test_reply_thread(self):
        user = User.objects.create(username='test', password='test')
        student = student_models.Student.objects.create(user=user)
        self.client.force_login(user)
        response = self.client.post('/forum/create_thread/', {
            'question': 'test',
            'titre': '_test_'
        })
        thread = forum_models.Sujet.objects.get(titre='_test_')
        user2 = User.objects.create(username='test2', password='test2')
        student2 = student_models.Student.objects.create(user=user2)
        response = self.client.post('/forum/reply_thread/', {
            'reponse': '_test_',
            'thread_id': thread.id
        })
        replies = forum_models.Reponse.objects.filter()
        self.assertTrue(replies.count() == 1)
        
    def test_delete_thread(self):
        user = User.objects.create(username='test', password='test')
        student = student_models.Student.objects.create(user=user)
        self.client.force_login(user)
        response = self.client.post('/forum/create_thread/', {
            'question': 'test',
            'titre': '_test_'
        })
        thread = forum_models.Sujet.objects.get(titre='_test_')
        response = self.client.get('/forum/delete_thread/' + str(thread.id) + '/')
        thread = forum_models.Sujet.objects.filter(titre='_test_')
        self.assertTrue(thread.count() == 0)
        
        