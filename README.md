# regular-expression-to-nfa

This program "ex2-v2.py" converts regular expression into e-NFA and gives e-NFA table as output.

### Requirements
1. Python 3.6+

### How to Run?
Install Python 3.6+
Clone this repository
In command line type:
```
python ex2-v2.py
```

You can also give your custom regular expression in the first line of the program

*Few things to take note of:
    a and b are the only terminals accepted by this script
    e denotes epsilon
    . is used for "and" operation Eg. ab = a.b
    + is used for "or" operation Eg. a|b = a+b
    * is the Kleene's Closure operator. You can give star operator after any closing brackets and terminals*

