# Algoritmos

A small collection of classic algorithm implementations in Python, paired with
shared benchmarking utilities for comparing their performance as input size grows.

## Structure

```
algoritmos/
├── binary_search/       # Binary search vs. linear search implementations
│   ├── algorithm.py
│   ├── main.py          # Runnable benchmark + plot demo
│   └── README.md
├── utils/                # Shared timing/benchmarking/data-generation helpers
│   ├── generator.py
│   ├── timer.py
│   └── README.md
├── requirements.txt
└── README.md
```

Each algorithm lives in its own top-level package with a `README.md`
describing what it does and how to run it.

## Algorithms

- [binary_search](binary_search/README.md) — binary search vs. linear search

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running an example

Run any package's demo as a module from the repo root:

```bash
python3 -m binary_search.main
```

## Adding a new algorithm

1. Create a new top-level package, e.g. `algorithm_name/`.
2. Add `__init__.py`, `algorithm.py` (implementation), `main.py` (runnable demo), and `README.md`.
3. Reuse `utils.Generator_Data` for test data and `utils.time_function_decorator_global`
   / `utils.plot_elapsed_times` to benchmark and plot execution time vs. input size.
