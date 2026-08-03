## Day 1 - August 1, 2026
- Learned variables, data types, basic operators
- Learned what f-strings are and how they work
- Built temperature converter and simple calculator
- Concepts felt: variables and operators were easy, f-strings took a moment to click

## Day 2 - August 1, 2026
- Learned control flow: if/elif/else, for loops, while loops
- Practiced FizzBuzz and sum-with-while-loop
- Solved practice problems: even numbers loop, positive/negative/zero check
- Concepts felt: comfortable overall, learned to simplify elif to else when it's the only remaining casels

## Day 3 - August 1, 2026
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