************* Module test_ColorSpiral
C:  1, 0: Invalid module name "test_ColorSpiral" (invalid-name)
C: 62, 8: Invalid attribute name "c" (invalid-name)
C: 68, 8: Invalid variable name "cs" (invalid-name)
C: 80, 8: Invalid variable name "cs" (invalid-name)
C: 82,12: Invalid variable name "r" (invalid-name)
C: 82,15: Invalid variable name "g" (invalid-name)
C: 82,18: Invalid variable name "b" (invalid-name)
C: 85,12: Invalid variable name "h" (invalid-name)
C: 85,15: Invalid variable name "s" (invalid-name)
C: 85,18: Invalid variable name "v" (invalid-name)
C: 87,12: Invalid variable name "x" (invalid-name)
C: 87,15: Invalid variable name "y" (invalid-name)
W: 85,18: Unused variable 'v' (unused-variable)
R: 55, 0: Too many public methods (48/20) (too-many-public-methods)
C:104, 8: Invalid attribute name "c" (invalid-name)
C:111,15: Invalid variable name "c" (invalid-name)
C:113,12: Invalid variable name "x1" (invalid-name)
C:114,12: Invalid variable name "y1" (invalid-name)
R: 97, 0: Too many public methods (47/20) (too-many-public-methods)
R:125, 0: Too many public methods (46/20) (too-many-public-methods)
C:140, 4: Invalid constant name "runner" (invalid-name)


Report
======
64 statements analysed.

Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |17     |17       |=          |
+-----------+-------+---------+-----------+
|refactor   |3      |3        |=          |
+-----------+-------+---------+-----------+
|warning    |1      |1        |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+------------------------+------------+
|message id              |occurrences |
+========================+============+
|invalid-name            |17          |
+------------------------+------------+
|too-many-public-methods |3           |
+------------------------+------------+
|unused-variable         |1           |
+------------------------+------------+



Global evaluation
-----------------
Your code has been rated at 6.72/10 (previous run: 6.72/10, +0.00)

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |67     |49.26 |67       |=          |
+----------+-------+------+---------+-----------+
|docstring |23     |16.91 |23       |=          |
+----------+-------+------+---------+-----------+
|comment   |33     |24.26 |33       |=          |
+----------+-------+------+---------+-----------+
|empty     |13     |9.56  |13       |=          |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |100.00   |
+---------+-------+-----------+-----------+------------+---------+
|class    |3      |3          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |8      |8          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+



External dependencies
---------------------
::

    Bio 
      \-MissingPythonDependencyError (test_ColorSpiral)
    ColorSpiral 
      \-ColorSpiral (test_ColorSpiral)
      \-get_color_dict (test_ColorSpiral)
      \-get_colors (test_ColorSpiral)
    reportlab 
      \-lib 
      | \-pagesizes 
      |   \-A4 (test_ColorSpiral)
      \-pdfgen 
        \-canvas 
          \-Canvas (test_ColorSpiral)



