from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

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

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form = PostForm()
	return render(request,'blogApp/post_edit.html',{'form':form})
       
def post_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'blogApp/post_edit.html',{'form':form})	



#commit=False signifie que nous ne voulons pas encore enregistrer notre modèle Post