from .models import Agentes
from rest_framework import serializers

class AgentesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agentes
        fields='__all__'