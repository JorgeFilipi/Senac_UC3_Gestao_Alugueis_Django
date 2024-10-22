from django.contrib import admin
from imoveis.models import Imovel, Inquilino, Aluguel

admin.site.register(Imovel)
admin.site.register(Inquilino)
admin.site.register(Aluguel)