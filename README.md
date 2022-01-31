# flask
1. Go inside the flask_app and build the docker image with command docker build -t flask:latest tag
2. Test with docker itself docker run --rm -p 8080:8080 flask:latest
3. Open another terminal and curl -F file=@file.jpeg http://ip:8080/
4. deploy the application using helm.

