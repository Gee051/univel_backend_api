from django.apps import AppConfig


class StudentApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_api'
    
    
    # def ready(self):
    #    from . import signals
    
