from rest_framework import serializers

from .models import Hero, HeroRatings

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

