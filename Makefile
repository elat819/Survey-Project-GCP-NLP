setup:
	python3 -m venv ~/.myrepo

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C myrepolib cli web

all: install lint
