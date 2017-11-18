from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     # posts = Post.objects.filter(order_by('published_date'))
    # posts=Post.objects.all()
    posts = Post.objects.all().order_by('title')
    return render(request, 'blogApp/post_list.html', {'posts': posts}) 

	# Le point après from signifie le dossier courant ou l'application courante. Comme views.py et models.py sont dans le même dossier

def post_detail(request,pk):
		post = get_object_or_404(Post, pk=pk)
		return render(request, 'blogApp/post_detail.html', {'post': post})