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

        def get(self, request, id=0):
            if (id>0):
                agentes=list(Agentes.objects.filter(id=id).values())
                if len(agentes)>0:
                    agent= agentes[0]
                    datos = {'message': "Succes", 'agentes': agent}
                else:
                    datos = {'message': "Agentes not found"}
                return JsonResponse(datos)
            else:
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

        def put(self, request, id):
            jd = json.loads(request.body)
            agentes = list(Agentes.objects.filter(id=id).values())
            if len(agentes) > 0:
                agentes=Agentes.objects.get(id=id)
                agentes.nombre=jd['nombre']
                agentes.rol = jd['rol']
                agentes.pais = jd['pais']
                agentes.habilidad_q = jd['habilidad_q']
                agentes.habilidad_e = jd['habilidad_e']
                agentes.habilidad_c = jd['habilidad_c']
                agentes.definitiva = jd['definitiva']
                agentes.save()
                datos = {'message': "Succes"}
            else:
                datos = {'message': "Agentes not found"}
            return JsonResponse(datos)
        def delete(self, request, id):
            agentes = list(Agentes.objects.filter(id=id).values())
            if len(agentes) > 0:
                Agentes.objects.filter(id=id).delete()
                datos = {'message': "Succes"}
            else:
                datos = {'message': "Agentes not found"}
            return JsonResponse(datos)
            pass
