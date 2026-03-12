# Development Guidelines

## Setup
1. Install dev dependencies: `pip install -e ".[dev]"`
2. Run tests: `pytest`
3. Lint: `flake8 .`

## Branching
- `main`: Stable releases.
- `develop`: Ongoing feature work.
- `feature/*`: Specific new features.

## Coding Standards
- Use type hints for all function signatures.
- Write docstrings in Google format.
- Ensure all logic is covered by unit tests in the `tests/` directory.
