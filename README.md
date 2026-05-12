# Jardín Botánico Hacienda Teya

Sistema web desarrollado en Django para presentar las principales áreas del Jardín Botánico de Hacienda Teya.

## Tecnologías utilizadas

- Python
- Django
- HTML, CSS y Bootstrap
- SQLite
- Docker
- Gunicorn
- WhiteNoise

## Funcionalidades principales

- Página principal informativa
- Secciones del jardín
- Galería fotográfica por sección
- Video principal por sección
- Panel administrativo de Django
- Contenido editable desde el administrador
- Soporte bilingüe Español / Inglés
- Enlace preparado para futuras secciones completas

## Requisitos para despliegue

- Ubuntu 24.04 LTS
- Docker
- Docker Compose
- Red externa `npm_proxy` creada por Nginx Proxy Manager

## Variables de entorno

Crear un archivo `.env` tomando como base `.env.example`.

Ejemplo:

```env
SECRET_KEY=clave_segura
DEBUG=False
ALLOWED_HOSTS=dominio.com,www.dominio.com
CSRF_TRUSTED_ORIGINS=https://dominio.com,https://www.dominio.com

