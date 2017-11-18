
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/$',views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit, name='post_edit')
]



# Running away from the rift
# Didn’t follow the way I was supposed
# Now I uncover my wounds
# And y’all aware of what you mustn’t know
# Everybody knows the name
# But you don’t know what’s inside of myself
# I can’t wait for you to figure out half of that shit
# And I’m ready to walk alone
# Even on the darkest nights
# Oh you left on the way?
# Homie you been listening for your eyes
# And I’m ready to walk alone
# Even on the darkest nights
# “Passar bem, passar mal
# Tudo neste mundo é um passar”

# [HOOK]
# Oh my darling don’t you cry
# The show must go on
# Oh my darling don’t you cry
# I’m feeling fine

# [BRIDGE]
# “Hold on, hold on, hold on
# I told you you were crazy
# You better stop, you better stop..!
# Oh.. oh you want death?
# That’s what you want?.. “

# [VERSE 2]
# Let us dare
# Let us dare to do great things
# My potential and my will always in sync
# I ain’t getting really tired but just insane
# Ain’t that what you wanted for this ‘17
# I still got 50 beats down to get killed
# And another hundred more that I won’t sell
# But I produce everyday that’s in my genes
# Pressure on my path I gotta meditate with Rubin

# [VERSE 3]
# I’m sorry if I hurt you
# Last week another fight
# Anew Me vs. Me
# But I was about to drown
# I'mma stop fucking complaining
# And focus on my craft
# And smash that finish line
# And then fuck up all your minds

# [VERSE 4]
# And I’m ready to walk alone
# Even on the darkest nights
# Oh you left on the way?
# Homie you been listening for your eyes
# And I’m ready to walk alone
# Even on the darkest nights
# “Passar bem, passar mal
# Tudo neste mundo é um passar”

# [HOOK]
# Oh my darling don’t you cry
# The show must go on
# Oh my darling don’t you cry
# I’m feeling fine

# [OUTRO]
# Oh you wanna stay, uh?
# You're still inspired?
# You're always inspired
# Ok, ok..
# I'mma make sure your 5 last week gon' be your toughest
# Let's see if you can make it