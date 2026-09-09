_default:
    @just --list --unsorted

# Fetches dependencies and runs migrations.
restore:
    uv sync
    uv run alembic upgrade head

# Serves, backgrounding.
serve:
    uv run app/main.py &

# Halts backgrounded service.
stop:
    # By default the application runs on port 5001.
    # This command finds applications running on port 5001 and
    # kills them.
    lsof -i ":5001" | awk '{print $2}' | tail -n +2 | xargs kill

# Runs developer instance without backgrounding
dev:
    uv run app/main.py

# Runs almbic
alembic CMD:
    uv run alembic "{{CMD}}"

# Lints codebase
lint:
    uv run ruff check

# Runs all tests
test: unit integration #e2e

[group('tests')]
unit:
    TESTING=true uv run pytest tests/unit

[group('tests')]
integration:
    TESTING=true uv run pytest tests/integration

[group('tests')]
e2e:
    echo "Disabled pending rewrite."
    #uv run playwright install 
    #TESTING=true uv run pytest tests/e2e
