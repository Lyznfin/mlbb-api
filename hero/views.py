from .models import Hero, Role
from .serializers import HeroSerializer, HeroDetailSerializer

from rest_framework import mixins, generics
from rest_framework.response import Response

from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q

class HeroApi(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class HeroRoleApi(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = HeroSerializer
    lookup_field = "role_name"

    def get_queryset(self):
        queryset = Hero.objects.all()
        roles = self.kwargs['role_name']
        roles_dict = {"marksman": 1, "fighter": 2, "assassin": 3, "mage": 4, "tank": 5}
        if not isinstance(roles, int):
            roles = roles_dict.get(roles)
        # if not roles in roles_dict.values():
        #     return Response(status=404)
        if not roles == None:
            queryset = Hero.objects.filter(Q(primary_role=roles) | Q(secondary_role=roles))
        return queryset
    
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
