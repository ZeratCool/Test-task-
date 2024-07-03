from rest_framework import serializers

from .models import Restaurant, Menu



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Menu
        fields = '__all__'


class AddRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class AddingMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        def validate(self, attrs):
            if Restaurant.objects.filter(name=attrs['name']).exists():
                raise serializers.ValidationError('Restaurant already exists')
            return attrs
        def create(self, validated_data):
            return Restaurant.objects.create(**validated_data)

class RestaurantMenuSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = '__all__'
