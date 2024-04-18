from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.HeroApi.as_view()),
    path('<str:pk_or_name>', views.RedirectHeroDetailApi.as_view()),
    path('detail/<slug:hero_slug>', views.HeroDetailApi.as_view(), name="hero_detail"),
    path('role/', views.HeroRoleApi.as_view()),
    path('role/<str:role>', views.HeroRoleApi.as_view()),
    path('speciality/', views.HeroSpecialityApi.as_view()),
    path('speciality/<str:speciality>', views.HeroSpecialityApi.as_view()),
    path('lane/', views.HeroLaneApi.as_view()),
    path('lane/<str:lane>', views.HeroLaneApi.as_view()),
]
