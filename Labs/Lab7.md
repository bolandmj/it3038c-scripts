# LAB 7

This is a calculator plugin that can be installed using the pip installer. 

The code below is used to install the calculator plugin.

```python
pip install calculator_102
```

Calculator holds numbers in memory and this memory can be retrieved using this code.

```python
calculator = Calculator()
calculator.memory()
```

Adding, subtracting, division, multiplication, and n-root can all be performed using these functions.

```python
Num = 1
calculator.add(Num)
calculator.subtract(Num)
calculator.multiply(Num)
calculator.divide(Num)
calculator.n_root(Num)
```

To reset the calculator memory to 0 use the function.

```python
calculator.reset()
```

To see more visit https://pypi.org/project/calculator_102/
