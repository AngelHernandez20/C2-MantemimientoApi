
from django.urls import path
from .views import agentesView

urlpatterns = [
  path('agentes/',agentesView.as_view(), name='agentes_list')
]