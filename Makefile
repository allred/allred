#include .env
# https://ieftimov.com/post/golang-package-multiple-binaries/
# https://github.com/gobuffalo/packr/blob/master/packr/main.go
# checkout godag?
GOROOT = .
ALLRED_BIN = "./bin"
ALLRED_CMD = "./cmd"


build:
	#go build -v -o $(ALLRED_BIN) $(ALLRED_CMD)/glorphus
	go build -v -o $(ALLRED_BIN) $(ALLRED_CMD)/fakworker

run:
	#./bin/glorphus
	./bin/fakworker

test:
	go test
