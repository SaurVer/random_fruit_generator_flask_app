# Makefile for Python Project

# Variables
PYTHON = python
PIP = $(PYTHON) -m pip
PROJECT_NAME = random_fruit_generator_flask_app

# Phony targets (targets that are not actual files)
.PHONY: help install run lint format test clean

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  install  : Install dependencies from requirements.txt"
	@echo "  run      : Run the main.py script"
	@echo "  lint     : Run linters (e.g., flake8)"
	@echo "  format   : Format code (e.g., using black)"
	@echo "  test     : Run tests if available"
	@echo "  clean    : Remove temporary files and directories"

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) *.py

lint:
	flake8  *.py # Adjust with your specific linting command (e.g., pylint)

format:
	black *.py # Adjust with your specific code formatting tool (e.g., autopep8)

test:
	$(PYTHON) test.py

clean:
	@# Add clean-up commands here (e.g., remove temporary files, directories)

# Default target
all: install lint test

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete