PRODUCT := autotune
VERSION := $(shell cat VERSION)
WEBSITE := acksin.com

all: build

build: deps test
	go build -ldflags "-X main.version=$(VERSION)"
	$(MAKE) website-assets

deps:
	go get github.com/aktau/github-release
	go get -u github.com/golang/lint/golint
	go get -u ./...
	-cd ai && $(MAKE) deps

dev-deps:
	sudo add-apt-repository -y ppa:ubuntu-elisp/ppa && sudo apt-get -qq update && sudo apt-get -qq -f install && sudo apt-get -qq install emacs-snapshot && sudo apt-get -qq install emacs-snapshot-el;
	emacs --version
	wget https://raw.githubusercontent.com/acksin/release-checklist/master/install-orgmode.el
	emacs-snapshot --batch -l ./install-orgmode.el

test:
	golint ./...
	go test -cover ./...
	go tool vet **/*.go

archive:
	tar cvzf $(PRODUCT)-$(VERSION).tar.gz $(PRODUCT)

github-release:
	-github-release release --user acksin --repo $(PRODUCT) --tag v$(VERSION) --name "Autotune $(VERSION)" 
	-github-release upload --user acksin --repo $(PRODUCT) --tag v$(VERSION) --name "$(PRODUCT)-$(shell uname)-$(shell uname -i)-${VERSION}.tar.gz" --file $(PRODUCT)-$(VERSION).tar.gz

release: website-assets lambda-build build archive
	-git commit -m "Version $(VERSION)"
	-git tag v$(VERSION) && git push --tags
	$(MAKE) github-release
	s3cmd put --acl-public $(PRODUCT)-$(VERSION).tar.gz s3://assets.acksin.com/$(PRODUCT)/${VERSION}/$(PRODUCT)-$(shell uname)-$(shell uname -i)-${VERSION}.tar.gz

website-assets:
	emacs DOCS.org --batch --eval '(org-html-export-to-html nil nil nil t)'  --kill
	echo "---" > docs.html.erb
	echo "title: Autotune Docs" >> docs.html.erb
	echo "layout: docs" >> docs.html.erb
	echo "description: Documentation for Autotune. Tool to diagnoses Linux augmented with Machine Learning" >> docs.html.erb
	echo "---" >> docs.html.erb
	cat DOCS.html >> docs.html.erb
	rm DOCS.html
	-cp docs.html.erb $$GOPATH/src/github.com/acksin/fugue/acksin.com/source/autotune/

lambda-build:
	cd ai && $(MAKE) release
