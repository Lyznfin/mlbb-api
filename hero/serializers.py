from rest_framework import serializers

from .models import Hero, HeroRatings, Role

from django.db.models import Q

class HeroRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroRatings
        exclude  = ['id', 'hero']
        
class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['hero_id', 'hero_name', 'roles', 'specialities', 'lanes']

class HeroDetailSerializer(serializers.ModelSerializer):
    hero_ratings = HeroRatingsSerializer(many=False, read_only=True)
    class Meta:
        model = Hero
        fields = ['hero_id', 'hero_name', 'hero_alias', 'hero_ratings', 'roles', 'specialities', 'lanes']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_name', 'description']

class HeroRoleSerializer(serializers.ModelSerializer):
    # role_description = RoleSerializer(many=False, read_only=True)
    heroes = serializers.SerializerMethodField(method_name="get_heroes")

    def get_heroes(self, obj: Role):
        heroes = Hero.objects.filter(Q(primary_role=obj) | Q(secondary_role=obj))
        serializer = HeroSerializer(instance=heroes, many=True)
        return serializer.data

    class Meta:
        model = Role
        fields = ['role_name', 'description', 'heroes']