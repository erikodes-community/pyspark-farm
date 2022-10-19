# Pyspark and Python Imports

From the PySpark documentation, we have:

```python
from pyspark.sql import SparkSession
```

However, if we inspect the source code, we would find that the SparkSession class actually lives in the module `pyspark.sql.session`. So shouldn't we have to import it like this?

```python
from pyspark.sql.session import SparkSession
```


If we look more closely, we see that the file `__init__.py` in the package `spark.sql` has the following import statement:

```python
from pyspark.sql.session import SparkSession
```

So, when we say `from pyspark.sql import SparkSession`, a line in `pyspark.sql.__init__` tells Python to go and look in `pyspark.sql.session` for `SparkSession`.

For a demonstration of how this works, without the large PySpark codebase to distract us, let's look at `my_cool_package`.
