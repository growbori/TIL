from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render (request, 'movies/new.html')

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render (request, 'movies/detail.html', context)
def create(request):
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.content = request.POST.get('description')
    movie.save()
    return redirect ('movies:detail', movie.pk)

def edit(request, pk):
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.title = request.POST.get('title')
    movie.content = request.POST.get('description')
    movie.save()
    return redirect('movies:detail', movie.pk)

def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.delete()
    return redirect ('movies:index')