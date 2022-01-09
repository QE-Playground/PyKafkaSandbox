### I. Docker compose
I use `docker-compose.yml` file from `bitnami`.
##### 1. Start Docker:
```
docker compose up -d
```
##### 2. Show info about containers:
```
docker compose ps
```
##### 3. Shut down:
```
docker compose down
```
### II. Setup Pycharm
Pycharm will automatically sets up virtual env.

Execute this command:
```
pip install -r requirements.txt
```

### III. Running test cases:
```
cd tests
pytest test_create_topic.py
```