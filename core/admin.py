from django.contrib import admin
from core.models import Dentista

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
     list_display = ('titulo',  'data_evento', 'data_criacao')
     list_filter = ('usuario', 'data_evento', 'data_criacao')

admin.site.register(Dentista, EventoAdmin)