from django.apps import AppConfig


class PhoneCheckerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "phone_checker"

    def ready(self):
        """
        При запуске приложение запускается загрузка реестра если его нет, либо если UPDATE_REGISTRY_ON_START = True (Принудительная загрузка реестра)
        """
        from phone_checker.tasks import load_numeric_registry

        from app.settings import UPDATE_REGISTRY_ON_START

        if UPDATE_REGISTRY_ON_START:
            load_numeric_registry.delay()
