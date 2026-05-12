from django.contrib import admin
from .models import Seccion, FotoGaleria


class FotoGaleriaInline(admin.TabularInline):
    model = FotoGaleria
    extra = 1


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en', 'orden')
    list_editable = ('orden',)
    search_fields = (
        'nombre',
        'nombre_en',
        'descripcion_corta',
        'descripcion_corta_en',
        'descripcion_detallada',
        'descripcion_detallada_en',
    )
    ordering = ('orden', 'nombre')

    fieldsets = (
        ('Información general', {
            'fields': ('nombre', 'nombre_en', 'orden')
        }),
        ('Contenido en español', {
            'fields': ('descripcion_corta', 'descripcion_detallada')
        }),
        ('Contenido en inglés', {
            'fields': ('descripcion_corta_en', 'descripcion_detallada_en')
        }),
        ('Multimedia y enlaces', {
            'fields': ('foto_portada', 'video_principal', 'enlace_seccion_completa')
        }),
    )

    inlines = [FotoGaleriaInline]


@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('seccion', 'fecha_subida')
    search_fields = ('seccion__nombre',)
    ordering = ('seccion', 'fecha_subida')

    