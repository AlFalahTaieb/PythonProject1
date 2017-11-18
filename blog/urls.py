"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blogApp.urls')),
]



# ^ -> le début du texte
# $ -> la fin du texte
# \d -> un chiffre
# + -> indique que l'expression précédente doit se répéter au moins une fois
# () -> capture une partie du pattern

# *************************************
# ^ post / indique à Django d'attraper toutes les url qui commencent par post/ (juste après ^)
# (\d+) signifie qu'il y aura un nombre (un ou plusieurs chiffres) que nous souhaitons capturer et extraire
# / dit à Django que le caractère / doit suivre le nombre
# $ marque la fin de l'URL, ce qui signifie que seules les chaînes de caractères se terminant par / correspondrons au pattern