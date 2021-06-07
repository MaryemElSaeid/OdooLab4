from django.shortcuts import render , redirect
from .models import  Itinew
from .forms import  ItinewForm


def welcome (request):
    return render(request,"welcome.html")

def load_form(request):
    form = ItinewForm
    return render(request,"index.html",{'form':form})
    
def add(request):
    form = ItinewForm(request.POST)
    form.save()
    return redirect('/show')
   
def show(request):
    itinew = Itinew.objects.all
    return render(request,'show.html',{'itinew':itinew})

def edit(request,id):
    itinew = Itinew.objects.get(id=id)
    return render(request,'edit.html',{'itinew':itinew})

def update(request,id):
    itinew = Itinew.objects.get(id=id)
    form = ItinewForm(request.POST,instance=itinew)
    form.save()
    return redirect('/show')


def delete(request,id):
    itinew = Itinew.objects.get(id=id)
    itinew.delete()
    return redirect('/show')