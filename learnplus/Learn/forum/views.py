from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import forum.models as forum_models

# Create your views here.

@login_required(login_url = 'login')
def threads(request):
    if request.user.is_authenticated:
        try:
            try:
                if request.user.student_user:
                    datas = {
                        "forum_general": forum_models.Sujet.objects.all(),
                    }
                    return render(request,'pages/fixed-forum.html', )
            except Exception as e:
                if request.user.instructor:
                    datas = {
                        "forum_general": forum_models.Sujet.objects.all(),
                    }
                    return render(request,'pages/instructor-forum.html',datas)
        except Exception as e:
            return redirect("/admin/")
        
@login_required(login_url = 'login')
def thread(request, thread_id):
    if request.user.is_authenticated:
        if not forum_models.Sujet.objects.filter(pk=thread_id).exists():
            return redirect('/forum/')
        try:
            try:
                if request.user.student_user:
                    forum = forum_models.Sujet.objects.get(pk=thread_id)
                    datas = {
                        "forum": forum,
                        "isOwner": forum.user == request.user,
                    }
                    return render(request,'pages/fixed-student-forum-thread.html', datas)
            except Exception as e:
                if request.user.instructor:
                    forum = forum_models.Sujet.objects.get(pk=thread_id)
                    datas = {
                        "forum": forum,
                        "isOwner": forum.user == request.user,
                    }
                    return render(request,'pages/instructor-forum-thread.html',datas)
        except Exception as e:
            return redirect("/admin/")
        
@login_required(login_url = 'login')
def create_thread(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                try:
                    if request.user.student_user:
                        thread = forum_models.Sujet.objects.create(
                            user = request.user,
                            question = request.POST.get('question'),
                            titre = request.POST.get('titre')
                        )
                        thread.save()
                        return JsonResponse({"success": True, "thread_id": thread.id})
                except Exception as e:
                    if request.user.instructor:
                        thread = forum_models.Sujet.objects.create(
                            user = request.user,
                            question = request.POST.get('question'),
                            titre = request.POST.get('titre')
                        )
                        thread.save()
                        return JsonResponse({"success": True, "thread_id": thread.id})
            except Exception as e:
                return redirect("/admin/")
        else:
            return JsonResponse({"status": "error"})

@login_required(login_url = 'login')
def delete_thread(request, thread_id):
    if request.user.is_authenticated:
        try:
            try:
                if request.user.student_user:
                    forum = forum_models.Sujet.objects.get(pk=thread_id)
                    if forum.user == request.user:
                        forum.delete()
                        return redirect('/forum/')
                    else:
                        return redirect('/forum/')
            except Exception as e:
                if request.user.instructor:
                    forum = forum_models.Sujet.objects.get(pk=thread_id)
                    if forum.user == request.user:
                        forum.delete()
                        return redirect('/forum/')
                    else:
                        return redirect('/forum/')
        except Exception as e:
            return redirect("/admin/")

@login_required(login_url = 'login')
def reply(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                try:
                    if request.user.student_user:
                        reply = forum_models.Reponse.objects.create(
                            user = request.user,
                            sujet = forum_models.Sujet.objects.get(pk=request.POST.get('thread_id')),
                            reponse = request.POST.get('reponse')
                        )
                        reply.save()
                        return JsonResponse({"success": True})
                except Exception as e:
                    if request.user.instructor:
                        reply = forum_models.Reponse.objects.create(
                            user = request.user,
                            sujet = forum_models.Sujet.objects.get(pk=request.POST.get('thread_id')),
                            reponse = request.POST.get('reponse')
                        )
                        reply.save()
                        return JsonResponse({"success": True})
            except Exception as e:
                return redirect("/admin/")
        else:
            return redirect('/forum/')