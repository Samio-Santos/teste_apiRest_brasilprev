from core.api.serializers import cadastroClienteSerializer, cadastroProdutoSerializer, contratacaoPlanoSerializer, aporteExtraeSerializer, resgateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from datetime import datetime, date

from core.models import Cadastro_cliente, Cadastro_produto, Contratacao_plano, Aporte_extra, Resgate

date = date.today()
date_atual = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}'

class cadastroClienteViewSet(ModelViewSet):
    queryset = Cadastro_cliente.objects.all()
    serializer_class = cadastroClienteSerializer


class cadastroProdutoViewSet(ModelViewSet):
    queryset = Cadastro_produto.objects.all()
    serializer_class = cadastroProdutoSerializer


class contratacaoPlanoViewSet(ModelViewSet):
    serializer_class = contratacaoPlanoSerializer

    def get_queryset(self):
        return Contratacao_plano.objects.all()
    
    def create(self, request):
        serializer = contratacaoPlanoSerializer(data=request.data)

        if serializer.is_valid():
            data = request.data
            aporteInicialProduto = Cadastro_produto.objects.filter(id=data['idProduto']).values()
            dataCliente= Cadastro_cliente.objects.filter(id=data['idCliente']).values()

            # Traz informações dos valores de aporte, tanto do produto quanto do plano.
            valorMinimo_Aporte_Inicial_Produto = aporteInicialProduto[0]['valorMinimoAporteInicial']
            aportePlano = float(data['aporte'])

            # Traz Informações da idade minima para adquitir um produto.
            idadeMinimaProduto = aporteInicialProduto[0]['idadeDeEntrada']

            # data de nascimento do cliente
            dataDeNascimentoCliente = dataCliente[0]["dataDeNascimento"]

            # faz um calculo para trazer a idade do cliente
            data_atual = datetime.strptime(date_atual, '%Y-%m-%d')
            current_date = datetime.strptime(str(dataDeNascimentoCliente), '%Y-%m-%d')
            idadeClinte = abs((data_atual - current_date).days) // 365


            if aportePlano < valorMinimo_Aporte_Inicial_Produto:
                return Response({f"O valor inicial para contratar este produto é de: {valorMinimo_Aporte_Inicial_Produto}"})
            
            if idadeClinte < idadeMinimaProduto:
                return Response({f"O cliente não tem a idade minima para adquirir este produto! A idade minima para adquirir o produto é de: {idadeMinimaProduto} anos."})
            
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class aporteExtraViewSet(ModelViewSet):
    serializer_class = aporteExtraeSerializer

    def get_queryset(self):
        return Aporte_extra.objects.all()
    
    def create(self, request):
        serializer = aporteExtraeSerializer(data=request.data)

        if serializer.is_valid():
            data = request.data
            aportePlano = Contratacao_plano.objects.filter(id=data['idPlano']).values()

            aportePlano = aportePlano[0]['aporte']
            aporte_extra_plano = float(data['valorAporte'])
            calcAportes = aportePlano + aporte_extra_plano

            Contratacao_plano.objects.filter(id=data['idPlano']).update(aporte=calcAportes)
            
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class resgateViewSet(ModelViewSet):
    serializer_class = resgateSerializer

    def get_queryset(self):
        return Resgate.objects.all()

    def create(self, request):
        serializer = resgateSerializer(data=request.data)

        if serializer.is_valid():
            data = request.data
            aportePlano = Contratacao_plano.objects.filter(id=data['idPlano']).values()

            aportePlano = aportePlano[0]['aporte']
            valorResgate = float(data['valorResgate'])
            calcAportes = aportePlano - valorResgate

            if valorResgate > aportePlano:
                return Response({f"O valor do resgate não pode ser maior que o valor do aporte! O valor do aporte ao plano é de: {aportePlano}"})

            else:
                Contratacao_plano.objects.filter(id=data['idPlano']).update(aporte=calcAportes)
                serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)