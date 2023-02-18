docker image build -t assignment3image:alpine .

docker run assignment3image:alpine

docker save -o assignment3image.tar assignment3image

docker load -i assignment3image.tar

docker run assignment3image:alpine
