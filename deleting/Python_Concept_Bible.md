# Python Concept Bible
> CIS 1100 — Complete Exam Reference

---

## 1. Basics & Hello World

### Core Concepts
- Programs are `.py` files executed top-to-bottom, one statement at a time
- `print()` displays output; `input()` reads user input (always returns `str`)
- Comments use `#` — ignored by Python
- File naming: `snake_case.py`

### Syntax / Patterns
```python
print("Hello, world!")           # basic output
name = input("Enter name: ")     # input() always returns str
print("Hello,", name)            # comma-separated print adds spaces
print(f"Hello, {name}!")         # f-string (preferred)

# Comments
# This is a comment
x = 5  # inline comment
```

### Key Rules
- Execution order: top to bottom, left to right
- `print()` returns `None`
- `input()` always returns `str`, even for numbers

### Common Pitfalls
- Forgetting to convert `input()` result: `age = int(input("Age: "))`
- `print(x, y)` prints with a space between; `print(x + y)` concatenates

### Exam Traps
- `print("hello")` returns `None`; `result = print("hi")` → `result` is `None`
- Each `print()` call goes on its own line

---

## 2. Variables & Expressions

### Core Concepts
- Variable: named portion of memory storing one value at a time
- Assignment operator `=` creates/updates variables
- Old value is overwritten forever on reassignment
- Variables are references (not boxes containing values directly)

### Syntax / Patterns
```python
year = 2024
first_name = "Harry"
pi = 3.14159

# Augmented assignment
score = 0
score = score + 8    # long form
score += 8           # short form (also -=, *=, /=)

# f-strings
age = 27
print(f"I am {age}, next year I'll be {age + 1}.")

# Multiple values on one print
print(num, "bottles of beer")
```

### Key Rules
- Variables store the *result* of evaluating the RHS at time of assignment
- `a = b = 5` assigns 5 to both; later changing `b` does NOT affect `a`
- snake_case: lowercase letters, words separated by `_`, no leading digits

### Common Pitfalls
```python
a = 10
b = a
a = 5
print(b)  # still 10! assignment copies the value, not a link
```

### Exam Traps
- `x = x + 1` is valid (uses old value of x on RHS, then stores result)
- Variable names cannot be Python keywords (`if`, `for`, `return`, `import`, etc.)
- `2_color` is invalid (can't start with digit); `color_2` is valid

---

## 3. Data Types

### Core Concepts
- `int` — whole numbers (no fractional part), exact arithmetic
- `float` — numbers with decimal parts, may have precision errors
- `bool` — `True` or `False` (capital T/F, no quotes)
- `str` — sequence of characters, surrounded by `"` or `'`
- `None` — absence of a value (single value type)

### Syntax / Patterns
```python
# Arithmetic operators
3 + 5     # 8  (int)
3 / 2     # 1.5 (always float)
3 // 2    # 1  (integer division, truncates toward 0)
5 % 2     # 1  (modulo: remainder)
2 ** 3    # 8  (exponentiation)

# float is "contagious"
3 + 5.0   # 8.0 (float)

# Relational operators (always return bool)
4 == 4    # True
4 != 5    # True
3 < 5     # True
"a" < "b" # True (alphabetical)

# Logical operators
True and False  # False
True or False   # True
not True        # False

# Chained comparisons
0 < x <= 20     # same as (0 < x) and (x <= 20)

# Type conversion
int("42")       # 42
float("3.14")   # 3.14
str(42)         # "42"
bool("True")    # True (any non-empty string is True!)
```

### Key Rules
- `int // int` → `int`; any operation with `float` → `float`
- `5 % 3` → always in range `[0, b-1]`
- `a % b == 0` means `a` is divisible by `b`
- Operator precedence: `**` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`

### Common Pitfalls
- `0.1 + 0.1 + 0.1` → `0.30000000000000004` (float precision)
- `"4" == 4` → `False` (different types)
- `4 > "howdy"` → `TypeError`

### Exam Traps
- `bool("")` → `False`; `bool("False")` → `True` (non-empty string!)
- `int / int` always returns `float`: `4 / 2` → `2.0`
- `not` binds tighter than `and` which binds tighter than `or`
- `True` and `False` must be capitalized

### Mini Examples
```python
# Leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Modulo cycling: x % n always gives 0..n-1
hour = (hour + 1) % 24   # wraps around clock
```

---

## 4. Conditionals

### Core Concepts
- `if`, `elif`, `else` control which code executes
- Only one branch of an `if/elif/else` chain executes
- Multiple independent `if` statements all get evaluated
- `match/case` for comparing one value against multiple options

### Syntax / Patterns
```python
# Basic if/elif/else
if temperature > 85:
    print("Beach!")
elif temperature > 55:
    print("Hiking!")
else:
    print("Stay in.")

# Nested if
if am_hungry:
    if is_morning:
        print("Pancakes!")
    else:
        print("Soup!")

# match/case
match traffic_light:
    case "red":
        print("Stop!")
    case "yellow":
        print("Slow.")
    case "green":
        print("Go.")
    case _:                 # default
        print("Unknown.")

# Multiple cases
    case 403 | 404:
        print("Not found/forbidden.")
```

### Key Rules
- `elif` only tests if all previous conditions were `False`
- `else` has no condition — runs if everything above was `False`
- Indentation defines the block; must be consistent
- `case _:` is the default in `match`

### Common Pitfalls
```python
# BUG: All if statements run independently
if exam_score > 90:
    grade = "A"
if exam_score > 80:   # This ALSO runs, overwriting "A"!
    grade = "B"

# FIX: use elif
if exam_score > 90:
    grade = "A"
elif exam_score > 80:
    grade = "B"
```

### Exam Traps
- `if x = 5:` → `SyntaxError` (use `==` for comparison)
- Each `if` in a sequence is independent; `elif` is NOT
- `else` always matches the nearest unmatched `if`

---

## 5. Loops

### Core Concepts
- `for` loop: iterates over each element of a sequence
- `while` loop: repeats while a condition is `True`
- Accumulator pattern: variable initialized outside loop, updated inside
- `enumerate()`: gives both index and value during iteration

### Syntax / Patterns
```python
# for loop
for number in range(1, 101):
    print(number)

for letter in "hello":
    print(letter)

for item in [1, 2, 3]:
    print(item)

# range(stop), range(start, stop), range(start, stop, step)
range(5)         # 0,1,2,3,4
range(1, 6)      # 1,2,3,4,5
range(0, 10, 2)  # 0,2,4,6,8
range(5, 0, -1)  # 5,4,3,2,1

# while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Accumulator patterns
total = 0
for x in nums:
    total += x          # sum

count = 0
for x in nums:
    if x > 0:
        count += 1      # conditional count

largest = nums[0]
for x in nums:
    if x > largest:
        largest = x     # max

# Mapping in place with enumerate
for index, score in enumerate(exam_scores):
    exam_scores[index] = score + 10

# Filter into new list
result = []
for x in nums:
    if x > 0:
        result.append(x)

# Infinite loop (animation)
while True:
    # draw frame
    pd.advance()
```

### Key Rules
- `for` loop variable remains in scope after the loop ends
- `while True:` loops forever unless `return` or `break` exits
- Accumulator must be initialized OUTSIDE the loop
- `range(n)` → n iterations (0 to n-1)

### Common Pitfalls
```python
# BUG: accumulator inside loop resets each iteration
for element in my_tuple:
    counter = 0        # resets every iteration!
    counter += 1

# BUG: mutating a list while iterating over it
```

### Exam Traps
- `for x in range(n)` runs exactly `n` times
- `while` loop with no update to loop variable → infinite loop
- `range(6, 0)` is EMPTY (need step=-1 to go backwards)
- `for element in sequence:` — `element` is a copy, not a reference (for immutable types)

---

## 6. Functions

### Core Concepts
- Function: named block of statements, defined once, called many times
- Parameters: variable names in the definition
- Arguments: actual values passed in the call
- `return` stops execution and provides a value
- Functions without `return` return `None`

### Syntax / Patterns
```python
# Definition
def multiply(a, b):
    product = a * b
    return product

# Calling
result = multiply(3, 7)   # result = 21

# Type annotations (documentation only, not enforced)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Keyword (default) arguments
def divide(a, b, rounding=False):
    result = a / b
    return round(result) if rounding else result

divide(10, 3)             # 3.333...
divide(10, 3, rounding=True)   # 3

# main() pattern
def main():
    print("Hello!")

if __name__ == "__main__":
    main()

# Docstrings
def add(x: int, y: int) -> int:
    """Returns the sum of x and y."""
    return x + y

# ord() and chr()
ord('A')   # 65
chr(65)    # 'A'
ord('A') - ord('A')  # 0  (A=0, B=1, ...)
```

### Key Rules
- Positional args filled left to right by order
- All positional params must come before keyword params in signature
- `return` immediately exits the function
- A function call is an expression with a value (even `None`)
- Printing ≠ returning

### Common Pitfalls
```python
# BUG: using print instead of return
def add(x, y):
    print(x + y)      # prints but returns None!

result = add(3, 4)    # result is None, not 7

# FIX:
def add(x, y):
    return x + y
```

### Exam Traps
- `def f(a, b=0, c):` → `SyntaxError` (keyword args must come last)
- `f(z=0, 3, 4)` → `SyntaxError` (positional args must precede keyword args in call)
- Early `return` exits immediately — code after `return` never runs
- Without `return`, function returns `None`

---

## 7. Sequences: Strings, Ranges, Tuples, Lists

### Core Concepts
- All sequences: ordered, indexable, support `len()` and `in`
- `str`: immutable sequence of characters
- `range`: immutable sequence of integers
- `tuple`: immutable sequence of any types, uses `()`
- `list`: **mutable** sequence of any types, uses `[]`

### Syntax / Patterns
```python
# Indexing (0-based, negative from end)
s = "hello"
s[0]     # 'h'
s[-1]    # 'o' (last character)
s[10]    # IndexError!

# Slicing: s[start:stop:step]  (stop is EXCLUSIVE)
s[1:4]   # 'ell'
s[:3]    # 'hel'  (from beginning)
s[3:]    # 'lo'   (to end)
s[::2]   # 'hlo'  (every other)
s[::-1]  # 'olleh' (reverse)

# Membership
"ell" in "hello"   # True
"x" in "hello"     # False

# String methods
"hello".upper()         # "HELLO"
"HELLO".lower()         # "hello"
"hello world".capitalize()  # "Hello world"
"  hi  ".strip()        # "hi"
"hello".replace("l","r") # "herro"
"hello".find("l")       # 2 (first occurrence, or -1)
"a,b,c".split(",")      # ["a","b","c"]
"hello".split()         # splits on whitespace
"hello".istitle()       # False
",".join(["a","b","c"]) # "a,b,c"
len("hello")            # 5

# String concatenation and repetition
"ha" * 3     # "hahaha"
"hi" + "!"   # "hi!"

# List operations
lst = [1, 2, 3]
lst.append(4)           # [1,2,3,4]
lst.extend([5, 6])      # [1,2,3,4,5,6]
lst.remove(2)           # removes first occurrence of 2
lst.pop()               # removes & returns last element
lst.pop(0)              # removes & returns element at index 0
lst.count(3)            # number of times 3 appears
lst.index(3)            # index of first 3 (ValueError if absent)
sorted(lst)             # returns new sorted list
lst.sort()              # sorts in place
lst[1] = 99             # mutation
new = lst + [7, 8]      # concatenation, creates new list
new = list(range(5))    # [0,1,2,3,4]

# Tuples
t = (1, 2, 3)
t[0]         # 1
t[0] = 9     # TypeError! tuples are immutable
a, b, c = t  # tuple unpacking
```

### Key Rules
- `list` is mutable (`append`, `extend`, index assignment)
- `tuple` is immutable (no item assignment, no `append`)
- `str` is immutable (methods return NEW strings, never modify in-place)
- `range` cannot be concatenated; cannot be printed directly
- Valid indices: `0` to `len(s)-1`; negatives: `-1` is last, `-len(s)` is first

### Common Pitfalls
- `s[len(s)]` → `IndexError` (off-by-one; last valid index is `len(s)-1`)
- `"hello".upper()` does NOT modify `"hello"` — must assign: `s = s.upper()`
- `s[1:4]` has length `4-1 = 3`
- `tuples` need a trailing comma for single-element: `(5,)` not `(5)`

### Exam Traps
- `"art" in "earth"` → `True` (substring check for strings)
- `("H","S") in ("H","S","S")` → `False` (checks element, not subsequence)
- `range(6,0)` → empty! Need `range(6,0,-1)` for descending
- Lists can hold mixed types: `[1, "hello", True]`
- Slicing never raises `IndexError`; out-of-range slices just return what's available

---

## 8. List Comprehensions

### Core Concepts
- Compact syntax for building lists from sequences
- Supports filtering (`if`) and mapping (expression)
- Returns a new list

### Syntax / Patterns
```python
# Basic: copy
[x for x in sequence]

# Map: transform
[x * 2 for x in range(5)]           # [0,2,4,6,8]
[s.upper() for s in names]

# Filter
[x for x in nums if x > 0]          # non-negatives only

# Map + Filter (filter first, then expression applied)
[x**2 for x in range(10) if x % 2 == 0]   # squares of evens

# Constant expression
[0 for _ in range(5)]                # [0,0,0,0,0]

# Set comprehension
{x**2 for x in range(5)}            # {0,1,4,9,16}

# Dict comprehension
{name: len(name) for name in names}
```

### Key Rules
- `[expr for var in seq if cond]` — condition applied to `var`, not `expr`
- Creates a NEW list; original sequence unchanged
- `_` convention for unused loop variable

### Exam Traps
- `[x for x in lst if x > 0]` — filter is on original `x`, not the expression
- Set/dict comprehensions use `{}`, list uses `[]`

---

## 9. Sets & Dictionaries

### Core Concepts
- `set`: unordered collection of **unique** elements, no indexing
- `dict`: unordered collection of unique **key**→value pairs
- Both use `{}` syntax (empty `{}` is a `dict`!)
- Keys/set elements must be **hashable** (no lists, sets, or dicts as keys)

### Syntax / Patterns
```python
# SET
s = {1, 2, 3}
s = set()           # empty set (NOT {})
s = set([1,1,2])    # {1, 2} — deduplicates

s.add(4)
s.remove(4)         # KeyError if missing
s.discard(4)        # safe remove (no error)
len(s)
3 in s              # True

# Set operations
a | b    # union
a & b    # intersection
a - b    # difference (in a but not b)
a ^ b    # symmetric difference (in exactly one)
a <= b   # a is subset of b
a >= b   # a is superset of b

# DICT
d = {"key": "value", "age": 27}
d = dict()          # empty dict

d["age"]            # 27 (KeyError if missing)
d["age"] = 28       # add or update
del d["age"]        # remove (KeyError if missing)
"age" in d          # True (checks keys only)
len(d)

d.keys()            # view of keys
d.values()          # view of values
d.items()           # view of (key, value) tuples

# Iterating
for k in d:             # iterates over keys
for k, v in d.items():  # iterates over key-value pairs

# Dict as counter pattern
counter = {}
for item in items:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

# Dict comprehension
{name: len(name) for name in names}
```

### Key Rules
- Sets are unordered → no indexing, unpredictable iteration order
- Dicts are unordered → iteration order is insertion order (Python 3.7+)
- `{}` → empty dict; `set()` → empty set
- Lists/sets/dicts cannot be dict keys or set elements (not hashable)
- Tuples CAN be dict keys

### Common Pitfalls
- `s.remove(x)` raises `KeyError` if `x` not in set; use `s.discard(x)` to be safe
- `d[missing_key]` raises `KeyError`; check `if key in d` first
- `{} ` is a dict, not a set!

### Exam Traps
- `"key" in d` checks **keys** only, not values
- Membership check in set/dict is O(1); in list is O(n)
- `for k in d:` iterates over keys, not values
- Dicts/sets are faster for membership testing than lists

### Mini Examples
```python
# Remove duplicates while preserving order
unique = list(dict.fromkeys(items))   # or list(set(items)) if order doesn't matter

# Choosing data structures:
# list  → ordered, need index access, can have duplicates
# set   → membership checks, no duplicates needed
# dict  → key-value lookup
# tuple → fixed collection, use as dict key, "final answer"
```

---

## 10. Functional Programming

### Core Concepts
- Functions are first-class objects (can be stored, passed, returned)
- Higher-order functions take functions as arguments
- `lambda`: anonymous single-expression function
- `map`, `filter`, `reduce` from `functools`

### Syntax / Patterns
```python
# Functions as objects
f = len            # f is now the len function
f("hello")         # 5

# map(f, seq) → applies f to each element
list(map(len, ["hi", "hello"]))     # [2, 5]
list(map(str.upper, names))

# filter(f, seq) → keeps elements where f returns True
list(filter(lambda x: x > 0, nums))
list(filter(str.istitle, names))    # str methods work!

# reduce(f, seq[, initial])
from functools import reduce
reduce(lambda a, b: a + b, [1,2,3,4])   # 10
reduce(lambda a, b: a + b, [], 0)       # 0 (initializer)

# lambda syntax
lambda x: x + 1
lambda a, b: a + b
lambda t: t[1]          # get second element of tuple

# min/max with key
min(names, key=len)                         # shortest name
max(records, key=lambda t: t[1])            # highest score
sorted(items, key=lambda x: x[1])          # sort by second element
```

### Key Rules
- `map` and `filter` return lazy objects; wrap with `list()` to materialize
- `lambda` body must be a single expression (no statements, no `return`)
- `filter` requires function that returns bool
- `map` requires function that takes one arg
- `reduce` requires function that takes two args (accumulator, element)

### Common Pitfalls
- `filter(str.istitle, names)` works; `filter(istitle, names)` → `NameError`
- `reduce` on empty sequence without initializer → `TypeError`
- Lambdas reduce readability; prefer `def` for complex logic

### Exam Traps
- `map(f, seq)` → `[f(elem) for elem in seq]`
- `filter(f, seq)` → `[elem for elem in seq if f(elem)]`
- `sorted()` returns new list; `.sort()` sorts in-place and returns `None`

---

## 11. Object-Oriented Programming (OOP)

### Core Concepts
- **Class**: blueprint/template for a new data type
- **Object/Instance**: specific realization of a class
- **Attribute**: variable belonging to an object
- **Method**: function belonging to a class
- `__init__`: constructor/initializer; called when creating an instance
- `self`: reference to the current object instance

### Syntax / Patterns
```python
# dataclass (simple, data-only)
from dataclasses import dataclass

@dataclass
class Movie:
    name: str
    year: int
    price: float

m = Movie("Parasite", 2019, 12.99)
print(m.name)       # "Parasite"
m.price = 9.99      # modify attribute

# Full class with methods
class Square:
    def __init__(self, x, y, size):
        self.x = x          # self.attr declares attribute
        self.y = y
        self.size = size

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        return (2 * self.size) ** 2

    def contains_point(self, px, py) -> bool:
        return (abs(px - self.x) <= self.size and
                abs(py - self.y) <= self.size)

# Creating instances
s = Square(0.5, 0.5, 0.1)
s.move_by(0.1, 0)
print(s.area())
print(s.x)          # access attribute

# Multiple independent instances
s1 = Square(0.1, 0.1, 0.05)
s2 = Square(0.9, 0.9, 0.05)
s1.move_by(0, 0.5)   # only s1 moves
```

### Key Rules
- All methods must have `self` as first parameter
- Access attributes via `self.attr_name` inside class; `obj.attr_name` outside
- `__init__` sets up initial attribute values
- `dataclass` auto-generates `__init__`, `__repr__`, `__eq__`
- Each instance has its own copy of attribute values

### Common Pitfalls
```python
# BUG: forgetting self
def change_color(new_color):     # missing self!
    color = new_color            # local variable, not attribute!

# FIX:
def change_color(self, new_color):
    self.color = new_color

# BUG: forgetting self. prefix
def __init__(self, x):
    self.x = x
    area = x * x    # local var, not self.area!
```

### Exam Traps
- `Movie.price` → `AttributeError` (class has no value; only instances do)
- `obj.method()` passes `obj` as `self` automatically
- `dataclass` attributes defined with type annotation at class level
- Calling `Square(...)` invokes `__init__` automatically

---

## 12. Mutability & References

### Core Concepts
- Variables store **references** (memory addresses), not values directly
- Immutable types: `int`, `float`, `bool`, `str`, `tuple` — operations create new objects
- Mutable types: `list`, `dict`, `set`, class instances — operations modify in-place
- Multiple variables can reference the SAME mutable object

### Syntax / Patterns
```python
# Immutable — reassignment creates new object
s = "hello"
s.upper()       # does nothing to s!
s = s.upper()   # now s is "HELLO"

# Mutable — mutations affect all references
a = [1, 2, 3]
b = a           # b and a point to the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4]!

# Passing mutable to function — original gets modified!
def add_item(lst):
    lst.append(99)

my_list = [1, 2]
add_item(my_list)
print(my_list)  # [1, 2, 99]

# Passing immutable to function — original unchanged
def add_five(n):
    n += 5      # creates new int, doesn't modify caller's variable

x = 10
add_five(x)
print(x)        # still 10
```

### Key Rules
- `b = a` for a list → `b` and `a` are aliases for the same list
- To copy a list: `b = a[:]` or `b = list(a)`
- Immutable types: reassignment changes what the variable points to
- Mutable types: methods like `append` change the object itself

### Exam Traps
- `not_p = p` for a class instance → both reference same object, mutations visible to both
- `m = p.y; m += 1` — `m` is an `int` (immutable), `p.y` unchanged
- Strings: `.replace()`, `.upper()` always return NEW strings

---

## 13. Recursion

### Core Concepts
- Recursive function: calls itself with a smaller/simpler input
- Must have a **base case** (trivially solvable) and **recursive case**
- Each recursive call must move "closer" to the base case
- Call stack: each call gets its own activation frame

### Syntax / Patterns
```python
# Template
def recursive_fn(input):
    if <base_case_condition>:   # simplest case
        return <base_result>
    else:
        return <combine>(recursive_fn(<smaller_input>))

# Multiply without *
def multiply(x, y):
    if x == 1:
        return y
    return y + multiply(x - 1, y)

# Is palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

# Find largest
def find_largest(lst):
    if len(lst) == 0:
        return float('-inf')
    head = lst[0]
    return max(head, find_largest(lst[1:]))

# Linear search (recursive)
def linear_search(lst, target, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return linear_search(lst, target, index + 1)

# Binary search (recursive) — requires sorted list
def binary_search(lst, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return binary_search(lst, target, left, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, right)
```

### Key Rules
- Always identify base case(s) first
- Recursive call must use a "smaller" version of the problem
- `lst[1:]` creates a copy of list without first element (common pattern)
- `float('-inf')` useful as initial "smallest" value

### Common Pitfalls
- Missing base case → infinite recursion → `RecursionError`
- Recursive call doesn't reduce problem → infinite recursion

### Exam Traps
- Tracing: work through call stack carefully, unwinding from deepest call
- `is_palindrome("a")` → `True` (base case: length ≤ 1)
- Binary search only works on **sorted** sequences

---

## 14. Searching & Efficiency

### Core Concepts
- **Linear search**: check each element one-by-one; works on unsorted data; O(n)
- **Binary search**: halve search space each step; requires sorted data; O(log n)
- `in` operator on `list`/`tuple` is O(n); on `set`/`dict` is O(1)

### Syntax / Patterns
```python
# Linear search (iterative)
def linear_search(seq, target):
    for idx, elem in enumerate(seq):
        if elem == target:
            return idx
    return -1

# Binary search (iterative)
def binary_search(seq, target):
    low, high = 0, len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < seq[mid]:
            high = mid - 1
        elif target > seq[mid]:
            low = mid + 1
        else:
            return mid
    return -1

# Built-in: sequence.index(target) — raises ValueError if not found
# str.find(target) — returns -1 if not found

# Timing code
import timeit
# python -m timeit -s "setup_code" "code_to_time"
```

### Key Rules
- Binary search requires sorted input
- `set` membership is ~100x faster than `list` for large collections
- Use `list` when order matters; `set` for fast membership; `dict` for key→value lookup

### Exam Traps
- Binary search on unsorted list → wrong results (no error!)
- Linear search max iterations = `len(sequence)`
- Binary search max iterations ≈ `log₂(len(sequence))`

---

## 15. Nested Data & JSON

### Core Concepts
- Nested structures: dicts containing lists containing dicts (etc.)
- JSON (JavaScript Object Notation): standard web data format, looks like Python dicts/lists
- `json.loads(string)` → parse string to Python dict
- `json.load(file)` → parse file to Python dict
- XML: hierarchical tag-based format; parsed with BeautifulSoup

### Syntax / Patterns
```python
import json

# Parse JSON string
data = json.loads('{"name": "Harry", "age": 27}')
print(data["name"])   # "Harry"

# Parse JSON file
with open("data.json") as f:
    data = json.load(f)

# Chained dict access
temp_unit = data["hourly_units"]["temperature_2m"]

# Nested dict access pattern
lat = data["latitude"]
temps = data["hourly"]["temperature_2m"]
max_temp = max(temps)

# BeautifulSoup XML parsing
from bs4 import BeautifulSoup
tree = BeautifulSoup(open("file.xml"), "xml")
root = tree.data
root.name            # tag name
root.attrs           # dict of attributes

for child in root.find_all(recursive=False):   # direct children
    print(child.name, child.attrs)

for elem in root.find_all("country"):          # all matching descendants
    print(elem.find("rank").string)            # first child with tag "rank"
```

### Key Rules
- Nested access: `data["key1"]["key2"][0]`
- Always study the structure (keys, nesting depth) before writing code
- `find_all(tag)` → list of all matching tags
- `find(tag)` → first matching tag (or None)
- `.string` → text content of a tag; `.attrs` → dict of HTML attributes

### Common Pitfalls
- `data["temperature_2m"]` when the key is nested: need `data["hourly"]["temperature_2m"]`

---

## 16. Testing

### Core Concepts
- Unit testing: test individual functions in isolation
- A test has: input, expected output, actual output, assertion
- `unittest` module built into Python
- Test passes when expected == actual; fails otherwise

### Syntax / Patterns
```python
import unittest
import my_code    # module being tested

class TestMyCode(unittest.TestCase):

    def test_basic_case(self):
        # INPUT
        a, b = 3, 7
        # EXPECTED
        expected = 10
        # ACTUAL
        actual = my_code.add(a, b)
        # ASSERTION
        self.assertEqual(expected, actual)

    def test_negative(self):
        self.assertEqual(-1, my_code.add(-3, 2))

    def test_true(self):
        self.assertTrue(my_code.is_palindrome("racecar"))

    def test_none(self):
        self.assertIsNone(my_code.no_return())

if __name__ == "__main__":
    unittest.main()

# Run all tests:  python -m unittest
# Run one file:   python test_file.py
```

### Assertions
| Method | Passes when |
|--------|-------------|
| `assertEqual(exp, act)` | `exp == act` |
| `assertTrue(result)` | `result is True` |
| `assertFalse(result)` | `result is False` |
| `assertIsNone(result)` | `result is None` |
| `assertNotEqual(a, b)` | `a != b` |

### Key Rules
- Test class must extend `unittest.TestCase`
- Test method names must start with `test`
- All test methods take `self` as only parameter
- `.` = pass, `F` = fail, `E` = error (crash) in output
- One failing test doesn't affect others

### Common Pitfalls
- Testing a function that prints instead of returns → will always assert `None`
- `assertEqual(expected, actual)` — order matters for error messages

### Exam Traps
- Argument order: `expected` first, `actual` second (convention)
- Test functions don't return anything
- `if __name__ == "__main__":` block needed to run file directly

---

## 17. Files & I/O

### Syntax / Patterns
```python
# Reading a file
f = open("filename.txt", "r")
line = f.readline()          # one line at a time (includes \n)
line = f.readline().strip()  # remove \n and whitespace
all_lines = f.readlines()    # list of all lines
for line in f:               # iterate line by line
    line = line.strip()
f.close()

# Writing a file
f = open("output.txt", "w")
f.write("Hello!\n")
f.close()

# Context manager (preferred)
with open("file.txt", "r") as f:
    content = f.read()
# file automatically closed

# Parsing CSV-like data
for line in f:
    parts = line.strip().split(",")
    name, score = parts[0], int(parts[1])

# Command line args
import sys
filename = sys.argv[1]   # first arg after script name
```

### Key Rules
- `readline()` includes the newline character `\n`; use `.strip()` to remove
- `readlines()` returns a list where each element is one line (with `\n`)
- Always `close()` files, or use `with` statement
- `"r"` = read mode, `"w"` = write mode (overwrites), `"a"` = append mode

---

## 18. Pandas & DataFrames

### Core Concepts
- DataFrame: 2D table (like a spreadsheet) made of Series (columns)
- Operations return new DataFrames; original unchanged unless reassigned
- Missing values represented as `NaN`

### Syntax / Patterns
```python
import pandas as pd

# Load data
df = pd.read_csv("file.csv", sep=",")
df = pd.read_csv("file.csv", sep=";", index_col="Territory")

# Inspect
df.head(5)            # first 5 rows
df.tail(5)            # last 5 rows
df.columns            # column names
df.describe()         # summary statistics
df.isna().sum()       # count NaN per column

# Select columns
df["Bands"]                       # single column → Series
df[["Bands", "Happiness"]]        # multiple columns → DataFrame
df.Bands                          # dot syntax (if valid identifier)

# Select rows
df[10:20]                          # slice by row number
df.iloc[13]                        # row by integer index

# Filter rows (boolean indexing)
df[df["Bands"] > 50]
df[(df["Bands"] > 50) & (df["Happiness"] < 4.0)]   # AND
df[(df["Bands"] < 10) | (df["Population"] < 5e6)]  # OR

# Modify / create columns
df["Population"] = df["Population"] / 1000000       # scale column
df["BPC"] = df["Bands"] / df["Population"]          # new column
df = df.drop(columns=["BPC"])                       # remove column
df = df.rename(columns={"Bands": "NumBands"})       # rename

# Handle NaN
df.dropna()             # drop rows with any NaN
df.fillna(0)            # replace NaN with 0

# String operations on columns
df["Name"].str.upper()
df["Name"].str.len()
df["Name"].str.strip()
df["Name"].str.replace(" ", "_")
df["Name"].str.contains("pattern")  # boolean series
df["Name"].str.split(",")
df["Name"].str.get(0)               # first element after split

# Set index
df = df.set_index("Territory")

# Plotting
df.plot(kind="hist", y="Bands")
df.plot(kind="scatter", x="BPC", y="Happiness", title="My Plot")
```

### Key Rules
- Operations like `rename`, `drop`, `fillna` return NEW DataFrames; must reassign
- `&` and `|` for combining boolean Series (not `and`/`or`)
- Wrap filter conditions in parentheses when combining
- `df["col"] = expr` MODIFIES the DataFrame in-place

### Common Pitfalls
- `df.rename(...)` without `df = ` → change is lost
- Using `and`/`or` instead of `&`/`|` → `ValueError`

---

## 19. Web Scraping & APIs

### Syntax / Patterns
```python
# requests library
import requests

# GET request
response = requests.get("https://example.com/api")
print(response.status_code)     # 200 = OK
data = response.json()          # parse JSON response
html = response.text            # raw HTML string

# GET with headers (API key)
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)

# POST request with body
body = {"model": "gpt-4", "messages": [...]}
response = requests.post(url, headers=headers, json=body)

# BeautifulSoup HTML scraping
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_string, "html.parser")

soup.title                          # first <title> tag
soup.title.string                   # text inside tag
soup.title.name                     # "title"
soup.p["class"]                     # attribute value
soup.find("h3", id="my-id")        # first matching tag
soup.find_all("a")                  # all <a> tags (list)
soup.find_all("p", class_="story") # filter by class (note: class_)
tag.parent.name                     # parent tag's name
tag.next_sibling.next_sibling       # navigate siblings
tag.text.strip()                    # text content, stripped

# Build DataFrame from scraping
rows = []
for item in soup.find_all("ul", class_="row"):
    rows.append({"title": ..., "artist": ...})
df = pd.DataFrame(rows)
df.to_csv("output.csv", index=False)
```

### Key Rules
- HTTP verbs: GET (read), POST (create), PUT (update), DELETE (delete)
- Response codes: 200=OK, 404=Not Found, 403=Forbidden, 500=Server Error
- `class_=` (with underscore) in BeautifulSoup because `class` is a Python keyword
- `find()` returns first match or `None`; `find_all()` returns list

---

## 20. Animation & Interactivity (PennDraw)

### Syntax / Patterns
```python
import penndraw as pd

# Animation loop structure
pd.set_canvas_size(500, 500)
x = 0.5   # SETUP: initialize state variables

while True:
    pd.clear()                          # 1. clear screen
    pd.filled_square(x, 0.5, 0.1)      # 2. draw frame
    x += 0.01                           # 3. update state
    if x - 0.1 > 1.0:
        x = -0.1                        # reset/wrap
    pd.advance()                        # 4. advance frame (REQUIRED)

# Mouse input
pd.mouse_x()          # cursor x position
pd.mouse_y()          # cursor y position
pd.mouse_pressed()    # True if mouse button held

# Keyboard input
if pd.has_next_key_typed():
    key = pd.next_key_typed()   # single character string
    if key == "x":
        ...
    if "a" <= key <= "z":       # lowercase letter check
        ...
    if "0" <= key <= "9":       # digit check
        ...
```

### Key Rules
- `pd.advance()` at end of loop is **required**; nothing shows without it
- `pd.clear()` clears all previous shapes; omit to draw trails
- Always check `has_next_key_typed()` before calling `next_key_typed()`
- `while True:` → runs forever; only stops when program killed

---

## 21. Type Annotations & Style

### Syntax / Patterns
```python
# Function with type annotations
def repeat(text: str, times: int) -> str:
    return text * times

# List, dict, set annotations
def process(items: list[int]) -> dict[str, int]:
    ...

def find(data: set[str], key: str) -> bool:
    ...

# Docstring format
def add(x: int, y: int) -> int:
    """Returns the sum of x and y.

    Arguments:
    x -- first operand
    y -- second operand
    """
    return x + y
```

### Key Rules
- Type annotations are **not enforced** by Python — documentation only
- `list[int]` means a list of ints
- `dict[str, int]` means keys are str, values are int
- Return type annotation uses `->` before the colon

---

## 22. Scope & Variable Lifetime

### Key Rules
- Variables declared inside a function are **local** to that function
- Global variables (outside all functions) can be read inside functions
- Parameters are local to the function they're defined in
- Variables created in a loop body are accessible after the loop (in Python)

### Mini Examples
```python
def foo():
    x = 10      # local to foo

foo()
print(x)        # NameError! x doesn't exist here

# Loop variable persists
for i in range(5):
    pass
print(i)        # 4 — still accessible
```

---

## Quick Reference: Common Patterns

### Reading a file into a dict
```python
d = {}
with open("data.csv") as f:
    for line in f:
        k, v = line.strip().split(",")
        d[k] = int(v)
```

### Counting occurrences
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
# or: use collections.Counter
```

### Deduplication
```python
unique = list(set(items))           # unordered
unique_ordered = list(dict.fromkeys(items))  # preserves order
```

### Sort by custom key
```python
sorted(records, key=lambda r: r[1])          # by second element
sorted(names, key=len)                       # by length
sorted(names, key=str.lower)                 # case-insensitive
```

### String → number conversions
```python
ord('A')        # 65
chr(65)         # 'A'
ord(c) - ord('A')   # letter → 0-indexed number
chr(n + ord('A'))   # number → letter
```

### Binary search setup
```python
result = binary_search(lst, target, 0, len(lst) - 1)
```

### Recursive helper pattern
```python
def search(lst, target):
    return _search_helper(lst, target, 0, len(lst) - 1)
```

---

## Common Bugs & Fixes

| Bug | Symptom | Fix |
|-----|---------|-----|
| `=` instead of `==` in condition | `SyntaxError` | Use `==` |
| Using `and`/`or` in pandas filter | `ValueError` | Use `&`/`|` |
| `dict["key"]` when key absent | `KeyError` | Check `if key in d` first |
| `set.remove(x)` when absent | `KeyError` | Use `.discard(x)` |
| `input()` not converted | Wrong type comparison | `int(input(...))` |
| Accumulator inside loop | Resets each iteration | Move init outside loop |
| `append` returns `None` | Variable is `None` | `lst.append(x)`, don't assign |
| `str.upper()` not saved | String unchanged | `s = s.upper()` |
| Missing `self` in method | `TypeError` on call | Add `self` as first param |
| Forgetting `self.` prefix | `NameError` | Use `self.attr_name` |
| `{}` instead of `set()` | Creates empty dict | Use `set()` for empty set |
| `return` vs `print` | Function returns `None` | Use `return value` |
| Forgetting `pd.advance()` | Nothing shows on screen | Add at end of `while True` loop |
| `code after return` | Never executes | `return` exits immediately |
| Calling `defaultdict[key]` when absent | Inserts default, no error | Intended behavior — use `dict.get()` if you don't want this |

---

## 23. PennDraw API Reference

### Syntax / Patterns
```python
import penndraw as pd

# Canvas setup
pd.set_canvas_size(width_px, height_px)   # default 512×512
pd.clear()                                 # clear to white
pd.clear(pd.BLUE)                          # clear to color
pd.clear(r, g, b)                          # clear to RGB color

# Pen settings
pd.set_pen_color(pd.RED)                   # named color
pd.set_pen_color(r, g, b)                  # RGB 0-255
pd.set_pen_radius(0.005)                   # thickness (default 0.002)

# Shapes (filled)
pd.filled_circle(x, y, radius)
pd.filled_square(x, y, half_side)
pd.filled_rectangle(x, y, half_w, half_h)
pd.filled_polygon(x1,y1, x2,y2, x3,y3)   # any number of x,y pairs

# Shapes (outline only)
pd.circle(x, y, radius)
pd.square(x, y, half_side)
pd.rectangle(x, y, half_w, half_h)
pd.polygon(x1,y1, x2,y2, x3,y3)

# Points and lines
pd.point(x, y)
pd.line(x1, y1, x2, y2)

# Text
pd.text(x, y, "message")

# Run / advance
pd.run()             # display static drawing — call once at end
pd.advance()         # push frame in animation loop — required each iteration

# Named colors: pd.BLACK, pd.WHITE, pd.RED, pd.GREEN, pd.BLUE,
#               pd.YELLOW, pd.MAGENTA, pd.CYAN, pd.ORANGE, pd.GRAY
```

### Key Rules
- Canvas coordinates: `(0,0)` = bottom-left, `(1,1)` = top-right
- Drawing order matters: later shapes paint over earlier ones
- `pd.run()` for static drawings; `pd.advance()` inside `while True:` for animation
- `set_pen_color` stays in effect until changed again

---

## 24. Advanced: `defaultdict` & `collections`

### Core Concepts
- `defaultdict(f)`: like a dict, but auto-inserts `f()` as the default for missing keys
- Avoids `KeyError` when first accessing a new key
- Common factories: `int` (→ 0), `list` (→ []), `set` (→ set()), `lambda: value`

### Syntax / Patterns
```python
from collections import defaultdict

# defaultdict(int) → default value is 0
counter = defaultdict(int)
counter["apples"] += 1      # no KeyError even though "apples" didn't exist
counter["bananas"] += 3
print(counter["cherries"])  # 0 (auto-inserted)

# defaultdict(list) → default value is []
groups = defaultdict(list)
groups["A"].append("Alice")
groups["B"].append("Bob")

# defaultdict(lambda: 11) → default value is 11
targets = defaultdict(lambda: 11)
targets["first"] = 12
print(targets["second"])    # 11 (default)

# Rewrite counter pattern with defaultdict
def get_counts(items):
    counts = defaultdict(int)
    for item in items:
        counts[item] += 1
    return dict(counts)   # convert back to regular dict if needed
```

### Key Rules
- `defaultdict` inherits all dict operations
- Accessing a missing key **creates** it with the default value (side effect!)
- Use `dict.get(key, default)` if you want a default WITHOUT inserting

### Exam Traps
- `d[key]` on a `defaultdict` with missing key inserts it — `key in d` becomes `True` after!
- `defaultdict(int)` → `0`; `defaultdict(list)` → `[]`; `defaultdict(set)` → `set()`

---

## 25. Cosine Similarity & Recommendation

### Core Concepts
- **Cosine similarity**: measure of similarity between two vectors (range −1 to 1)
  - `1.0` = identical direction, `0` = perpendicular, `-1` = opposite
- Represent user preferences as `dict[genre, rating]` (sparse vector)
- Missing genres assumed to have rating `0`

### Syntax / Patterns
```python
import math

# Dot product of two sparse vectors (dicts)
def dot(a: dict, b: dict) -> float:
    total = 0.0
    for key in a:
        if key in b:
            total += a[key] * b[key]
    return total

# Magnitude of a sparse vector
def magnitude(a: dict) -> float:
    return math.sqrt(sum(v * v for v in a.values()))

# Cosine similarity
def cosine_similarity(a: dict, b: dict) -> float:
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot(a, b) / (mag_a * mag_b)

# Example
a = {"Comedy": 4.0, "Action": 4.0}
b = {"Action": 5.0, "Comedy": 5.0}
print(cosine_similarity(a, b))   # close to 1.0 — very similar
```

### Key Rules
- Only shared keys contribute to the dot product
- Missing keys in a dict-vector are treated as `0`
- Result is between `0` and `1` when all ratings are non-negative

---

## 26. Recursion: Advanced Patterns

### Helper Function Pattern
Used when recursion needs extra state (e.g., index, accumulator) not in the public interface:

```python
# Public interface — clean signature
def binary_search(lst, target):
    return _binary_search_helper(lst, target, 0, len(lst) - 1)

# Internal helper — carries extra state
def _binary_search_helper(lst, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return _binary_search_helper(lst, target, lo, mid - 1)
    else:
        return _binary_search_helper(lst, target, mid + 1, hi)

# Factorial
def fact(n: int) -> int:
    if n <= 1:
        return 1
    return n * fact(n - 1)

# Sum of digits
def digit_sum(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

# Remove all spaces recursively
def remove_blanks(s: str) -> str:
    if s == "":
        return ""
    if s[0] == " ":
        return remove_blanks(s[1:])
    return s[0] + remove_blanks(s[1:])

# Count steps to reach 1 via integer division
def foo(n):
    if n <= 1:
        return 0
    return 1 + foo(n // 2)
# foo(16) → 4  (16→8→4→2→1)
```

### Mutual Recursion
```python
def cat(x):
    if x > 10:
        return x
    return dog(x * 2)

def dog(y):
    if y > 10:
        return y
    return cat(y * 2)
# cat(2) → dog(4) → cat(8) → dog(16) → 16
```

### Exam Traps
- `return answer; answer += 10` — the second line is DEAD CODE (never reached)
- Every recursive function needs a base case or it will cause `RecursionError`
- `lst[1:]` creates a COPY of the list without element 0; each recursive call gets its own copy

---

## 27. Testing Objects

### Core Concepts
- The "input" to a test for an object is **setting up the object** and calling methods on it
- Test each method and state change independently
- Multiple setup steps before the assertion are normal

### Syntax / Patterns
```python
class TestAccounts(unittest.TestCase):

    # Test initial state
    def test_new_account_checking_zero(self):
        acct = Accounts(100)        # setup: create object
        expected = 0
        actual = acct.checking      # read attribute
        self.assertEqual(expected, actual)

    # Test after calling a method
    def test_small_deposit_goes_to_checking(self):
        acct = Accounts(100)
        acct.deposit(50)            # call method to change state
        self.assertEqual(50, acct.checking)
        self.assertEqual(0, acct.savings)

    # Test complex interaction
    def test_large_deposit_fills_checking_then_savings(self):
        acct = Accounts(100)
        acct.deposit(500)
        self.assertEqual(100, acct.checking)   # threshold filled
        self.assertEqual(400, acct.savings)    # remainder in savings
```

### Key Rules
- Always create a fresh object in each test (don't share state between tests)
- Test one behavior per test method
- Access attributes directly for assertion: `acct.checking`, not `print(acct)`

---

## 28. While Loops with Terminating Conditions

### Core Concepts
- `while True:` loops forever — only use for animations
- `while <expr>:` loops only as long as `expr` is `True`
- Useful for: waiting for a condition, counting down, game loops

### Syntax / Patterns
```python
# Loop until condition is met
count = 0
while count < 10:
    count += 2
    print("*")
print(count)   # runs AFTER loop ends

# Animation that stops (rivalry.py pattern)
import penndraw as pd
still_running = True
# SETUP
while still_running:
    pd.clear()
    # draw frame
    # update state
    if <end_condition>:
        still_running = False
    pd.advance()
# FINALE (runs after loop ends)
pd.clear(pd.GREEN)
pd.text(0.5, 0.5, "Game Over!")
pd.run()

# Guessing game example
letter = "s"
still_guessing = True
while still_guessing:
    if pd.has_next_key_typed():
        guess = pd.next_key_typed()
        if guess == letter:
            still_guessing = False
        else:
            pd.clear()
            pd.text(0.5, 0.5, f"Not {guess}, try again!")
    pd.advance()
pd.clear(pd.GREEN)
pd.text(0.5, 0.5, "You got it!")
pd.run()
```

### Key Rules
- Code **after** the `while` loop runs only once the loop condition is `False`
- `while not button_released:` — natural English-like condition
- `pd.run()` after the loop is needed to show the finale screen

### Exam Traps
- `while count < 10: count += 2` → loop runs 5 times (count = 0,2,4,6,8), exits at 10
- Code inside loop body runs **before** condition is re-checked
- `still_guessing = False` exits the loop **at the end of that iteration**, not immediately
