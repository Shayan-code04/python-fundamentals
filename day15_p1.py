def filter_evens(numbers):
    """Return only the even numbers from a list using filter() and lambda."""
    return list(filter(lambda num: num % 2 == 0, numbers))


def square_numbers(numbers):
    """Return a list containing the square of each number using map() and lambda."""
    return list(map(lambda num: num ** 2, numbers))


def uppercase_keys(data):
    """Return a new dictionary with all keys converted to uppercase."""
    return {key.upper(): value for key, value in data.items()}


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    students = {
        "alice": 90,
        "bob": 85,
        "charlie": 95
    }

    print("Even Numbers:")
    print(filter_evens(numbers))

    print("\nSquared Numbers:")
    print(square_numbers(numbers))

    print("\nUppercase Dictionary Keys:")
    print(uppercase_keys(students))




    ## Day 15 — List Comprehensions + Lambda + map()/filter()

### What I learned
"""- List and dict comprehension syntax: `[expr for x in iterable if condition]`
- Lambda functions: `lambda x: expression`
- `map(func, iterable)` and `filter(func, iterable)` — both return iterators, wrapped in `list()` to materialize

### Rewriting old programs — when comprehensions help (and when they don't)
Reviewed 5 programs from Days 1–4 to identify which benefit from comprehension rewrites:

- **FizzBuzz (day02_p2)** — NOT rewritten. Multi-branch conditional logic with print side-effects doesn't belong in a comprehension; forcing it in makes the code harder to read, not easier.
- **Star pattern (day02_p5)** — NOT rewritten. Same reason — visual/print side-effects across nested loops, not data construction.
- **Multiplication table (day02_p3)** — Rewritten. Separated data generation (comprehension) from display (`print`/`join`), making the function reusable and testable.
- **Primes 1–100 (day03_p2)** — Rewritten. Classic filter-into-list pattern, a clean comprehension fit.
- **Word frequency (day03_p5)** — NOT rewritten as a comprehension. Counting requires accumulating state across iterations, which comprehensions can't do. `collections.Counter` is the correct tool instead.

**Key takeaway:** comprehensions are for filtering, transforming, or building a collection in one clear expression — not for multi-branch logic, side effects, or stateful accumulation. Knowing when *not* to use one matters as much as the syntax itself.

### New programs (day15/day15_p2.py)
- `filter_evens()` — using `filter()` + `lambda`
- `square_numbers()` — using `map()` + `lambda`
- `uppercase_keys()` — using dict comprehension (map/filter don't have a clean equivalent for transforming dict keys, so comprehension is the idiomatic choice here)"""