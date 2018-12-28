from rest_framework import serializers

from .models import *


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
