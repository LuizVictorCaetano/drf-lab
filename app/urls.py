from django.urls import path, include
from .views import HelloAPI, TarefaAPI, DetailTarefa, TarefaListCreateView, TarefaCreate, TarefaList, TarefaRetrive, TarefaViewSets, UserViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tarefa', TarefaViewSets)
router.register(r'user', UserViewSets)

urlpatterns = [
    path('hello/', HelloAPI.as_view()),
    path('tarefa/', TarefaAPI.as_view()),
    path('detailview/<int:pk>/', DetailTarefa.as_view()),
    path('tarefacreatelist/', TarefaListCreateView.as_view()),
    path('tarefacreate/', TarefaCreate.as_view()),
    path('tarefaget/', TarefaList.as_view()),
    path('tarefaretrive/<int:pk>/', TarefaRetrive.as_view()),
    path('', include(router.urls))
]
