from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required
from school import models as school_models
from forum import models as forum_models
from instructor import models as instructor_models
from django.db.models import Q
from chat import models as chat_models
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse 
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import authenticate, login


# Create your views here.
@login_required(login_url = 'login')
def index(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard') 
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    cours = school_models.Cours.objects.filter(Q(status=True) & Q(chapitre__classe=request.user.student_user.classe)).order_by('-date_add')[:5]
                    forum = forum_models.Sujet.objects.filter(cours__chapitre__classe=request.user.student_user.classe)[:5]
                    forum_count = forum_models.Sujet.objects.filter(cours__chapitre__classe=request.user.student_user.classe).count()
                    datas = {
                                'cours': cours,
                                'forum': forum,
                                'forum_count': forum_count,
                           }
                return render(request,'pages/fixed-student-dashboard.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url = 'login')
def payment(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-payment-information.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
   
@login_required(login_url = 'login')
def subscription(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-subscription.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def upgrade(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-upgrade.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                    }
                return render(request,'pages/fixed-student-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def edit_basic(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit-basic.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def edit_profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit-profile.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url = 'login')
def billing(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-billing.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
# @login_required(login_url = 'login')
# def browse_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     cours = school_models.Cours.objects.filter(Q(status=True) & Q(chapitre__classe=request.user.student_user.classe))
#                     datas = {
#                                 'all_cours' : all_cours ,
#                            }
#                 return render(request,'pages/fixed-student-browse-courses.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")
   

@login_required(login_url = 'login')
def cart(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-cart.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard') 
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                   
                    datas = {
                                
                           }
                return render(request,'pages/fixed-student-courses.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
# @login_required(login_url = 'login')
# def dashboard(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     datas = {

#                            }
#                 return render(request,'pages/fixed-student-dashboard.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")

@login_required(login_url = 'login')
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-earnings.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    forum_general = forum_models.Sujet.objects.filter(cours=None)
                    forum = forum_models.Sujet.objects.filter(cours__chapitre__classe=request.user.student_user.classe)
                    datas = {
                        'forum_general': forum_general,
                        'forum': forum,
                    }
                return render(request,'pages/fixed-student-forum.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def forum_lesson(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    lesson = school_models.Cours.objects.get(slug=slug)
                    datas = {
                        'lesson':lesson,
                    }
                return render(request,'pages/fixed-student-forum-lesson.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def forum_ask(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-forum-ask.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")




@login_required(login_url = 'login')
def forum_thread(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    forum = forum_models.Sujet.objects.get(slug=slug)
                    datas = {
                        "forum": forum,
                    }
                return render(request,'pages/fixed-student-forum-thread.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def help_center(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-help-center.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def invoice(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-invoice.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def messages(request, classe):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    exist_classe = chat_models.Salon.objects.get(classe=request.user.student_user.classe)
                    info = school_models.Classe.objects.get(id=request.user.student_user.classe.id)
                    instructor = instructor_models.Instructor.objects.get(classe__id=request.user.student_user.classe.id)
                    user_room = ''                    
                    print(user_room)
                    datas = {
                        'instructor':instructor,
                        'info_classe':info,
                        'classe': exist_classe,
                        'classe_json': mark_safe(json.dumps(exist_classe.id)),
                        'username': mark_safe(json.dumps(request.user.username))
                    }
                return render(request,'pages/fixed-student-messages.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
# @login_required(login_url = 'login')
# def messages_2(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     datas = {

#                            }
#                 return render(request,'pages/fixed-student-messages-2.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")

@login_required(login_url = 'login')
def my_courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    chapitre = school_models.Chapitre.objects.filter(status=True)
                    cours = school_models.Cours.objects.filter(status=True)
                    all_cours = school_models.Cours.objects.filter(Q(status=True) & Q(chapitre__classe=request.user.student_user.classe))
                    datas = {
                                'chapitre':chapitre, 
                                'cours':cours,
                                'all_cours': all_cours,
                           }
                return render(request,'pages/fixed-student-my-courses.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def quiz_list(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-quiz-list.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-profile.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def profile_posts(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-profile-posts.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def quiz_results(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-quiz-results.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def quizzes(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-quizzes.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-statement.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

# @login_required(login_url = 'login')
# def student_take_course(request, slug):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     cours  = school_models.Cours.objets.get(slug=slug)
#                     datas = {
#                         'cours': cours,
#                     }
#                 return render(request,'pages/fixed-student-student-take-course.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url='login')
def take_course(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    cours = school_models.Cours.objects.get(slug=slug)
                    instructor = instructor_models.Instructor.objects.get(classe__id=request.user.student_user.classe.id)
                    datas = {
                        'cours': cours,
                        'instructor' : instructor,
                    }
                return render(request,'pages/fixed-student-take-course.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect('my-courses')
   

@login_required(login_url = 'login')
def take_quiz(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-take-quiz.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def view_course(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-view-course.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def account_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

        
def update_profil(request):
    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    email = request.POST.get("email")
    bio = request.POST.get("bio")

    try:
        user = User.objects.get(username=request.user.username)
        user.last_name = nom
        user.first_name = prenom
        user.email = email
        user.save()
        student = models.Student.objects.get(user__id=request.user.id)
        student.bio = bio
        student.save()
        try:
            image = request.FILES["file"]
            student.photo = image 
            student.save()

        except:
            pass
        success = True 
        message = "vos informations ont été modifié avec succés"

    except:
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success" : success,
        "message" : message,
        }
    return JsonResponse(data,safe=False)

        
def update_password(request):
    last_password = request.POST.get("last_password")
    new_password = request.POST.get("new_password")
    confirm_password = request.POST.get("confirm_password")

    try:
        if not request.user.check_password(last_password):
            success = False
            message = "Ancien mot de passe incorrect"
        elif new_password != confirm_password:
            success = False
            message = "Les mots de passe ne sont pas identiques"
        else:
            user = User.objects.get(username=request.user.username)
            username = user.username
            user.password = new_password
            user.set_password(user.password)
            user.save()
            user = authenticate(username=username, password=new_password)
            login(request, user)
            success = True 
            message = "Mot de passe modfifié avec succès"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success" : success,
        "message" : message,
        }
    return JsonResponse(data,safe=False)

    

        
def post_forum(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    lesson = request.POST.get("lesson")
    val = ""
    try:
        lesson = school_models.Cours.objects.get(id=int(lesson))
        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.cours = lesson
        forum.user = request.user
        forum.save()
        val = forum.slug
        success = True 
        message = "Votre sujet a bien été ajouté!"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la soumission"
    data = {
        "success" : success,
        "message": message,
        "forum": val,
        }
    return JsonResponse(data,safe=False)

    
def post_forum_g(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    val = ""
    try:
        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.user = request.user
        forum.save()
        val = forum.slug
        success = True 
        message = "Votre sujet a bien été ajouté!"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la soumission"
    data = {
        "success" : success,
        "message": message,
        "forum": val,
        }
    return JsonResponse(data,safe=False)
