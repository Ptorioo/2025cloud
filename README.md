# 2025cloud

## How to build & run

Build the Docker image:
```
docker build -t flask-app .
```
Run the container:
```
docker run -p 5000:5000 flask-app
```

## Development Process

![diagram](/diagram.jpg)

After the developer submits a Push/Pull Request to GitHub, the GitHub Action is triggered to automatically execute the build process and finally push the generated image file to Docker Hub.
The latest image push will be tagged as latest, the base (without other dev dependencies) will be tagged as base.