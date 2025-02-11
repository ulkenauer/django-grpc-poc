import grpc
from notification.proto import notification_pb2
from notification.proto import notification_pb2_grpc


def run_client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = notification_pb2_grpc.NotificationServiceStub(channel)

    subscription = stub.Subscribe(
        notification_pb2.SubscriptionRequest(user_id="test_user")
    )

    try:
        for response in subscription:
            print(f"Received notification: {response.content}")
    except KeyboardInterrupt:
        print("Client stopped")


if __name__ == "__main__":
    run_client()

# import time
# import grpc
# from notification.proto.notification_pb2 import NotificationRequest
# from notification.proto.notification_pb2_grpc import NotificationServiceStub


# def send_notification(message: str):
#     channel = grpc.insecure_channel("localhost:50051")
#     stub = NotificationServiceStub(channel)
#     response = stub.SendNotification(NotificationRequest(message=message))
#     print(f"Server response: {response.success}")
#     time.sleep(2)
#     response = stub.SendNotification(NotificationRequest(message=message))
#     print(f"Server response: {response.success}")


# if __name__ == "__main__":
#     send_notification("Hello from Django gRPC!")
