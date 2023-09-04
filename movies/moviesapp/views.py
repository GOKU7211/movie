from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import MovieForm
from .models import movies
from django.views.generic import ListView

# Create your views here.


def movie(request):
    movie = movies.objects.all()
    context= {'movielist':movie}
    return render(request,"index.html",context)
def detail(request,movieid):
    movie=movies.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method =='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=movies(name=name,desc=desc,year=year,img=img)

        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=movies.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})
def delete(request,id):
    if request.method =='POST':
        movie =movies.objects.get(id=id)
        movie.delete()

        return redirect('/')
    return render(request,'delete.html')
