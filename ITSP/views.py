from functools import partial
import stat
import uuid
from django import http
import django
from django.shortcuts import render
from django.http import HttpResponse

from ITSP.serializers import TeamSerializer
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def index(request):

    teams = Team.objects.all()
    return render(request=request, template_name="index.html", context={'teams':teams})

def go(request,pk):
    # team_detail = Team.objects.get(Team_id = pk)
    try:
        team_info = Team.objects.get(Team_id = pk)
        print(team_info)
        return render(request,template_name="team.html",context={'team':team_info})
    except:
        pass
        return HttpResponse("Team id Does not exist! Try again!!!")


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Team_API(request,pk=None):
    if request.method== 'GET':
        teamid = pk
        if teamid is not None:
            team = Team.objects.get(Team_id = teamid)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        team = Team.objects.all()
        serializer = TeamSerializer(team , many =True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        teamid = pk
        team = Team.objects.get(pk = teamid)
        serializer = TeamSerializer(team,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    if request.method == 'PATCH':
        teamid = pk
        team = Team.objects.get(pk = teamid)
        serializer = TeamSerializer(team,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        teamid = request.data.get('Team_id')
        team = Team.objects.get(Team_id = teamid)
        team.delete()
        return Response({'msg':'Data deleted'})
