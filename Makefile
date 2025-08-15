docker:
	docker build -t myagent .

run:
	docker run --env-file .env -p 8000:8000 myagent