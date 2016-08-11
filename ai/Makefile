all: dev

release:
	cd mental_models && serverless deploy --stage prod

dev:
	cd mental_models && serverless deploy

deps:
	npm install -g serverless@beta
