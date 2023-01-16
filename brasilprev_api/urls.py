"""brasilprev_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.api.viewsets import cadastroClienteViewSet, cadastroProdutoViewSet, contratacaoPlanoViewSet, aporteExtraViewSet, resgateViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('cadastro_cliente', cadastroClienteViewSet, basename='Cadastro_cliente'),
router.register('cadastro_produto', cadastroProdutoViewSet, basename='Cadastro_produto'),
router.register('contratacao_plano', contratacaoPlanoViewSet, basename='Contratacao_plano'),
router.register('aporte_extra', aporteExtraViewSet, basename='Aporte_extra'),
router.register('resgate', resgateViewSet, basename='Resgate'),

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
