# from django.http import HttpResponse


# def hello_world(request):
#     return HttpResponse("Hello, World!")
from django.http import JsonResponse
from notification.servicer import notification_manager


def hello_world(request):
    message = request.GET.get("message", "Hello from Django!")
    notification_manager.message_queue.put(message)
    return JsonResponse({"status": "Notification queued"})
