from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())  

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())  

def testing(request):
    mymembers = Member.objects.all().values()
    tester = loader.get_template('template.html')
    context = {
        'mymembers' : mymembers ,
    }
    return HttpResponse(tester.render(context, request))

   # return HttpResponse("Hello, this is the members page of the tennis club!")  
   

