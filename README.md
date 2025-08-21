## 💡 What You’ll Learn

- ✅ Python syntax & logic building
- ✅ Basic Git & GitHub workflow
- ✅ Numpy library
- ✅ Pandas library
- ✅ Matplotlib library


## 🧪 Requirements

- Python 3.x
- VS Code / any text editor
- python libraries- numpy , pandas , matplotlib

# NumPy Practice 🧮

This folder contains my NumPy practice exercises after watching a NumPy crash course. It includes array creation, reshaping, indexing, slicing, mathematical operations, boolean filtering, and more.

## 🧠 Topics Covered
- Creating 1D, 2D arrays
- Zeros, Ones, Arange, Linspace
- Indexing & slicing arrays
- Mathematical operations
- Dot product & elementwise ops
- Reshaping arrays
- Flattening
- Aggregation: mean, std, min, max
- Boolean masking & filtering

## 📂 Files

| File Name           | Description                        |
|---------------------|------------------------------------|
| Numpy.py | Python file with all NumPy examples |

## ▶ How to Run

```bash
python Numpy.py
```


# Pandas Practice 🧮

This folder contains my Pandas practice exercises after completing the Pandas crash course.  
It covers dataset loading, data cleaning, filtering, grouping, sorting, and basic analysis.

## 🧠 Topics Covered
- Reading CSV files (`pd.read_csv`)
- Viewing data (`head`, `tail`, `info`, `describe`)
- Selecting rows & columns (`loc`, `iloc`)
- Filtering with conditions
- Sorting data (`sort_values`)
- Adding & modifying columns
- Grouping & aggregations (`groupby`, `mean`, `sum`, `count`)
- Handling missing values (`fillna`, `dropna`)
- Exporting datasets (`to_csv`)

## 📂 Files

| File Name           | Description                                   |
|---------------------|-----------------------------------------------|
| `Pandas.py`| Python file with Pandas examples and exercises|

## ▶️ How to Run

```bash
python Pandas.py
```

# Matplotlib Practice 📊

This folder contains my Matplotlib practice exercises after completing the Matplotlib crash course.  
It includes basic plotting, customization, legends, labels, styles, bar charts, pie charts, histograms, and more.

---

## 🧠 Topics Covered
- Basic line plots
- Adding labels & titles
- Legends (`ax.legend()`)
- Line styles, colors & markers
- Bar charts (vertical & horizontal)
- Pie charts
- Histograms
- Plotting multiple datasets
- Customizing figure size & layout
- Using `plt.style` and `plt.xkcd` mode

---

## 📂 Files

| File Name        | Description                               |
|------------------|-------------------------------------------|
| `Matplotlib.py`  | Python file with all Matplotlib examples  |

---

## ▶ How to Run
```bash
python Matplotlib.py
```


## ===== Choosing the Right Plot =====
- plt.plot()        → Use for continuous numeric data over a sequence (like trends over time)
- plt.bar()         → Use for categorical data (vertical bars) when categories are few
- plt.barh()        → Use for categorical data (horizontal bars), good for long labels
- plt.scatter()     → Use to show relationship between two numeric variables
- plt.hist()        → Use for distribution of a single numeric variable
- plt.fill_between()→ Use for area charts (good for showing magnitude over a range)
- plt.pie()         → Use for showing parts of a whole (not great for many categories)

# Seaborn Visual Cheat Sheet 🌈

A **cute & quick guide** for Seaborn — perfect for Python data visualization! 🐾  
Includes **code + mini example plots** for fast learning & revision.

---

## 1️⃣ Basics
- **Seaborn** = Statistical visualization library built on Matplotlib  
- **Install:** `pip install seaborn`  
- **Import:**
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```

## 2️⃣ Common Plots
-**Barplot**
Numeric vs categorical
```
sns.barplot(x='Gender', y='Hours', data=df)
plt.show()
Male   ▇▇▇▇
Female ▇▇▇
```
-**Countplot**
Category frequency
```
sns.countplot(x='Gender', data=df)
plt.show()
Male   ▇▇▇▇▇
Female ▇▇▇
```
-**Scatterplot**
Numeric vs numeric with optional hue/style
```
sns.scatterplot(x='Age', y='Hours', hue='Gender', style='Gender', data=df)
plt.show()
```
Example: Points colored by Gender

-**Boxplot**
Distribution & outliers
```
sns.boxplot(x='Gender', y='Hours', data=df)
plt.show()
```
Example: Shows median, quartiles & outliers

-**Boxplot**
Distribution & outliers
```
sns.boxplot(x='Gender', y='Hours', data=df)
plt.show()
```
Example: Shows median, quartiles & outliers

-**Heatmap**
Color-coded numbers / correlation
```
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```
Example: Darker = higher correlation, lighter = lower correlation

-**Lineplot / Pointplot**
Trend over x, summary per category
```
sns.pointplot(x='Day', y='Sales', data=df)
plt.show()
```
example: Shows average sales per day

##3️⃣ Estimator 🧠

Summarize multiple numeric values per category into one value
Default: np.mean
Other options: np.median, np.sum, custom function
```
sns.barplot(x='Gender', y='Hours', data=df, estimator=np.median)
```
##4️⃣ Color & Style

**palette** → color scheme: 'pastel', 'coolwarm', 'Blues'

**hue** → color by another categorical column

**style** → marker shape / line style
```
sns.scatterplot(x='Age', y='Hours', hue='Gender', style='Gender', data=df)
```

##5️⃣ Quick Tricks ✨

-Always add plt.show() to display plots
-order → control category order in barplots
-linewidths → separate cells in heatmap
-Combine hue + style → multi-category visualization
-Can use figsize from Matplotlib: plt.figure(figsize=(8,5))


📜 License
This project is open source and available under the MIT License.

🙋‍♂ Author
Minakshi Dubey
undergraduating AIML engineering student passionate about Python and AI.

⭐ Want to Help?
If you found this useful, feel free to ⭐ star the repo or share it with your friends learning Python!
