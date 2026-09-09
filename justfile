_default:
    @just --list --unsorted

restore:
    uv sync
    uv run alembic upgrade head

serve:
    uv run app/main.py &

stop:
    port=${PORT:-5001}
    # By default the application runs on port 5001.
    # This command finds applications running on port 5001 and
    # kills them.
    lsof -i ":$port" | awk '{print $2}' | tail -n +2 | xargs kill

dev:
    uv run app/main.py

alembic:
    uv run alembic "$@"

lint:
    uv run ruff check

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
