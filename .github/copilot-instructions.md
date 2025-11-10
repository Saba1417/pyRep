## Repository snapshot

- Minimal Python project with top-level scripts: `main.py` and `test.py`.
- `README.md` contains a one-line project title only.

## Purpose for an AI coding agent

Be pragmatic: this repo currently holds small scripts rather than an app or package. Focus on clear, minimal changes that match the existing style (single-file scripts, simple print statements). When adding features, create small, well-scoped files and update `README.md` with usage notes.

## How to run and validate locally

- Run the main script: `python main.py` (project has no dependencies or packaging).
- There are no test frameworks configured; `test.py` exists but is empty. If you add tests, prefer `unittest` or a minimal `pytest` setup and add instructions to `README.md`.

## Project-specific conventions and observable patterns

- Files are simple and procedural. Follow the same style: clear top-level script behavior and minimal imports.
- Keep changes explicit and minimal: prefer editing or adding a new script over introducing heavy frameworks.

## Examples to reference

- `main.py` uses plain prints:
  - Example: `print("testname")` and `print("testname2")` — follow this simple, side-effect-first approach for scripts.
- `README.md` currently only contains a title — update it when you add runnable behavior or dependencies.

## When editing or creating files

- If you add functionality, add a short usage example to `README.md` (1–3 lines). Example: how to run the script and expected output.
- Keep new files at the repository root unless you are establishing a package (in that case add a `pyproject.toml` and explain packaging in `README.md`).

## Pull request / commit guidance for AI agents

- Keep commits small and focused (single logical change per commit). Use clear commit messages like: `feat: add greet script with example` or `chore: update README usage`.
- Update `README.md` when adding runnable behavior or third-party dependencies.

## What to avoid

- Do not introduce large frameworks or dependency manifests without the user's explicit request.
- Avoid changing global settings or environment assumptions (this repo currently has no virtualenv or CI config).

## When you need clarification from the human

- If a change requires a dependency, ask which test framework or packaging they prefer.
- If adding a CLI or service, ask for expected invocations and target environment (local script vs. package vs. web service).

---
If any of these assumptions are wrong (for example, this repo will be expanded into a package), ask a clarifying question before making large structural changes.
