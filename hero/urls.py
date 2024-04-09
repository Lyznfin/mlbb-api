from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.HeroApi.as_view()),
    path('<int:pk>', views.RedirectHeroDetailApi.as_view()),
    path('<slug:hero_slug>', views.HeroDetailApi.as_view(), name="hero_detail")
]
