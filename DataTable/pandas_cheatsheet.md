# 🐼 Pandas Cheat Sheet — Most Commonly Used Functions

> Quick reference for working with **Pandas** DataFrames and Series.
> Import convention:
>
> ```python
> import pandas as pd
> ```

---

## 📦 Data Creation

| Function                       | Description            | Example                                  |
| ------------------------------ | ---------------------- | ---------------------------------------- |
| `pd.Series(data)`              | Create a Series        | `pd.Series([1, 2, 3])`                   |
| `pd.DataFrame(data)`           | Create a DataFrame     | `pd.DataFrame({'A': [1,2], 'B': [3,4]})` |
| `pd.read_csv(path)`            | Read CSV file          | `pd.read_csv('data.csv')`                |
| `pd.read_excel(path)`          | Read Excel file        | `pd.read_excel('data.xlsx')`             |
| `pd.read_json(path)`           | Read JSON file         | `pd.read_json('data.json')`              |
| `pd.DataFrame.from_dict(dict)` | Create from dictionary | `pd.DataFrame.from_dict(my_dict)`        |

---

## 📊 Data Inspection

| Function        | Description   | Example         |
| --------------- | ------------- | --------------- |
| `df.head(n)`    | First n rows  | `df.head(5)`    |
| `df.tail(n)`    | Last n rows   | `df.tail(3)`    |
| `df.shape`      | Rows, columns | `df.shape`      |
| `df.info()`     | Column info   | `df.info()`     |
| `df.describe()` | Summary stats | `df.describe()` |
| `df.dtypes`     | Data types    | `df.dtypes`     |
| `df.columns`    | Column names  | `df.columns`    |
| `df.index`      | Row index     | `df.index`      |

---

## 🎯 Selecting & Indexing

| Function              | Description                | Example               |
| --------------------- | -------------------------- | --------------------- |
| `df['col']`           | Select column              | `df['A']`             |
| `df[['col1','col2']]` | Select multiple columns    | `df[['A','B']]`       |
| `df.loc[row, col]`    | Label-based selection      | `df.loc[0, 'A']`      |
| `df.iloc[row, col]`   | Integer position selection | `df.iloc[0, 1]`       |
| `df.at[row, col]`     | Fast scalar access (label) | `df.at[0, 'A']`       |
| `df.iat[row, col]`    | Fast scalar access (int)   | `df.iat[0, 1]`        |
| `df.loc[df['A'] > 5]` | Conditional selection      | `df.loc[df['A'] > 5]` |

---

## 🔄 Data Manipulation

| Function                | Description         | Example                           |
| ----------------------- | ------------------- | --------------------------------- |
| `df.sort_values(by)`    | Sort by column      | `df.sort_values('A')`             |
| `df.sort_index()`       | Sort by index       | `df.sort_index()`                 |
| `df.rename(columns={})` | Rename columns      | `df.rename(columns={'A':'col1'})` |
| `df.drop(columns=[])`   | Drop columns        | `df.drop(columns=['B'])`          |
| `df.dropna()`           | Remove missing rows | `df.dropna()`                     |
| `df.fillna(value)`      | Fill missing values | `df.fillna(0)`                    |
| `df.replace(old, new)`  | Replace values      | `df.replace('?', np.nan)`         |
| `df.astype(dtype)`      | Change type         | `df['A'].astype(float)`           |
| `df.apply(func)`        | Apply function      | `df['A'].apply(np.sqrt)`          |

---

## ➕ Combining Data

| Function                                 | Description                            | Example                                       |
| ---------------------------------------- | -------------------------------------- | --------------------------------------------- |
| `pd.concat([df1, df2])`                  | Concatenate vertically                 | `pd.concat([df1, df2])`                       |
| `pd.merge(df1, df2, on='col')`           | Merge (SQL-style join)                 | `pd.merge(df1, df2, on='id')`                 |
| `df.join(df2)`                           | Join on index                          | `df1.join(df2)`                               |
| `df.append(row_dict, ignore_index=True)` | Add row (deprecated → use `pd.concat`) | `pd.concat([df, new_row], ignore_index=True)` |

---

## 📈 Statistics & Math

| Function      | Description        | Example            |
| ------------- | ------------------ | ------------------ |
| `df.mean()`   | Mean               | `df['A'].mean()`   |
| `df.median()` | Median             | `df['A'].median()` |
| `df.std()`    | Standard deviation | `df['A'].std()`    |
| `df.min()`    | Minimum            | `df.min()`         |
| `df.max()`    | Maximum            | `df.max()`         |
| `df.sum()`    | Sum                | `df.sum()`         |
| `df.cumsum()` | Cumulative sum     | `df.cumsum()`      |
| `df.count()`  | Count non-NaN      | `df.count()`       |
| `df.corr()`   | Correlation matrix | `df.corr()`        |

---

## 🧮 Grouping & Aggregation

| Function                                        | Description           | Example                                           |
| ----------------------------------------------- | --------------------- | ------------------------------------------------- |
| `df.groupby('col')`                             | Group by column       | `df.groupby('A')`                                 |
| `df.groupby('col').mean()`                      | Mean per group        | `df.groupby('A').mean()`                          |
| `df.groupby('col').agg({'B': ['mean', 'max']})` | Multiple aggregations | `df.groupby('A').agg({'B': ['mean','max']})`      |
| `df.pivot_table(values, index, columns)`        | Pivot table           | `df.pivot_table('value', index='A', columns='B')` |

---

## 🧹 Handling Missing Data

| Function           | Description                | Example            |
| ------------------ | -------------------------- | ------------------ |
| `df.isna()`        | Boolean mask for NaN       | `df.isna()`        |
| `df.notna()`       | Opposite of `isna()`       | `df.notna()`       |
| `df.dropna()`      | Drop missing rows          | `df.dropna()`      |
| `df.fillna(value)` | Fill missing values        | `df.fillna(0)`     |
| `df.interpolate()` | Interpolate missing values | `df.interpolate()` |

---

## 📅 Working with Dates

| Function                   | Description         | Example                              |
| -------------------------- | ------------------- | ------------------------------------ |
| `pd.to_datetime(series)`   | Convert to datetime | `pd.to_datetime(df['date'])`         |
| `df['date'].dt.year`       | Extract year        | `df['date'].dt.year`                 |
| `df['date'].dt.month`      | Extract month       | `df['date'].dt.month`                |
| `df['date'].dt.day_name()` | Day of week         | `df['date'].dt.day_name()`           |
| `df.set_index('date')`     | Use date as index   | `df.set_index('date', inplace=True)` |
| `df.resample('M').mean()`  | Resample by month   | `df.resample('M').mean()`            |

---

## 🔍 Filtering & Querying

| Function                             | Description          | Example                              |
| ------------------------------------ | -------------------- | ------------------------------------ |
| `df.query('A > 5 & B < 10')`         | Query with condition | `df.query('age > 30')`               |
| `df[df['A'] > 5]`                    | Boolean filter       | `df[df['A'] > 5]`                    |
| `df[(df['A'] > 5) & (df['B'] < 10)]` | Multiple conditions  | `df[(df['A'] > 5) & (df['B'] < 10)]` |

---

## 📂 Input / Output (I/O)

| Function                       | Description   | Example                              |
| ------------------------------ | ------------- | ------------------------------------ |
| `df.to_csv(path, index=False)` | Save to CSV   | `df.to_csv('data.csv', index=False)` |
| `df.to_excel(path)`            | Save to Excel | `df.to_excel('data.xlsx')`           |
| `df.to_json(path)`             | Save to JSON  | `df.to_json('data.json')`            |
| `df.to_sql(table, conn)`       | Save to SQL   | `df.to_sql('table', conn)`           |

---

## 🧰 Miscellaneous

| Function               | Description             | Example                     |
| ---------------------- | ----------------------- | --------------------------- |
| `df.value_counts()`    | Count unique values     | `df['A'].value_counts()`    |
| `df.duplicated()`      | Find duplicates         | `df.duplicated()`           |
| `df.drop_duplicates()` | Remove duplicates       | `df.drop_duplicates()`      |
| `df.sample(n)`         | Random sample           | `df.sample(5)`              |
| `df.nunique()`         | Number of unique values | `df.nunique()`              |
| `df.memory_usage()`    | Memory usage            | `df.memory_usage()`         |
| `df.style.format()`    | Format display          | `df.style.format("{:.2f}")` |

---

## ⚡ Tips

* Use **`inplace=True`** to modify a DataFrame directly (e.g., `df.dropna(inplace=True)`).
* Chain operations with care; use parentheses for readability.
* Use `pd.set_option('display.max_columns', None)` to show all columns.
* For performance: use `df.itertuples()` or `df.to_numpy()` for fast iteration.
