from core.models import Cadastro_cliente, Cadastro_produto, Contratacao_plano, Aporte_extra, Resgate
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from datetime import date, datetime

date = date.today()
date_atual = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}'

class cadastroClienteSerializer(ModelSerializer):
    class Meta:
        model = Cadastro_cliente
        fields = "__all__"

class cadastroProdutoSerializer(ModelSerializer):
    class Meta:
        model = Cadastro_produto
        fields = "__all__"
    
    def validate_valorMinimoAporteInicial(self, valor):
        if valor >= 1000:
            return valor
        raise serializers.ValidationError("Valor minimo do aporte inicial: 1000R$.")
    
    def validate_valorMinimoAporteExtra(self, valor):
        if valor >= 100:
            return valor
        raise serializers.ValidationError("Valor minimo do aporte extra: 100R$.")
    
    def validate_idadeDeEntrada(self, valor):
        if valor >= 18:
            return valor
        raise serializers.ValidationError("A idade minima para comprar um produto é de 18 anos.")
    
    def validate_idadeDeSaida(self, valor):
        if valor >= 60:
            return valor
        raise serializers.ValidationError("A idade máxima para começar a usufruir dos benéficios é de 60 anos.")
    
    def validate_carenciaInicialDeResgate(self, valor):
        if valor >= 60:
            return valor
        raise serializers.ValidationError("O périodo de carência para realizar o primeiro resgate é de 60 dias.")
    
    def validate_carenciaEntreResgates(self, valor):
        if valor >= 30:
            return valor
        raise serializers.ValidationError("O périodo de carência para realizar outro resgate é de 30 dias.")
    
class contratacaoPlanoSerializer(ModelSerializer):
    # triggerid = request.POST.get('triggerid')
    class Meta:
        model = Contratacao_plano
        fields = '__all__'

    def validate_idProduto(self, valor):
        if str(valor.expiracaoDeVenda) > date_atual:
            return valor
        raise serializers.ValidationError("Não foi possível contratar o produto! Produto com prazo de venda expirado.")
    
    def validate_aporte(self, valor):
        if valor >= 1000:
            return valor
        raise serializers.ValidationError("O valor minimo do aporte é de 1000R$")

class aporteExtraeSerializer(ModelSerializer):
    class Meta:
        model = Aporte_extra
        fields = '__all__'
    
    def validate_valorAporte(self, valor):
        if valor >= 100:
            return valor
        raise serializers.ValidationError("Valor minimo do aporte: 100R$")

class resgateSerializer(ModelSerializer):
    class Meta:
        model = Resgate
        fields = "__all__"
    
    def validate_idPlano(self, valor):
        day_contratação = datetime.strptime(str(valor.dataDaContratacao), '%Y-%m-%d')
        day_atual = datetime.strptime(date_atual, '%Y-%m-%d')
        FirstResgate = abs((day_contratação - day_atual).days)

        if FirstResgate >= 60:
            return valor
        raise serializers.ValidationError(f"Resgate recusado! O periodo para o primeiro resgate é de 60 dias ápos a contratação do plano, faz {FirstResgate} dias que o plano foi adquirido.")
    

    def validate_valorResgate(self, valor):
        if valor >= 1000:
            return valor       
        raise serializers.ValidationError("Valor minimo para o resgate é de 1000R$")