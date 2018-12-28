"""pollsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from polls.views import *

from polls.api_view import *

from .using_generics import *

from .optimized_views import *

urlpatterns = [
   path("polls_list", polls_list, name='polls_list'),
   path("poll_detail/<int:pk>/", poll_detail, name="poll_detail"),
   path("polls_list_as_view", polls_list_as_view.as_view(), name="polls_list_as_view"),
   path("poll_detail_as_view/<int:pk>", poll_detail_as_view.as_view(), name="poll_detail_as_view"),
   path("poll_list_generics", PollList_generics.as_view(), name="poll_list_using_generics"),
   path("poll_detail_generics/<int:pk>", PollDetail_generics.as_view(), name="poll_detail_using_generics"),
   path("choice_generics/", ChoiceCreate_generics.as_view(), name="Choice_using_generics"),
   path("vote_generics/", CreateVote_generics.as_view(), name="Vote_using_generics"),
   path("choice_optimized/<int:pk>", ChoiceList_Optimized.as_view(), name="Choice_Optimized"),
   path("poll/<int:poll_pk>/choice/<int:choice_pk>/vote/", CreateVote_Optimized.as_view(), name="Create_Vote_Optimized")

]