from rest_framework import serializers
from .models import BeautyProducts, Fruits, Vegetables

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = '__all__'
       

class VegetablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetables
        fields = '__all__'

class BeautyProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyProducts
        fields = '__all__'