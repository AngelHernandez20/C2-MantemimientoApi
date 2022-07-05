from django.shortcuts import render
from .models import  Agentes
from .serializers import AgentesSerializer
from rest_framework import viewsets

class AgentesviewSet(viewsets.ModelViewSet):
    queryset= Agentes.objects.all()
    serializer_class=AgentesSerializer

