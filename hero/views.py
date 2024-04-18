from .models import Hero, Role, Speciality, Lane
from .serializers import HeroSerializer, HeroDetailSerializer, HeroRoleSerializer, HeroSpecialitySerializer, HeroLaneSerializer

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
    
class HeroRoleApi(APIView):
    def get_queryset(self):
        queryset = Role.objects.all()
        try:
            searched_role = str(self.kwargs['role']).capitalize()
        except KeyError:
            return queryset
        
        valid_roles = [role.role_name for role in queryset]
        if searched_role not in valid_roles:
            return None
        else:
            return queryset.get(role_name=searched_role)
    
    def get(self, request: HttpRequest, *args, **kwargs) -> None:
        queryset = self.get_queryset()
        if queryset is None:
            error_message = f"No hero matches the given role of {self.kwargs.get('role')}"
            return Response({"detail": error_message}, status=status.HTTP_404_NOT_FOUND)
        
        if isinstance(queryset, Role):
            serializer = HeroRoleSerializer(queryset)
        else:
            serializer = HeroRoleSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class HeroSpecialityApi(APIView):
    def get_queryset(self):
        queryset = Speciality.objects.all()
        try:
            searched_speciality = str(self.kwargs['speciality']).title()
        except KeyError:
            return queryset
        
        valid_specialities = [speciality.speciality_name for speciality in queryset]
        if searched_speciality not in valid_specialities:
            return None
        else:
            return queryset.get(speciality_name=searched_speciality)
    
    def get(self, request: HttpRequest, *args, **kwargs) -> None:
        queryset = self.get_queryset()
        if queryset is None:
            error_message = f"No hero matches the given speciality of {self.kwargs.get('speciality')}"
            return Response({"detail": error_message}, status=status.HTTP_404_NOT_FOUND)
        
        if isinstance(queryset, Speciality):
            serializer = HeroSpecialitySerializer(queryset)
        else:
            serializer = HeroSpecialitySerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HeroLaneApi(APIView):
    def get_queryset(self):
        queryset = Lane.objects.all()
        try:
            searched_lane = str(self.kwargs['lane']).title()
        except KeyError:
            return queryset
        
        valid_lane = [lane.lane_name for lane in queryset]
        if searched_lane not in valid_lane:
            return None
        else:
            return queryset.get(lane_name=searched_lane)
    
    def get(self, request: HttpRequest, *args, **kwargs) -> None:
        queryset = self.get_queryset()
        if queryset is None:
            error_message = f"No hero matches the given lane of {self.kwargs.get('lane')}"
            return Response({"detail": error_message}, status=status.HTTP_404_NOT_FOUND)
        
        if isinstance(queryset, Lane):
            serializer = HeroLaneSerializer(queryset)
        else:
            serializer = HeroLaneSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)