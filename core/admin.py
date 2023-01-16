from django.contrib import admin
from .models import Cadastro_cliente, Cadastro_produto, Contratacao_plano, Aporte_extra, Resgate

# Register your models here.

admin.site.register(Cadastro_cliente)
admin.site.register(Cadastro_produto)
admin.site.register(Contratacao_plano)
admin.site.register(Aporte_extra)
admin.site.register(Resgate)