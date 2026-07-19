# Utils

Shared helpers used by every algorithm package for generating test data and
benchmarking execution time.

## Files

- `generator.py` — `Generator_Data.list_generator(size)` returns a sorted
  `list(range(size))` for use as test input.
- `timer.py` — timing helpers:
  - `Timer.time_function(func, *args, **kwargs)` — call a function once and
    get back `(result, elapsed_time)`.
  - `@time_function_decorator` — decorator that prints a function's execution
    time on every call.
  - `@time_function_decorator_global` — decorator that records
    `(input_size, elapsed_time)` per call into a shared `elapsed_times` dict,
    keyed by function name, so a function can be benchmarked across many
    input sizes and later plotted.
  - `plot_elapsed_times(log_scale=True)` — plots every function tracked by
    `@time_function_decorator_global` as execution time vs. input size, one
    line per function, useful for comparing algorithmic growth rates
    (e.g. O(log n) vs. O(n)).

## Example

```python
from utils import Generator_Data, time_function_decorator_global, plot_elapsed_times

@time_function_decorator_global
def my_algorithm(data, target):
    ...

for size in [10, 100, 1000, 10000]:
    my_algorithm(Generator_Data.list_generator(size), size // 2)

plot_elapsed_times()
```
