run all commands from the backend folder: cd backend

install dependencies: uv sync
to run it use this command: uv run uvicorn src.main:app --reload
or: uv run python -m src.main
add sample data: uv run python -m src.seed
note: always put "uv run" in front of python commands, plain "python" is not on PATH (it is installed in .venv)
search for db file : Get-ChildItem -Recurse -Filter *.db
