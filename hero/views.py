from .models import Hero
from .serializers import HeroSerializer, HeroDetailSerializer

from rest_framework import mixins, generics

from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404

class HeroApi(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RedirectHeroDetailApi(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroDetailSerializer
    lookup_field = "pk"

    def get(self, request: HttpRequest, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        return redirect('hero_detail', hero_slug=instance.hero_slug, permanent=True)

class HeroDetailApi(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroDetailSerializer
    lookup_field = "hero_slug"

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
