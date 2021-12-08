Task

You are given two values  and .
Perform integer division and print .

Output Format

Print the value of .
In the case of ZeroDivisionError or ValueError, print the error code.




Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'

























def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")