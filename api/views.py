from django.shortcuts import render
from .models import  Agentes
from .serializers import AgentesSerializer
from rest_framework import viewsets
from django.views import View
from django.http.response import JsonResponse

class agentesView(View):
        def get(self, request):
            agentes = list(Agentes.objects.values())
            if len(agentes)>0:
                datos = {'message':"Succes", 'agentes': agentes}
            else:
                datos = {'message': "Agentes not found"}
            return JsonResponse(datos)

        def post(self, request):
            pass

        def put(self, request):
            pass

        def delete(self, request):
            pass
