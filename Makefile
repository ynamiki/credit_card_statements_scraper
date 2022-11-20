venv = .venv
pip = $(venv)/bin/python -m pip
black = $(venv)/bin/black
chromedriver = $(venv)/bin/chromedriver

all:

$(venv):
	python3 -m venv $(venv)

$(black): $(venv)
	$(pip) install black

format:
	$(black) main.py

$(chromedriver): $(venv)
	curl -o chromedriver.zip https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_mac_arm64.zip
	unzip chromedriver.zip -d $(venv)/bin/
	rm chromedriver.zip

clean:
	rm -r $(venv)
