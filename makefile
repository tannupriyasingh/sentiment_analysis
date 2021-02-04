build:
	docker build -t senti .

run: build
	docker run -it senti:latest
