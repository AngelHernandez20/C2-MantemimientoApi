import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import  Agentes
from .serializers import AgentesSerializer
from rest_framework import viewsets
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

class agentesView(View):

        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

        def get(self, request):
            agentes = list(Agentes.objects.values())
            if len(agentes)>0:
                datos = {'message':"Succes", 'agentes': agentes}
            else:
                datos = {'message': "Agentes not found"}
            return JsonResponse(datos)

        def post(self, request):
            jd= json.loads(request.body)
            print(jd)
            Agentes.objects.create(nombre=jd['nombre'], rol=jd['rol'], pais=jd['pais'], habilidad_q=jd['habilidad_q'], habilidad_e=jd['habilidad_e'],
                                   habilidad_c=jd['habilidad_c'], definitiva=jd['definitiva'])
            datos = {'message':"Succes"}
            return JsonResponse(datos)

        def put(self, request):
            pass

        def delete(self, request):
            pass
