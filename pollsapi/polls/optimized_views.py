from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class ChoiceList_Optimized(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll__id=self.kwargs["pk"])
        return queryset 
    serializer_class = ChoiceSerializer


class CreateVote_Optimized(APIView):
    def get(self, request, poll_pk, choice_pk):
        voted_by = request.user
        data = {
            "choice" : choice_pk, "poll" : poll_pk, "voted_by" : voted_by.id,
        }
        print(voted_by.username)
        serializer = VoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # def get(self, request,poll_pk, choice_pk):
    #     queryset = Vote.objects.filter(choice=choice_pk).filter(poll=poll_pk).filter(voted_by=request.user)
    #     data = VoteSerializer(queryset, many=True).data
    #     return Response(data)