from django.apps import AppConfig


class DjangoModelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_model_app'
