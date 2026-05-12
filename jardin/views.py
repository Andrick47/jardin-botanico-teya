from django.shortcuts import render, get_object_or_404
from .models import Seccion


def index(request):
    secciones = Seccion.objects.all().order_by('orden', 'nombre')

    portada_principal = (
        Seccion.objects.filter(nombre='MUSEO').first()
        or Seccion.objects.first()
    )

    return render(request, 'jardin/index.html', {
        'secciones': secciones,
        'portada': portada_principal,
    })


def galeria_seccion(request, seccion_id):
    seccion = get_object_or_404(Seccion, id=seccion_id)
    fotos = seccion.fotos.all()

    return render(request, 'jardin/galeria.html', {
        'seccion': seccion,
        'fotos': fotos,
    })

