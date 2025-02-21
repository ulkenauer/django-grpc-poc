# Django + GRPC server
Proof of concept of launch GRPC server with Django in a single process with communication via python queue

TODO:
1. Use async GRPC server

## Launch
```bash
cd myproject && python manage.py runserver # launch django + grpc in dedicated thread
cd myproject && python client.py # launch grpc test client
curl -i http://localhost:8000/hello/?message=TestMessage # send test message
```
