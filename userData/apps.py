from django.apps import AppConfig


class UserdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userData'
    def ready(self):
        import userData.signals