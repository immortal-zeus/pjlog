# PJLOG

This is a simple Logarithm Library to make working with Logarithm easy and with better useful functions.

## Installation

Run the following to install 
```python
pip install pjlog
```

## Usage

```python
import pjlog as pl

# Make a Logarithm Object 
a = pl.log(value = 100, base =10)

# Printing the Object 
print(a)

# To get value
print(a.Lget_value())

# To add
c = a + pl.log(value =4 , base =2 )
```