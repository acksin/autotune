all: dev

release:
	cd mental_models && serverless deploy --stage prod

dev:
	cd mental_models && serverless deploy

upgrade-dev:
	cd mental_models && serverless invoke -l -f mentalmodels -s dev --path upgrade-event.json

upgrade-prod:
	cd mental_models && serverless invoke -l -f mentalmodels -s prod --path upgrade-event.json

deps:
	npm install -g serverless@beta
