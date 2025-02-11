```bash
cd myproject && python manage.py runserver # launch django + grpc in dedicated thread
cd myproject && python client.py # launch grpc test client
curl -i http://localhost:8000/hello/?message=TestMessage # send test message
```