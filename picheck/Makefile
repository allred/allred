#include .env
# https://ieftimov.com/post/golang-package-multiple-binaries/
# https://github.com/gobuffalo/packr/blob/master/packr/main.go
# checkout godag?
GOROOT = .
PYCHECK_BIN = "./bin"
PYCHECK_CMD = "./cmd"

debug:
	cd cmd/fluxcheck && dlv debug

build:
	go build -v -o $(PYCHECK_BIN) $(PYCHECK_CMD)/fluxcheck

run:
	./bin/fluxcheck

test:
	go test
