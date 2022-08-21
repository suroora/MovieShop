from django.shortcuts import redirect

from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from . forms import MovieForm

# Create your views here.
def index(request):
   movie = Movie.objects.all()
   context={
       'movie_list' : movie
   }
   return render(request,'index.html',context)

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie' :movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        img = request.FILES['img']
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)

        movie=Movie(name=name,img=img,desc=desc,year=year)
        movie.save()
        return redirect('/')

    return render(request,"add.html")


def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
