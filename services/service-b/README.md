Build the image
docker build -t flask-app:latest .

After the build completes, run the container:
docker run -d -p 80:5000 service_b