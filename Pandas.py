import pandas as pd
import numpy as np

# -------------------------------
# 1. Create a Simple DataFrame
# -------------------------------
df = pd.DataFrame(
    [[1, 2, 3], [3, 5, 6], [7, 3, 9]],
    columns=["A", "B", "C"],
    index=["x", "y", "z"]
)
print("\n--- First Few Rows ---")
print(df.head(1))
print(df.head(2))
print(df.head(3))
print("head end")

print("\n--- Last Few Rows ---")
print(df.tail(1))
print(df.tail(2))
print(df.tail(3))
print("tail end")

# -------------------------------
# 2. DataFrame Basic Info
# -------------------------------
print("\nColumns:", df.columns)
print("Index:", df.index)
print("Index as list:", df.index.to_list())
print("\n--- Info ---")
df.info()
print("\n--- Description ---")
print(df.describe())
print("Shape:", df.shape)
print("\nNumber of unique values in each column:\n", df.nunique())
print("Unique values in A:", df["A"].unique())

# -------------------------------
# 3. Reading CSV File
# -------------------------------
try:
    student = pd.read_csv('Students Social Media Addiction.csv')
except FileNotFoundError:
    print("\n❌ CSV file not found. Please check the file path!")
    exit()

# -------------------------------
# 4. Viewing Data
# -------------------------------
print("\nFirst 5 rows:\n", student.head(5))
print("\nLast 10 rows:\n", student.tail(10))
print("\nRandom 10 rows:\n", student.sample(10))

# -------------------------------
# 5. Accessing Data
# -------------------------------
print("\nRows from index 700 onwards:\n", student.loc[700:])
print("\nRow with label/index 0:\n", student.loc[0])
print("\nRows from position 700 onwards:\n", student.iloc[700:])

# -------------------------------
# 6. Sorting
# -------------------------------
print("\nSorted by Age:\n", student.sort_values('Age'))

# -------------------------------
# 7. Filtering Data
# -------------------------------
print("\nStudent_ID > 400:\n", student.loc[student['Student_ID'] > 400])
print("\nMethod-1:\n", student.loc[student['Student_ID'] > 400, ['Gender', 'Relationship_Status']])
print("\nMethod-2:\n", student[student['Student_ID'] > 400][['Gender', 'Relationship_Status']])
print("\nTwo conditions:\n", student[(student['Student_ID'] > 400) & (student['Relationship_Status'] == 'Single')])

# -------------------------------
# 8. String Filtering (case-insensitive)
# -------------------------------
print("\nContains 'Female':\n", student[student['Gender'].str.contains("Female", case=False, na=False)])
print("\nRelationship complicated or single:\n",
      student[student['Relationship_Status'].str.contains("complicated|single", case=False, na=False)])
print("\nStarts with Complicated:\n", student[student['Relationship_Status'].str.startswith("Complicated", na=False)])
print("\nUsing isin:\n", student[student['Relationship_Status'].isin(["Complicated", "single"])])

# -------------------------------
# 9. Query
# -------------------------------
print("\nQuery example:\n", student.query('Age > 20 and Gender == "Female"'))

# -------------------------------
# 10. Adding / Updating Columns
# -------------------------------
student['happy?'] = np.where(student['Addicted_Score'] > 8, 'No', 'Yes')
print("\nAfter adding happy? column:\n", student.head())

# -------------------------------
# 11. Dropping
# -------------------------------
print("\nDrop row with index 2:\n", student.drop(2))
print("\nDrop column happy?:\n", student.drop(columns=['happy?']))

# -------------------------------
# 12. Renaming Columns
# -------------------------------
pdf = student.rename(columns={'Relationship_Status': 'is happy or not'})
print("\nRenamed column:\n", pdf.head())

# -------------------------------
# 13. Apply with Lambda
# -------------------------------
student_copy = student.copy()
student_copy['addiction'] = student["Addicted_Score"].apply(
    lambda x: 'high' if x > 5 else ('average' if x > 3 else 'low')
)
print("\nStudent copy with addiction column:\n", student_copy.head())

# -------------------------------
# 14. Apply with Custom Function
# -------------------------------
def Reality_Check(row):
    if row['Age'] > 20 and row['Relationship_Status'] == "In Relationship":
        return "career bnalo! bhadwon"
    elif row['Relationship_Status'] == 'In Relationship' and row['Age'] < 20:
        return "abe pehle ande se to bahar niklo"
    else:
        return "bhagwan aapka bhala kre"

student['Reality_Check'] = student.apply(Reality_Check, axis=1)
print("\nReality Check column:\n", student.head())

#-------------------------------
# 15. Handling Null Values Example
# -------------------------------
"""
🧩 Pandas Interpolation Cheat Sheet

METHODS:
----------------------------------------------------------
1. linear (default)
   - Straight-line estimate between prev & next values.
   - Best for: Numeric data with gradual change.
   Example: 10 → NaN → 30 → fills 20

2. time
   - Interpolates based on actual time index values.
   - Best for: Time series data with DatetimeIndex.
   Note: Index must be datetime type.

3. index
   - Uses numeric index values as x-axis for interpolation.
   - Best for: Irregular numeric indexes.

4. nearest
   - Fills NaN with nearest non-NaN value.
   - Best for: Snapping to closest reading.
   Example: 10 → NaN → 30 → fills 10

5. pad / ffill
   - Forward fills with last valid value.
   - Best for: Keeping previous value until a new one appears.
   Example: 10 → NaN → fills 10

6. backfill / bfill
   - Backward fills from next valid value.
   - Best for: Filling with next value.
   Example: 10 → NaN → 30 → fills 30

7. polynomial
   - Fits a polynomial curve of given order.
   - Best for: Smooth curve data.
   Example: method='polynomial', order=2

8. spline
   - Fits a spline curve for smooth transitions.
   - Best for: Smooth continuous trends.
   Example: method='spline', order=3

9. quadratic
   - Same as polynomial with order=2.
   - Best for: U-shaped data patterns.

----------------------------------------------------------
EXAMPLES:
import pandas as pd
import numpy as np

data = pd.Series([10, np.nan, 30, np.nan, 50])

# Linear interpolation
print(data.interpolate(method='linear'))

# Nearest neighbor
print(data.interpolate(method='nearest'))

# Forward fill
print(data.interpolate(method='pad'))

# Backward fill
print(data.interpolate(method='bfill'))

# Polynomial interpolation
print(data.interpolate(method='polynomial', order=2))
"""

student.loc[[0,1], 'Age'] = pd.NA
student = student.fillna(100)
print(student.dropna())
print(student['Age'].isna())

"""
-----------------------------------------------------------
💡 Pandas: fillna() vs interpolate() - Side-by-Side Example
-----------------------------------------------------------
"""

import pandas as pd
import numpy as np

# Sample data
s = pd.Series([10, np.nan, 30, np.nan, 50])
print("Original Series:\n", s, "\n")

# 1️⃣ fillna() - Static replacement
print("fillna(0):\n", s.fillna(0), "\n")   # Replace NaN with 0
print("fillna(method='ffill'):\n", s.fillna(method='ffill'), "\n")  # Forward fill
print("fillna(method='bfill'):\n", s.fillna(method='bfill'), "\n")  # Backward fill

# 2️⃣ interpolate() - Dynamic estimation
print("interpolate(method='linear'):\n", s.interpolate(method='linear'), "\n")  # Linear
print("interpolate(method='nearest'):\n", s.interpolate(method='nearest'), "\n")  # Nearest neighbor
print("interpolate(method='polynomial', order=2):\n", s.interpolate(method='polynomial', order=2), "\n")  # Polynomial

"""
📝 Key Takeaways:
- fillna(): Directly replaces NaN with given value or previous/next value.
- interpolate(): Calculates missing values based on data trend or method.
- Use fillna() when you know EXACT replacement value.
- Use interpolate() when you want ESTIMATED missing values based on surrounding data.
"""


#-------------------------------
# 15. Aggregating data
# -------------------------------
print(student["Addicted_Score"].value_counts())
print(student[student['Academic_Level']== 'High School']['Age'].value_counts())
print(student.groupby(['Age']).agg({'Addicted_Score' : 'mean' , 'Conflicts_Over_Social_Media' : 'sum'}))

#💡 Key Notes
# groupby('column') → Groups rows based on values in that column.
# You can call aggregation functions directly (sum(), mean(), count()).
# .agg() → Allows multiple functions on multiple columns.
# Works with multiple grouping keys.
# You can also use .apply() for custom logic.

pivot = student.pivot_table(columns="Academic_Level",index='Addicted_Score',values="happy?",aggfunc='first')# or "count", "sum", etc. depending on your need
print(pivot)
# pivot() reshapes your DataFrame:
# - Turns unique values in a column into new columns
# - Rearranges data to make it easier to read or analyze
# - It’s like turning a long table into a wide table 📊

# 📌 Pandas Reshaping & Aggregation Cheat Sheet
# =============================================
#
# 🔄 pivot():
#   - Reshapes DataFrame: unique values in one column become new columns.
#   - Requires unique index/column combinations (no duplicates).
#   - Syntax:
#       df.pivot(index='row_col', columns='col_to_expand', values='value_col')
#
# 🔄 pivot_table():
#   - Like pivot(), but handles duplicates using an aggregation function (aggfunc).
#   - Useful for summarizing data.
#   - Syntax:
#       df.pivot_table(index='row_col', columns='col_to_expand', values='value_col', aggfunc='mean')
#
# 🔄 melt():
#   - Opposite of pivot: turns wide table into long table.
#   - Syntax:
#       pd.melt(df, id_vars=['keep_these'], value_vars=['unpivot_these'])
#
# 🔄 stack():
#   - Rotates column labels into rows (MultiIndex to long form).
#   - Often used after pivoting to re-flatten data.
#   - Syntax:
#       df.stack()
#
# 🔄 unstack():
#   - Opposite of stack(): moves row index to column axis.
#   - Syntax:
#       df.unstack()
#
# ---------------------------------------------
# 💡 Common Aggregation Functions (aggfunc):
# ---------------------------------------------
# "mean"     -> Average of values
# "sum"      -> Total sum of values
# "count"    -> Number of non-null values
# "nunique"  -> Number of unique values
# "min"      -> Minimum value
# "max"      -> Maximum value
# "median"   -> Median value
# "std"      -> Standard deviation
# "var"      -> Variance
# "first"    -> First non-null value
# "last"     -> Last non-null value
#
# ✅ Examples:
# df.pivot_table(index='Category', values='Sales', aggfunc='sum')
# df.groupby('Category')['Sales'].agg(['mean', 'max'])
# pd.melt(df, id_vars=['ID'], value_vars=['Math', 'Science'])


# 📌 Pandas Window, Ranking & Shifting Functions Cheat Sheet
# ===========================================================
#
# 🔄 shift():
#   - Shifts data in a column/row by a specified number of periods.
#   - Useful for comparing current row with previous/next row.
#   - Syntax:
#       df['prev_value'] = df['value'].shift(1)   # shift down by 1
#       df['next_value'] = df['value'].shift(-1)  # shift up by 1
#
# 📊 rank():
#   - Assigns ranks to values (1 = smallest by default).
#   - Handles ties by default with average rank.
#   - Syntax:
#       df['rank'] = df['score'].rank(method='average', ascending=True)
#   - Common methods: 'average', 'min', 'max', 'first', 'dense'
#
# 🔄 rolling():
#   - Performs calculations on a rolling/moving window.
#   - Common in time-series for moving averages, sums, etc.
#   - Syntax:
#       df['rolling_mean'] = df['value'].rolling(window=3).mean()
#       df['rolling_sum']  = df['value'].rolling(window=5).sum()
#   - Parameters:
#       window   -> number of observations
#       min_periods -> minimum observations required for calculation
#       center   -> center the window label
#
# 🔄 expanding():
#   - Similar to rolling, but window starts from the first value and expands.
#   - Syntax:
#       df['cum_mean'] = df['value'].expanding().mean()
#
# 🔄 cumsum(), cumprod(), cummax(), cummin():
#   - Cumulative operations.
#   - Syntax:
#       df['cum_sum'] = df['value'].cumsum()
#       df['cum_max'] = df['value'].cummax()
#
# 🔄 diff():
#   - Difference between current element and previous element.
#   - Syntax:
#       df['change'] = df['value'].diff()
#
# 🔄 pct_change():
#   - Percentage change between the current and previous row.
#   - Syntax:
#       df['pct_change'] = df['value'].pct_change()
#
# ✅ Examples:
# df['prev'] = df['Sales'].shift(1)
# df['rank'] = df['Sales'].rank(ascending=False)
# df['ma_3'] = df['Sales'].rolling(window=3).mean()
# df['cum_total'] = df['Sales'].cumsum()
# df['change'] = df['Sales'].diff()
# df['pct'] = df['Sales'].pct_change()

print(pd.__version__)


# 📌 Pandas Window, Ranking & Shifting Functions Cheat Sheet
# ===========================================================
#
# 🔄 shift():
#   - Shifts data in a column/row by a specified number of periods.
#   - Useful for comparing current row with previous/next row.
#   - Syntax:
#       df['prev_value'] = df['value'].shift(1)   # shift down by 1
#       df['next_value'] = df['value'].shift(-1)  # shift up by 1
#
# 📊 rank():
#   - Assigns ranks to values (1 = smallest by default).
#   - Handles ties by default with average rank.
#   - Syntax:
#       df['rank'] = df['score'].rank(method='average', ascending=True)
#   - Common methods: 'average', 'min', 'max', 'first', 'dense'
#
# 🔄 rolling():
#   - Performs calculations on a rolling/moving window.
#   - Common in time-series for moving averages, sums, etc.
#   - Syntax:
#       df['rolling_mean'] = df['value'].rolling(window=3).mean()
#       df['rolling_sum']  = df['value'].rolling(window=5).sum()
#   - Parameters:
#       window   -> number of observations
#       min_periods -> minimum observations required for calculation
#       center   -> center the window label
#
# 🔄 expanding():
#   - Similar to rolling, but window starts from the first value and expands.
#   - Syntax:
#       df['cum_mean'] = df['value'].expanding().mean()
#
# 🔄 cumsum(), cumprod(), cummax(), cummin():
#   - Cumulative operations.
#   - Syntax:
#       df['cum_sum'] = df['value'].cumsum()
#       df['cum_max'] = df['value'].cummax()
#
# 🔄 diff():
#   - Difference between current element and previous element.
#   - Syntax:
#       df['change'] = df['value'].diff()
#
# 🔄 pct_change():
#   - Percentage change between the current and previous row.
#   - Syntax:
#       df['pct_change'] = df['value'].pct_change()
#
# ✅ Examples:
# df['prev'] = df['Sales'].shift(1)
# df['rank'] = df['Sales'].rank(ascending=False)
# df['ma_3'] = df['Sales'].rolling(window=3).mean()
# df['cum_total'] = df['Sales'].cumsum()
# df['change'] = df['Sales'].diff()
# df['pct'] = df['Sales'].pct_change()


# 📌 Pandas + PyArrow Integration Example
# ========================================
# Make sure you have pyarrow installed:
# pip install pyarrow pandas

import pandas as pd

# 🎯 1. Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [88.5, 92.0, 79.5]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 🎯 2. Save DataFrame to a Parquet file using PyArrow as the engine
df.to_parquet("people.parquet", engine="pyarrow", index=False)
print("\n✅ Data saved to 'people.parquet' using PyArrow")

# 🎯 3. Read Parquet file back into DataFrame
df_parquet = pd.read_parquet("people.parquet", engine="pyarrow")
print("\nDataFrame read from 'people.parquet':\n", df_parquet)

# 🎯 4. Save DataFrame to a Feather file
df.to_feather("people.feather")
print("\n✅ Data saved to 'people.feather' (Feather format)")

# 🎯 5. Read Feather file back into DataFrame
df_feather = pd.read_feather("people.feather")
print("\nDataFrame read from 'people.feather':\n", df_feather)

# 📌 Why use Parquet/Feather with PyArrow?
# - Much faster read/write than CSV
# - Preserves data types
# - Ideal for large datasets
# - Compatible across Python, R, and big data tools
