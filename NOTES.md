## Week 1, Day 1 - August 1, 2026
- Learned variables, data types, basic operators
- Learned what f-strings are and how they work
- Built temperature converter and simple calculator
- Concepts felt: variables and operators were easy, f-strings took a moment to click

## Week 1, Day 2 - August 2, 2026
- Learned control flow: if/elif/else, for loops, while loops
- Practiced FizzBuzz and sum-with-while-loop
- Solved practice problems: even numbers loop, positive/negative/zero check
- Concepts felt: comfortable overall, learned to simplify elif to else when it's the only remaining casels

## Week 1, Day 3 - August 3, 2026
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

## Week 1, Day 4 - August 4, 2026
- Learned data structures: lists, tuples, dicts, sets
- Built get_evens() - looped through a list, appended matching items to a new list
- Learned list comprehensions as a more concise alternative to loop + append,
  e.g. [n for n in numbers if n % 2 == 0]
- Practiced printing dictionary key-value pairs with .items()
- Built remove_duplicates() using set(items), then converted back to a list
  with list(set(items))
- Learned list(dict.fromkeys(items)) as an alternative that preserves order,
  when order matters and set() alone would lose it

## Week 1, Day 5 - August 5, 2026
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

## Week 2, Day 3 - August 10, 2026
- Learned Git branching workflow: checkout -b, committing on a branch,
  switching back to main, merging, pushing, deleting the branch
- Saw firsthand that a commit made on a branch doesn't exist on main until
  merged - the file disappeared when switching to main, reappeared after merge
- Learned pull requests are the team-setting equivalent: a request to merge
  one branch into another, letting others review changes before they land
- Documented the whole workflow as comments in day3-git-practice.py

## Week 2, Day 4 - August 16, 2026
- Learned modules: created helpers.py with functions, imported into
  day4-modules.py using both `import helpers` and `from helpers import ...`
- Learned packages: a folder of modules with an __init__.py file
- Learned virtual environments: isolated Python setup per project, so
  packages for one project don't conflict with another
- Set up venv (had to install python3.12-venv via apt first), activated it,
  installed requests as a test, deactivated
- Created .gitignore with venv/ so the virtual environment folder never
  gets committed to Git

## Week 2, Day 5 - August 17, 2026
- Learned pytest: test_*.py files, test_* functions, assert statements
- Learned assert checks a condition is True - False means the test fails
  and pytest shows exactly what was expected vs what was returned
- Wrote tests for is_prime(), average(), and remove_duplicates()
- Lesson: assert average([1,2,3]) alone only checks "truthy" - always
  compare against an exact expected value with ==
- Lesson: set() doesn't preserve order, so comparing directly with ==
  against a list can create a "flaky test" - use set(result) == {...}
  for order-independent comparisons, or better, use dict.fromkeys(items)
  instead of set(items) to preserve order at the source
- Wrote multiple small, focused tests (removes duplicates / preserves
  order / empty list / no duplicates) instead of one big test

## Week 2 complete
- OOP (classes, inheritance, polymorphism, encapsulation), Git branching
  workflow, modules/venv/.gitignore, and pytest - all done

## Review session - August 19, 2026
- Rebuilt is_prime() and BankAccount from memory before starting Week 3
- Both included the professional touches (type hints, validation, square
  root optimization) without prompting - good sign the material stuck
- Wrote full pytest suites for both, including pytest.raises() for
  testing that invalid input correctly raises ValueError
- Learned Python filenames need underscores, not hyphens, to be importable