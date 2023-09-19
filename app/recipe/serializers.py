from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=('id','title','price','link')
        read_only_fields=('id',)

class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=('id','title','description','time_minutes','price','link')