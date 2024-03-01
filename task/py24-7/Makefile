genswag:
	protoc -I . --openapiv2_out . --openapiv2_opt=allow_merge=true ./proto/*

build:
	docker build -t python-task:24-7 .

run: build
	docker run -p 8080:8080 -t python-task:24-7