# Simple python app

This is a standalone application you can run it using Docker and then access it at http://localhost:5000/

```
docker build -t simple-python-app:dev .
docker run -p 5000:5000 simple-python-app:dev 
```
