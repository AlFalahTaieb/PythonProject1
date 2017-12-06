from django.shortcuts import render, get_object_or_404
#AUTHENTIFICATION
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
##
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView


# def post_list(request):
#     # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#      # posts = Post.objects.filter(order_by('published_date'))
#     # posts=Post.objects.all()
#     posts = Post.objects.all().order_by('title')
#     return render(request, 'blogApp/post_list.html', {'posts': posts}) 

	# Le point après from signifie le dossier courant ou l'application courante. Comme views.py et models.py sont dans le même dossier


class PostList(ListView):
	model= Post
	queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	context_object_name='posts'

		
class PostDetail(DetailView):
	model=Post

class PostRemove(DeleteView):
	model = Post
	success_url = '/'
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

class PostCreate(CreateView):
	# form_class=PostForm
	model=Post
	fields=['author','title','text','published_date']
	#1879-03-14 00:00
	success_url='/'

class PostUpdate(UpdateView):
    model = Post
    fields=['author','title','text']
    success_url = '/'		

def authentificate_user(request):
 	username = request.POST['username']
 	password = request.POST['password']
 	user = authenticate(username=username, password=password)
 	if user is not None:
 		if user.is_active:
 			login(request, user)
 			return HttpResponseRedirect('/')

    

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


# def post_detail(request,pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	return render(request, 'blogApp/post_detail.html', {'post': post})


# def post_new(request): 	
# 	if request.method == 'POST':
# 		form = PostForm(request.POST)
# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.author = request.user
# 			post.published_date = timezone.now()
# 			post.save()
# 			return redirect('post_detail',pk=post.pk)
# 	else:
# 		form = PostForm()
# 	return render(request,'blogApp/post_edit.html',{'form':form})
       
# def post_edit(request,pk):
# 	post = get_object_or_404(Post,pk=pk)
# 	if request.method == 'POST':
# 		form = PostForm(request.POST, instance=post)
# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.author = request.user
# 			post.published_date = timezone.now()
# 			post.save()
# 			return redirect('post_detail',pk=post.pk)
# 	else:
# 		form = PostForm(instance=post)
# 	return render(request,'blogApp/post_edit.html',{'form':form})	

# def post_remove(request,pk):
# 	post = get_object_or_404(Post,pk=pk)
# 	post.delete()
# 	return redirect('post_list')


#commit=False signifie que nous ne voulons pas encore enregistrer notre modèle Post