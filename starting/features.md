Oh yeah — that **list comprehension trick** is one of Python’s coolest features 😎

Let’s go over some more *neat, practical tricks* and patterns you can do with **lists** and **dictionaries** using comprehensions and other concise techniques.

---

## 🧩 LIST COMPREHENSIONS

### 1. Basic Filtering and Transformation

```python
nums = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in nums if n % 2 == 0]
print(squares)   # [4, 16, 36]
```

➡️ Builds a list of squares, but only for even numbers.

---

### 2. Nested Loops in One Line

```python
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs)
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

➡️ You can nest loops inside comprehensions.

---

### 3. Flattening a Nested List

```python
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8]
```

➡️ This is a neat way to “unpack” lists within lists.

---

### 4. List Comprehension + Function (or Lambda)

```python
words = ["hi", "Python", "rocks"]
lengths = list(map(lambda w: len(w), words))
# Same as:
lengths2 = [len(w) for w in words]
```

➡️ Both give `[2, 6, 5]`.

---

## 🧠 DICTIONARY COMPREHENSIONS

Just like list comprehensions, but with key–value pairs.

### 1. Basic Example

```python
nums = [1, 2, 3, 4]
squares = {n: n**2 for n in nums}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16}
```

---

### 2. Filtering Dictionary Items

```python
grades = {'Alice': 85, 'Bob': 72, 'Chad': 95, 'Dana': 60}
passed = {name: grade for name, grade in grades.items() if grade >= 70}
print(passed)
# {'Alice': 85, 'Bob': 72, 'Chad': 95}
```

---

### 3. Swapping Keys and Values

```python
morse = {'A': '.-', 'B': '-...'}
inverse = {v: k for k, v in morse.items()}
print(inverse)
# {'.-': 'A', '-...': 'B'}
```

➡️ Useful for decoding Morse back into letters!

---

### 4. Combining Lists into a Dictionary

```python
keys = ["name", "age", "color"]
values = ["Alice", 30, "blue"]
person = {k: v for k, v in zip(keys, values)}
print(person)
# {'name': 'Alice', 'age': 30, 'color': 'blue'}
```

---

## 🧩 BONUS: SET & GENERATOR COMPREHENSIONS

### Sets

```python
nums = [1, 2, 2, 3, 3, 4]
unique_squares = {n**2 for n in nums}
print(unique_squares)  # {16, 1, 4, 9}
```

### Generators (for big data / memory saving)

```python
gen = (n**2 for n in range(1000000))
# Doesn’t build the list in memory – you iterate instead
for val in gen:
    ...
```

---

Would you like me to show how to use **a list comprehension and a dictionary comprehension together** in one short, real example (like automatically encoding Morse code)?
