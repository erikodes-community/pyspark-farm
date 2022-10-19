# Using Windows

What are windows in PySpark?

Better (first) question: What are windows in Spark?


From the Spark documentation:

"Window functions operate on a group of rows, referred to as a window, and calculate a return value for each row based on the group of rows. Window functions are useful for processing tasks such as calculating a moving average, computing a cumulative statistic, or accessing the value of rows given the relative position of the current row." 

The Spark documentation also shows the syntax for window functions like this:

```sql
window_function [ nulls_option ] OVER
( [  { PARTITION | DISTRIBUTE } BY partition_col_name = partition_col_val ( [ , ... ] ) ]
  { ORDER | SORT } BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [ , ... ]
  [ window_frame ] )
```

I'm going to attempt to translate this block of syntax into English. Here it goes:

First, write down a window function. Then, optionally write down a null option. Then write OVER. Then write an opening parenthesis. Then optionally write PARTITION OR DISTRIBUTE followed by one or more partition column names separated by commas. Then write ORDER or SORT followed by BY and an expression. Next, optionally include either ASC or DESC. Then optionally include NULLS followed by either FIRST or LAST. Then optionally repeat something. (?) Include optionally a window frame. Then include a closing parenthesis.

That's a lot to look at all at once, so let's pull out some possible examples.

```sql
window_function OVER (PARTITION BY partition_col_name ORDER BY expression)

window_function OVER (SORT BY expression)

window_function IGNORE NULLS OVER (PARTITION BY partition_column_name ORDER BY expression ASC window_frame)

window_function OVER (ORDER BY expression DESC NULLS FIRST)
```

Next, let's look at this with some example data. 
The data is like this:

|name|dept|salary|age|
|---|---|---|---|
|Lisa|Sales|10000|35|
|Evan|Sales|32000|38|
|Fred|Engineering|21000|28|
|Alex|Sales|30000|33|
|Tom|Engineering|23000|33|
|Jane|Marketing|29000|28|
|Jeff|Marketing|35000|38|
|Paul|Engineering|29000|23|
|Chloe|Engineering|23000|25|



```sql
SELECT name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary) AS rank FROM employees;
```


Here's an example in SQL syntax

```
window_function() OVER (PARTITION BY thing ORDER BY other_thing)
```
And an example from the Apache Spark documentation:
```
SELECT name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary) AS rank FROM employees;

```

Here's an example of what I ended up writing in Python, but shown here in SQL.

```
SELECT *, RANK() OVER (PARTITION BY tag ORDER BY hay_ration) as rank FROM df
```

Syntax for Window.partition:

```
Window.partitionBy(“column_name”).orderBy(“column_name”)
```
Syntax for Window function:
```
DataFrame.withColumn(“new_col_name”, Window_function().over(Window_partition))
```

Here's the Python code that I actually used:
```python
window = Window.partitionBy('tag').orderBy('hay_ration')

df = df.withColumn('rank', F.rank().over(window))
```