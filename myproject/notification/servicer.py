from concurrent import futures
import grpc
import logging
from .proto.notification_pb2_grpc import (
    add_NotificationServiceServicer_to_server,
    NotificationServiceServicer,
)
from .proto.notification_pb2 import (
    NotificationResponse,
)

logger = logging.getLogger(__name__)


class NotificationServicer(NotificationServiceServicer):
    def SendNotification(self, request, context):
        print(f"Received notification: {request.message}")
        # Здесь можно добавить логику отправки уведомлений
        return NotificationResponse(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_NotificationServiceServicer_to_server(NotificationServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()
