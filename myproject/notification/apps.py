from django.apps import AppConfig
import threading
from .servicer import serve


class NotificationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notification"

    def ready(self):
        print("ASDASD")
        # if not self.is_running_test_server():
        server_thread = threading.Thread(target=serve, daemon=True)
        server_thread.start()

    def is_running_test_server(self):
        import sys

        return "runserver" in sys.argv
