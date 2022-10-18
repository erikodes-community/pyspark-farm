# Using Windows

What are windows in PySpark?

Better question: What are windows in Spark?

```
window_function OVER

```

Syntax for Window.partition:

```
Window.partitionBy(“column_name”).orderBy(“column_name”)
```
Syntax for Window function:
```
DataFrame.withColumn(“new_col_name”, Window_function().over(Window_partition))
```

