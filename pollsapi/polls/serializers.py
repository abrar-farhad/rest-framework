from rest_framework import serializers

from .models import *

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['id','question', 'created_by', 'pub_date']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','poll', 'choice_text']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['choice', 'poll', 'voted_by']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user