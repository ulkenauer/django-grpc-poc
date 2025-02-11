from concurrent import futures
import grpc
import logging
from .proto.notification_pb2_grpc import (
    add_NotificationServiceServicer_to_server,
    NotificationServiceServicer,
)
# from .proto.notification_pb2 import (
#     NotificationResponse,
# )
import threading
import queue
from collections import deque

from notification.proto import notification_pb2

from notification.proto import notification_pb2_grpc

logger = logging.getLogger(__name__)


class NotificationManager:
    def __init__(self):
        self.subscribers = deque()
        self.lock = threading.Lock()
        self.message_queue = queue.Queue()
        self.thread = threading.Thread(target=self._process_messages, daemon=True)
        self.thread.start()

    def _process_messages(self):
        while True:
            message = self.message_queue.get()
            with self.lock:
                print(message)
                print(self.subscribers)
                for sub in list(self.subscribers):
                    try:
                        print("send")
                        sub["stream"].put(message)
                        # sub["stream"].send(message)
                    except Exception as err:
                        print("err")
                        print(err)
                        self.subscribers.remove(sub)

    def add_subscriber(self, stream, user_id):
        with self.lock:
            self.subscribers.append({"stream": stream, "user_id": user_id})


notification_manager = NotificationManager()


class NotificationServicer(notification_pb2_grpc.NotificationServiceServicer):
    def Subscribe(self, request, context):
        def message_generator():
            q = queue.Queue()
            print("sub")
            notification_manager.add_subscriber(q, request.user_id)
            while context.is_active():
                try:
                    message = q.get(timeout=1)
                    yield notification_pb2.Notification(content=message)
                except queue.Empty:
                    continue

        return message_generator()


# class NotificationServicer(NotificationServiceServicer):
#     def SendNotification(self, request, context):
#         print(f"Received notification: {request.message}")
#         # Здесь можно добавить логику отправки уведомлений
#         return NotificationResponse(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_NotificationServiceServicer_to_server(NotificationServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()
