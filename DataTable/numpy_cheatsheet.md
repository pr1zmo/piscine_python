# 🧮 NumPy Cheat Sheet — Most Commonly Used Functions

> A quick reference for working with NumPy arrays in Python.
> Import convention:
>
> ```python
> import numpy as np
> ```

---

## 📦 Array Creation

| Function                             | Description                                  | Example                         |
| ------------------------------------ | -------------------------------------------- | ------------------------------- |
| `np.array(list)`                     | Create an array from a list or tuple         | `np.array([1, 2, 3])`           |
| `np.zeros(shape)`                    | Create an array of zeros                     | `np.zeros((3,3))`               |
| `np.ones(shape)`                     | Create an array of ones                      | `np.ones((2,4))`                |
| `np.full(shape, value)`              | Create a constant array                      | `np.full((2,2), 7)`             |
| `np.eye(n)`                          | Create an identity matrix                    | `np.eye(3)`                     |
| `np.arange(start, stop, step)`       | Create array with evenly spaced values       | `np.arange(0,10,2)`             |
| `np.linspace(start, stop, num)`      | Create array with `num` evenly spaced values | `np.linspace(0,1,5)`            |
| `np.random.rand(shape)`              | Random values in `[0, 1)`                    | `np.random.rand(2,3)`           |
| `np.random.randn(shape)`             | Random values from normal distribution       | `np.random.randn(3,3)`          |
| `np.random.randint(low, high, size)` | Random integers                              | `np.random.randint(0,10,(2,3))` |

---

## 🔢 Array Inspection

| Function       | Description              | Example        |
| -------------- | ------------------------ | -------------- |
| `arr.shape`    | Shape (rows, cols)       | `arr.shape`    |
| `arr.ndim`     | Number of dimensions     | `arr.ndim`     |
| `arr.size`     | Total number of elements | `arr.size`     |
| `arr.dtype`    | Data type                | `arr.dtype`    |
| `arr.itemsize` | Bytes per element        | `arr.itemsize` |

---

## 🔁 Array Manipulation

| Function                        | Description        | Example                         |
| ------------------------------- | ------------------ | ------------------------------- |
| `np.reshape(arr, newshape)`     | Change shape       | `np.reshape(arr, (2,3))`        |
| `arr.flatten()`                 | Flatten to 1D      | `arr.flatten()`                 |
| `np.concatenate((a,b), axis=0)` | Combine arrays     | `np.concatenate((a,b), axis=1)` |
| `np.vstack((a,b))`              | Stack vertically   | `np.vstack((a,b))`              |
| `np.hstack((a,b))`              | Stack horizontally | `np.hstack((a,b))`              |
| `np.split(arr, sections)`       | Split into parts   | `np.split(arr, 3)`              |
| `arr.T`                         | Transpose          | `arr.T`                         |

---

## 🎯 Indexing & Slicing

| Function       | Description            | Example        |
| -------------- | ---------------------- | -------------- |
| `arr[i]`       | Access element         | `arr[0]`       |
| `arr[i, j]`    | Access row & column    | `arr[1,2]`     |
| `arr[:, 0]`    | All rows, first column | `arr[:,0]`     |
| `arr[1:3]`     | Slice rows             | `arr[1:3]`     |
| `arr[arr > 5]` | Boolean indexing       | `arr[arr > 5]` |

---

## ➕ Arithmetic Operations

| Function           | Description                | Example            |
| ------------------ | -------------------------- | ------------------ |
| `arr1 + arr2`      | Elementwise addition       | `a + b`            |
| `arr1 - arr2`      | Elementwise subtraction    | `a - b`            |
| `arr1 * arr2`      | Elementwise multiplication | `a * b`            |
| `arr1 / arr2`      | Elementwise division       | `a / b`            |
| `np.add(a,b)`      | Addition                   | `np.add(a,b)`      |
| `np.multiply(a,b)` | Multiplication             | `np.multiply(a,b)` |
| `np.dot(a,b)`      | Matrix multiplication      | `np.dot(a,b)`      |
| `np.sqrt(arr)`     | Square root                | `np.sqrt(a)`       |
| `np.power(a, n)`   | Power                      | `np.power(a, 2)`   |

---

## 📈 Statistics & Math

| Function         | Description         | Example        |
| ---------------- | ------------------- | -------------- |
| `np.mean(arr)`   | Mean                | `np.mean(a)`   |
| `np.median(arr)` | Median              | `np.median(a)` |
| `np.std(arr)`    | Standard deviation  | `np.std(a)`    |
| `np.var(arr)`    | Variance            | `np.var(a)`    |
| `np.min(arr)`    | Minimum             | `np.min(a)`    |
| `np.max(arr)`    | Maximum             | `np.max(a)`    |
| `np.argmin(arr)` | Index of min        | `np.argmin(a)` |
| `np.argmax(arr)` | Index of max        | `np.argmax(a)` |
| `np.sum(arr)`    | Sum                 | `np.sum(a)`    |
| `np.prod(arr)`   | Product of elements | `np.prod(a)`   |

---

## 🧮 Linear Algebra

| Function            | Description                | Example             |
| ------------------- | -------------------------- | ------------------- |
| `np.dot(a,b)`       | Dot product                | `np.dot(a,b)`       |
| `np.matmul(a,b)`    | Matrix multiplication      | `np.matmul(a,b)`    |
| `np.linalg.inv(a)`  | Inverse                    | `np.linalg.inv(a)`  |
| `np.linalg.det(a)`  | Determinant                | `np.linalg.det(a)`  |
| `np.linalg.eig(a)`  | Eigenvalues & eigenvectors | `np.linalg.eig(a)`  |
| `np.linalg.norm(a)` | Vector/matrix norm         | `np.linalg.norm(a)` |

---

## 🔄 Useful Utilities

| Function                    | Description        | Example                 |
| --------------------------- | ------------------ | ----------------------- |
| `np.unique(arr)`            | Unique elements    | `np.unique(a)`          |
| `np.sort(arr)`              | Sort array         | `np.sort(a)`            |
| `np.where(condition, x, y)` | Conditional select | `np.where(a > 0, 1, 0)` |
| `np.isnan(arr)`             | Detect NaN         | `np.isnan(a)`           |
| `np.any(condition)`         | If any True        | `np.any(a > 0)`         |
| `np.all(condition)`         | If all True        | `np.all(a > 0)`         |
| `np.clip(arr, min, max)`    | Limit values       | `np.clip(a, 0, 1)`      |

---

## 🧰 File I/O

| Function                    | Description          | Example                     |
| --------------------------- | -------------------- | --------------------------- |
| `np.save(filename, arr)`    | Save array to `.npy` | `np.save('data.npy', a)`    |
| `np.load(filename)`         | Load `.npy` file     | `np.load('data.npy')`       |
| `np.savetxt(filename, arr)` | Save to text         | `np.savetxt('data.txt', a)` |
| `np.loadtxt(filename)`      | Load from text       | `np.loadtxt('data.txt')`    |

---

## ⚡ Tips

* Always prefer `np.array` over lists for math operations — faster and vectorized.
* Broadcasting rules let you operate on arrays of different shapes (e.g., `(3,1)` and `(1,3)`).
* Use `np.set_printoptions(precision=3)` for cleaner printed output.

---