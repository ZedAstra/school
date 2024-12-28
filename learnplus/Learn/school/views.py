from math import e
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_request, logout
from django.shortcuts import render , redirect 
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    else:
        datas = {

        }
        return render(request, 'pages/guest-login.html', datas)

def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                try:
                    print("1")
                    if request.user.student_user:
                        return redirect('index_student')
                except:
                    print("2")
                    if request.user.instructor:
                        return redirect('dashboard')
            except:
                print("3")
                return redirect("/admin/")
        else:
            datas = {

            }
            return render(request, 'pages/guest-signup.html', datas)
        
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            datas = {
                'error': True,
                'message': 'Les mots de passe ne correspondent pas',
            }
            return render(request, 'pages/guest-signup.html', datas)
        elif request.POST.get('terms') is None: 
            datas = {
                'error': True,
                'message': 'Vous devez accepter les conditions d\'utilisation',
            }
            return render(request, 'pages/guest-signup.html', datas)
        else:
            try:
                
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                datas = {
                    'isSuccess': True,
                    'message': 'Votre compte a été créé avec succès',
                }
                return render(request, 'pages/guest-login.html', datas)
            except:
                datas = {
                    'error': True,
                    'message': 'Une erreur s\'est produite',
                }
        return render(request, 'pages/guest-signup.html') 

def forgot_password(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except:
            print("3")
            return redirect("/admin/")
    else:
        datas = {

        }
        return render(request, 'pages/guest-forgot-password.html', datas)



def islogin(request):

    postdata = json.loads(request.body.decode('utf-8'))
        
    # name = postdata['name']

    username = postdata['username']
    password = postdata['password']

    isSuccess = False
    u_type = ''
    try:
        
        if '@' in username:
            utilisateur = User.objects.get(email=username)
            user = authenticate(request, username=utilisateur.username, password=password)
        else:
            user = authenticate(request, username=username, password=password)
            utilisateur = User.objects.get(username=username)
            
        if user is not None and user.is_active:
            print("user is login")
            isSuccess = True
            login_request(request, user)
            try:
                try:
                    print("1")
                    if utilisateur.student_user: # type: ignore
                        u_type = "student"
                except:
                    print("2")
                    if utilisateur.instructor: # type: ignore
                        u_type = "instructor"
            except:
                print("3")
                u_type = "admin"

            datas = {
                'redirect' : u_type,
                'success':True,
                'message':'Vous êtes connectés!!!',
                'next': '/'+u_type
            }
            print(datas)
            return JsonResponse(datas,safe=False) # page si connect
                
        else:
            data = {
                'success':False,
                'message':'Vos identifiants ne sont pas correcte',
            }
            return JsonResponse(data, safe=False)
    except:
        data = {
            'success':False,
            'message':"Une erreur s'est produite",
        }
        return JsonResponse(data, safe=False)
    
def deconnexion(request):
    logout(request)
    return redirect('login')
