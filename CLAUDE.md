# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace Overview

This is a multi-project development workspace containing independent projects. There is no top-level build system; each subdirectory is self-contained.

## Projects

### `ccode/` — Tic Tac Toe (Flask + Minimax AI)
A tic-tac-toe game with both a terminal CLI and a Flask web UI. The AI uses minimax for optimal play.

- **`tictactoe.py`** — Game engine: board logic, minimax AI, and terminal UI. Exports `EMPTY`, `HUMAN`, `AI`, `check_winner`, `is_full`, `ai_move` for use by the web app.
- **`app.py`** — Flask web server exposing `/` (serves `index.html`) and `/move` (POST, accepts `{board, position}`, returns updated board + game status).
- **`templates/index.html`** — Single-page frontend that communicates with `/move` via fetch.
- Has its own git repo.

**Run the web app:**
```bash
cd ccode && python app.py  # starts Flask dev server on port 5000
```

**Run the terminal game:**
```bash
cd ccode && python tictactoe.py
```

### `unsloth/` — LLM Fine-tuning Script
`test_unsloth.py` — Script for fine-tuning LLMs (e.g., Gemma 3 4B) using Unsloth + LoRA + SFTTrainer from trl. Requires GPU, CUDA, and the `unsloth`, `trl`, `datasets`, and `torch` packages.

### `testgpu.py` — CUDA/Numba GPU Sanity Test
A standalone script that verifies CUDA availability and runs a simple GPU kernel via Numba.

```bash
python testgpu.py
```

## Python Environment

A local virtualenv exists at `myenv/`. Activate with:
```bash
source myenv/bin/activate
```
