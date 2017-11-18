from django.db import models
from django.utils import timezone

# class Post(models.Model): - C'est cette ligne qui permet de définir notre modèle. C'est un object).
#moels.Model signifie que POST est un modèle Django, comme ça Django isahlou fel BD
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


# models.CharField - Cela nous permet de définir un champ texte avec un nombre limité de caractères.
# models.TextField - Cela nous permet de définir un champ texte sans limite de caractères. Parfait pour le contenu d'un blog post !
# models.DateTimeField - Définit que le champ en question est une date ou une heure.
# models.ForeignKey - C'est un lien vers un autre modèle.