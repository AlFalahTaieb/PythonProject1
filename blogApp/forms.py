from django import forms
from .models import Post

#POSTFORM est le nom de notre formulaire, c'est un formulaire de ModelForm
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
 #pour dire quel model utriliser pour créer le formualaire
		fields = ('title', 'text',)