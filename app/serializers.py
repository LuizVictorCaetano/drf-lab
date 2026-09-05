from rest_framework import serializers
from .models import Tarefa
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # Esconde a senha nas respostas HTTP
        }

        

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

    def validate_descricao(self, value):
        if len(value) > 40:
            raise serializers.ValidationError('o valor nao pode ser maior q 40')
        
        return value
    
