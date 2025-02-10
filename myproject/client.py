import time
import grpc
from notification.proto.notification_pb2 import NotificationRequest
from notification.proto.notification_pb2_grpc import NotificationServiceStub


def send_notification(message: str):
    channel = grpc.insecure_channel("localhost:50051")
    stub = NotificationServiceStub(channel)
    response = stub.SendNotification(NotificationRequest(message=message))
    print(f"Server response: {response.success}")
    time.sleep(2)
    response = stub.SendNotification(NotificationRequest(message=message))
    print(f"Server response: {response.success}")


if __name__ == "__main__":
    send_notification("Hello from Django gRPC!")
