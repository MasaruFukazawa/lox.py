SERVICE := lox
COMPOSE := docker compose
EXEC    := $(COMPOSE) exec $(SERVICE)
RUN     := $(COMPOSE) run --rm $(SERVICE)

.PHONY: help build up down restart shell ps logs test lint format run clean precommit-install precommit-uninstall precommit

help:
	@echo "Targets:"
	@echo "  build    - build the docker image"
	@echo "  up       - start the container in the background"
	@echo "  down     - stop and remove the container"
	@echo "  restart  - restart the container"
	@echo "  shell    - open a bash shell in the running container"
	@echo "  ps       - show container status"
	@echo "  logs     - tail container logs"
	@echo "  test     - run pytest inside the running container"
	@echo "  lint     - run ruff check inside the running container"
	@echo "  format   - run ruff format inside the running container"
	@echo "  run      - run the lox interpreter (ARGS=... to pass args)"
	@echo "  precommit-install   - point git hooks to .githooks (runs in container)"
	@echo "  precommit-uninstall - reset git hooks path to default"
	@echo "  precommit           - run all pre-commit hooks on all files (in container)"
	@echo "  clean    - remove caches"

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart: down up

shell:
	$(EXEC) /bin/bash

ps:
	$(COMPOSE) ps

logs:
	$(COMPOSE) logs -f

test:
	$(EXEC) pytest $(ARGS)

lint:
	$(EXEC) ruff check $(ARGS) .

format:
	$(EXEC) ruff format $(ARGS) .

run:
	$(EXEC) lox $(ARGS)

precommit-install:
	git config core.hooksPath .githooks
	chmod +x .githooks/pre-commit
	@echo "git hooks path set to .githooks (runs inside the container)"

precommit-uninstall:
	git config --unset core.hooksPath || true
	@echo "git hooks path reset to default"

precommit:
	$(EXEC) pre-commit run --all-files

clean:
	rm -rf .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
