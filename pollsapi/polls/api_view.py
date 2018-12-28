from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import *
from .serializers import *


class polls_list_as_view(APIView):

    def get(self,request):
        poll = Poll.objects.all()

        data = PollSerializer(poll, many=True).data
        print(data)
        return Response(data)


class poll_detail_as_view(APIView):

    def get(self, request, pk):
        p = get_object_or_404(Poll, pk = pk)

        data = PollSerializer(p, many=False).data
        print(data)
        return Response(data)
        