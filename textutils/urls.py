from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze')
    # path('removepunc', views.removepunk, name='removepunc'),
    # path('capitalizefirst', views.capfirst, name='capfirst'),
    # path('newlineremove', views.newlineremove, name='newlineremove'),
    # path('spaceremove', views.spaceremove, name='spaceremove'),
    # path('charcount', views.charcount, name='charcount'),
]

