### Required skills: 
Pycharm, Docker Compose, pytest (at basic level).
### I. Docker compose
I use `docker-compose.yml` file from `bitnami`. See https://github.com/bitnami/bitnami-docker-kafka for further info.
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
pytest test_create_topic.py -s
```

### Donations:
If you think that any information you obtained here is worth of some money and are willing to pay for it, feel free to send any amount through paypal.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/TruongDang85)
