from django.db import models


class Seccion(models.Model):
    OPCIONES_AREAS = [
        ('MUSEO', 'Museo Viviente: Orquídeas'),
        ('ACUATICO', 'Jardín Acuático'),
        ('EPIFITARIO', 'Epifitario'),
        ('INVERNADEROS', 'Invernaderos'),
        ('HORTALIZAS', 'Hortalizas'),
        ('MERCADO', 'Mercado'),
    ]

    nombre = models.CharField(
        max_length=50,
        choices=OPCIONES_AREAS,
        unique=True
    )
    orden = models.PositiveIntegerField(
        default=0,
        help_text="Número para ordenar las secciones en la página principal"
    )
    descripcion_corta = models.TextField(
        blank=True,
        help_text="Texto breve y amigable para mostrar en la tarjeta principal"
    )
    descripcion_detallada = models.TextField(
        blank=True,
        help_text="Texto más completo e informativo para mostrar dentro de la ficha"
    )
    
    # NUEVOS CAMPOS BILINGÜES (inglés)
    nombre_en = models.CharField(
        max_length=100,
        blank=True,
        help_text="Nombre de la sección en inglés"
    )
    
    descripcion_corta_en = models.TextField(
        blank=True,
        help_text="Texto breve en inglés para mostrar en la tarjeta principal"
    )
    
    descripcion_detallada_en = models.TextField(
        blank=True,
        help_text="Texto más completo en inglés para mostrar dentro de la ficha"
    )
    
    enlace_seccion_completa = models.URLField(
        blank=True,
        help_text="Enlace a la página completa de esta sección (base de datos o sistema detallado)"
    )
    video_principal = models.FileField(
        upload_to='videos/',
        null=True,
        blank=True
    )
    foto_portada = models.ImageField(
        upload_to='portadas/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.get_nombre_display()


class FotoGaleria(models.Model):
    seccion = models.ForeignKey(
        Seccion,
        on_delete=models.CASCADE,
        related_name='fotos'
    )
    imagen = models.ImageField(upload_to='galeria/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foto de galería"
        verbose_name_plural = "Fotos de galería"
        ordering = ['fecha_subida']

    def __str__(self):
        return f"Imagen de {self.seccion.get_nombre_display()}"
    
    