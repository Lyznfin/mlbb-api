from .models import Hero, Role, Speciality, Lane
from .serializers import HeroSerializer, HeroDetailSerializer

from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q

class HeroApi(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RedirectHeroDetailApi(APIView):
    def get(self, request: HttpRequest, pk_or_name: str, format=None):
        if str(pk_or_name).isdigit():
            instance = get_object_or_404(Hero, pk=pk_or_name)
        else:
            instance = get_object_or_404(Hero, hero_name=pk_or_name.capitalize())

        return redirect('hero_detail', hero_slug=instance.hero_slug, permanent=True)

class HeroDetailApi(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroDetailSerializer
    lookup_field = "hero_slug"

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class HeroRoleApi(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = "role"

    def get_queryset(self):
        searched_role = str(self.kwargs['role']).capitalize()
        all_roles = Role.objects.all()
        valid_roles = [role.role_name for role in all_roles]

        if searched_role not in valid_roles:
            return self.queryset.none()
        else:
            role = all_roles.get(role_name=searched_role)
            queryset = Hero.objects.filter(Q(primary_role=role) | Q(secondary_role=role))
            return queryset
    
    def get(self, request: HttpRequest, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            error_message = f"No hero matches the given role of {self.kwargs['role']}"
            return Response({"detail": error_message}, status=status.HTTP_404_NOT_FOUND)
        
        return self.list(request, *args, **kwargs)

class HeroSpecialityApi(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = "speciality"

    def get_queryset(self):
        searched_speciality = str(self.kwargs['speciality']).title()
        all_specialities = Speciality.objects.all()
        valid_specialities = [speciality.speciality_name for speciality in all_specialities]

        if searched_speciality not in valid_specialities:
            return self.queryset.none()
        else:
            speciality = all_specialities.get(speciality_name=searched_speciality)
            queryset = Hero.objects.filter(Q(primary_speciality=speciality) | Q(secondary_speciality=speciality))
            return queryset
    
    def get(self, request: HttpRequest, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            error_message = f"No hero matches the given speciality of {self.kwargs['speciality']}"
            return Response({"detail": error_message}, status=status.HTTP_404_NOT_FOUND)
        
        return self.list(request, *args, **kwargs)
    
class HeroLaneApi(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = "lane"

    def get_queryset(self):
        searched_lane = str(self.kwargs['lane']).replace("%20", " ").title()
        all_lanes = Lane.objects.all()
        valid_lanes = [lane.lane_name for lane in all_lanes]

        if searched_lane not in valid_lanes:
            return self.queryset.none()
        else:
            lane = all_lanes.get(lane_name=searched_lane)
            queryset = Hero.objects.filter(Q(primary_lane=lane) | Q(secondary_lane=lane))
            return queryset
    
    def get(self, request: HttpRequest, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            error_message = f"No hero matches the given kane of {self.kwargs['lane']}"
            return Response({"detail": error_message}, status=status.HTTP_404_NOT_FOUND)
        
        return self.list(request, *args, **kwargs)