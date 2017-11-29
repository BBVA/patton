# Deploy to DockerHub
VERSION=$(cat VERSION)
docker build -t bbvalabs/patton:$VERSION -t bbvalabs/patton:latest .
docker login -u $DOCKER_USER -p $DOCKER_PASS
docker push bbvalabs/patton:$VERSION
docker push bbvalabs/patton:latest
