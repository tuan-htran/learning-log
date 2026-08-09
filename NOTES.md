## Day 1 - August 1, 2026
- Learned variables, data types, basic operators
- Learned what f-strings are and how they work
- Built temperature converter and simple calculator
- Concepts felt: variables and operators were easy, f-strings took a moment to click

## Day 2 - August 2, 2026
- Learned control flow: if/elif/else, for loops, while loops
- Practiced FizzBuzz and sum-with-while-loop
- Solved practice problems: even numbers loop, positive/negative/zero check
- Concepts felt: comfortable overall, learned to simplify elif to else when it's the only remaining casels

## Day 3 - August 3, 2026
- Learned functions (def, parameters, return, default parameters)
- Learned scope: local vs global variables
- Learned try/except error handling
- Built average() and is_prime() functions
- Debugged is_prime() logic: initially returned inside the loop after checking
  just one divisor instead of checking all divisors before deciding - learned
  that "check everything before deciding" logic belongs after the loop, not
  inside a branch
- Saw an optimized is_prime() version using the square root trick (only need
  to check divisors up to √n) and skipping even numbers
- Practiced try/except for bad input (ValueError), learned to only catch
  exceptions that can actually occur in that code (removed unused
  ZeroDivisionError handler since there was no division happening)

## Day 4 - August 4, 2026
- Learned data structures: lists, tuples, dicts, sets
- Built get_evens() - looped through a list, appended matching items to a new list
- Learned list comprehensions as a more concise alternative to loop + append,
  e.g. [n for n in numbers if n % 2 == 0]
- Practiced printing dictionary key-value pairs with .items()
- Built remove_duplicates() using set(items), then converted back to a list
  with list(set(items))
- Learned list(dict.fromkeys(items)) as an alternative that preserves order,
  when order matters and set() alone would lose it

## Day 5 - August 5, 2026
- Learned string manipulation: strip(), lower(), upper(), replace(), split(), join(), slicing
- Learned file I/O: writing and reading files with `with open(...) as f`
- Built word counter using split() and len()
- Built sentence reverser using split()[::-1] and join()
- Wrote about_me.txt with 3 facts, read it back
- Learned writelines() and using a list of strings instead of repeated
  .write() calls, plus wrapping file operations in try/except for robustness

## Week 1 complete
- Python fundamentals: variables, control flow, functions, data structures,
  string manipulation, file I/O - all done


## Week 2, Day 1 - August 6, 2026
- Learned classes, objects, attributes, methods, and __init__
- Learned self: it's how a method knows which specific object's data to use
  (Python passes the object in automatically when you call obj.method())
- Built BankAccount class with deposit(), withdraw(), check_balance()
- Debugged operator typos: =- instead of -= for withdraw
- Saw a more professional version with docstrings, type hints, and input
  validation (raising ValueError for invalid amounts)

## Week 2, Day 2 - August 8, 2026
- Learned inheritance: subclasses inherit attributes/methods, can override them
- Learned polymorphism: different classes respond to the same method call in
  their own way (e.g. shape.area() behaves differently per subclass)
- Learned encapsulation: underscore convention (_balance) signals "internal,
  use methods instead of touching directly"
- Built Shape/Rectangle/Circle classes practicing inheritance + polymorphism
- Learned Python's abc module: ABC + @abstractmethod enforces that subclasses
  must implement required methods, catching mistakes immediately instead of
  silently later
- Learned type hints (e.g. `-> float`, `width: float`) - documentation for
  humans/tooling, not enforced at runtime