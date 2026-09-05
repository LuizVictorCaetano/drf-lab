from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User

class UserViewSets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class TarefaViewSets(viewsets.ModelViewSet):
    queryset=Tarefa.objects.all()
    serializer_class=TarefaSerializer
    permission_classes=[IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        print("USUÁRIO:", request.user)
        print("ESTÁ AUTENTICADO?:", request.user.is_authenticated)
        return super().list(request, *args, **kwargs)

class TarefaListCreateView(generics.ListCreateAPIView):
    queryset=Tarefa.objects.all()
    serializer_class=TarefaSerializer

class TarefaList(generics.ListAPIView):
    queryset=Tarefa.objects.all()
    serializer_class=TarefaSerializer

class TarefaCreate(generics.CreateAPIView):
    queryset=Tarefa.objects.all()
    serializer_class=TarefaSerializer

class TarefaRetrive(generics.RetrieveAPIView):
    queryset=Tarefa.objects.all()
    serializer_class=TarefaSerializer

class HelloAPI(APIView):
    def get(self, request):
        return Response({'msg':'hello'})

class TarefaAPI(APIView):
    def get(self, request):
        tarefa = Tarefa.objects.all()
        seralizer = TarefaSerializer(tarefa, many=True)
        return Response(seralizer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DetailTarefa(APIView):
    def get(self, request, pk, *args, **kwargs,):
        #pegar o id do bd e mandar para rota
        tarefa = get_object_or_404(Tarefa, pk=pk)
        #passar o db para serializer
        serializer = TarefaSerializer(tarefa)
        #passar json para o serializer e retornar 200
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #autoalização completa
    def put(self, request, pk, *args, **kwargs):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        serializer=TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save() #executa o uptade
            return Response(serializer.data, status=status.HTTP_200_OK)
        #errors para mostrar 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, *args, **kwargs):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
