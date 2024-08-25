from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Members,Person,Test
from .forms import Signup,Search
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.http import HttpResponse,JsonResponse




def members(request):
    mymembers=Members.objects.all().values()
    template=loader.get_template("all_members.html")
    context={'mymembers':mymembers}
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember=Members.objects.get(id=id)
    template=loader.get_template("details.html")
    context={'mymember':mymember,}
    return HttpResponse(template.render(context,request))

def test(request,slug):
    test=Test.objects.get(slug=slug)
    template=loader.get_template("test.html")
    context={'test':test,}
    return HttpResponse(template.render(context,request))

def likes(request,id):
    # if request.method == "post":
    mymember=Members.objects.get(id=id)
    mymember.like.add(request.user)
    template=loader.get_template("details.html")
    context={'likes':mymember,}
    return HttpResponse(template.render(context,request))

# Create your views here.
def signupuser(request):
    user=request.user
    if user.is_authenticated:
        return render(request,'all_members.html')
    context={}
    form=Signup()
    if request.POST:
        # context={}
        form=Signup(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            user=authenticate(request,username=username)
            login(request,user)
        else:
            context['form']=form
    else:
        form=Signup()
        context={'form':form}
    
    return render(request,'signup.html',context)
            




def search(request):
    form=Search()
    # context=[] 
    if request.POST:
        searched_name=request.POST["name"]
        # if searched_name:
        res=None                
        found_names=Person.objects.filter(name__icontains=searched_name)
        if  len(found_names) > 0 and len(searched_name) > 0:
            data=[]
            for i in found_names:
                names={
                    'name':i.name,
                }
                data.append(names)
            res=data
            return JsonResponse({"status":"200","data":res})

        else:
            res="no name founde ..."
        return JsonResponse({"status":"200","data":res})
    # return JsonResponse({})
                
    
    
    context={'form':form}
    return render(request,'searching.html',context)

