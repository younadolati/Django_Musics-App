from django.shortcuts import render,redirect,get_object_or_404
from .models import Musics,Comment,User,Test
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import loader
from .forms import CommentForm
# from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.urls import reverse





def show_musics(request,page=1):
    musics=Musics.objects.all().values()
    pagination=Paginator(musics,3)
    page = pagination.get_page(page)
    template=loader.get_template("musics/all_musics.html")
    context={'musics':page,}
    return HttpResponse(template.render(context,request))

def show_tests(request):
    tests=Test.objects.all().values()
    template=loader.get_template("musics/test.html")
    context={'tests':tests,}
    return HttpResponse(template.render(context,request))

def test(request,slug):
    test=Test.objects.get(slug=slug)
    template=loader.get_template("musics/detailstest.html")
    context={'test':test}
    return HttpResponse(template.render(context,request))


def likes(request,id):
    # if request.method == "post":
    music=Musics.objects.get(id=id)
    music.likes.add(request.user)
    template=loader.get_template("musics/details.html")
    context={'likes':music.likes.count(),}
    return HttpResponse((context,request))

# Create your views here.

def details(request,id):
    music=get_object_or_404(Musics,id=id)
    comments=Comment.objects.filter(music_id=id)
    form=CommentForm()
    context={'music':music,"form":form,"comments":comments,}
    if request.POST:
        form=CommentForm(request.POST)
        isinstance=form.save(commit=False)
        isinstance.user=request.user
        isinstance.music=music
        isinstance.save()
        template=loader.get_template("musics/details.html")
        return HttpResponse(template.render(context,request))   

    template=loader.get_template("musics/details.html")
    return HttpResponse(template.render(context,request))
    

# def send_gmail(request):
#     subject="sallam"
#     message="youna dolati"
#     email_from=f'dolati.youna20@gmail.com'
#     recipient=['younadolati35@gmail.com']
#     res = send_mail( subject, message, email_from, recipient,fail_silently=True)
#     return HttpResponse('%s'%res)
    
    











def like_show(request,id):
    obj=Musics.objects.get(id=id)
    # if obj.likes.filter(id=request.user):
    obj.likes.add(request.user)


    
    template=loader.get_template("details.html")
    context={'obj':obj.total_likes(),}
    return HttpResponse(template.render(context,request))

