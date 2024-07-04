import datetime

from rest_framework import serializers, status

from api.models import Vote
from .models import UserData
from django.core import exceptions
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data["email"],
                                       name=validated_data["name"])
        user.set_password(validated_data["password"])
        user.save()
        return user

class TotalUsersSerializer(serializers.Serializer):
    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

class ResultSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Vote
        fields = [
            'id',
            'user',
            'restaurant'
        ]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'id',
            'restaurant',
            'date'
        ]

    def validate(self, data):
        request = self.context.get('request', None)
        user = request.user
        today = datetime.date.today()
        if Vote.objects.filter(user=user, date=today).exists():
            raise serializers.ValidationError("You have already voted today")
        return data

    def create(self, validated_data):
        return Vote.objects.create(**validated_data)
class UserSerializer(serializers.ModelSerializer):
    class InnerVoteSerializer(serializers.ModelSerializer):
        restaurant = serializers.StringRelatedField()

        class Meta:
            model = Vote
            fields = [
                'id',
                'restaurant',
                'date'
            ]

    votes = InnerVoteSerializer(many=True)

    class Meta:
        model = UserData
        fields = [
            'id',
            'username',
            'email',
            'votes',
        ]