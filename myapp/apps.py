from django.apps import AppConfig

#Configurar el módulo 

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
