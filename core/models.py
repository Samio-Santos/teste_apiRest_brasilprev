from django.db import models

from datetime import date, datetime

date = date.today()
date_atual = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}'

# Create your models here.
class Cadastro_cliente(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    dataDeNascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    rendaMensal = models.FloatField()

    class Meta:
        verbose_name_plural = "Cadastro Cliente"

    def __str__(self):
        return self.name


class Cadastro_produto(models.Model):
    name = models.CharField(max_length=200)
    susep = models.CharField(max_length=200)
    expiracaoDeVenda = models.DateField()
    valorMinimoAporteInicial = models.FloatField()
    valorMinimoAporteExtra =  models.FloatField()
    idadeDeEntrada = models.IntegerField()
    idadeDeSaida = models.IntegerField()
    carenciaInicialDeResgate = models.IntegerField()
    carenciaEntreResgates = models.IntegerField()


    class Meta:
        verbose_name_plural = "Cadastro Produto"
        

    def __str__(self):
        return self.name

class Contratacao_plano(models.Model):
    idCliente = models.ForeignKey(Cadastro_cliente, on_delete=models.CASCADE)
    idProduto = models.ForeignKey(Cadastro_produto, on_delete=models.CASCADE)
    aporte = models.FloatField()
    dataDaContratacao = models.DateField() 

    class Meta:
        verbose_name_plural = "Contratação Plano"

    def __str__(self):
        return self.idProduto.name

class Aporte_extra(models.Model):
    idCliente = models.ForeignKey(Cadastro_cliente, on_delete=models.CASCADE)
    idPlano = models.ForeignKey(Contratacao_plano, on_delete=models.CASCADE)
    valorAporte = models.FloatField()

    class Meta:
        verbose_name_plural = "Aporte Extra"

    def __str__(self):
        return self.idCliente.name
    

class Resgate(models.Model):
    idPlano = models.ForeignKey(Contratacao_plano, on_delete=models.CASCADE)
    valorResgate = models.FloatField()

    class Meta:
        verbose_name_plural = "Resgate"

    def __str__(self):
        return self.idPlano.idProduto.name