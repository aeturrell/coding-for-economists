---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: 'Python 3.8.6 64-bit (''codeforecon'': conda)'
  language: python
  name: codeforecon
---

# Basics of Coding

In this chapter, you'll learn about the basics of objects, types, operations, conditions, loops, functions, and imports. These are the basic building blocks of any programming language.

## If you get stuck

It's worth saying at the outset that, *no-one*, and I mean no-one, memorises half of the stuff you'll see in this book. 80% or more of time spent programming is actually time spent looking up how to do this or that online, 'debugging' a code for errors, or testing code. This applies to all programmers, regardless of level. You are here to learn the skills and concepts of programming, not the precise syntax (which is easy to look up later).

![xkcd-what-did-you-see](https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png)

Knowing how to Google is one of the most important skills of any coder. No-one remembers every function from every library. Here are some useful coding resources:

- when you have an error, look on Stack Overflow to see if anyone else had the same error (they probably did) and how they overcame it.

- if you're having trouble navigating a new package or library, look up the documentation online. The best libraries put as much effort into documentation as they do the code base.

- use cheat sheets to get on top of a range of functionality quickly. For instance, this excellent (mostly) base Python [Cheat Sheet](https://gto76.github.io/python-cheatsheet/).

- if you're having a coding issue, take a walk to think about the problem, or explain your problem to an animal toy on your desk ([traditionally](https://en.wikipedia.org/wiki/Rubber_duck_debugging) a rubber duck, but other animals are available).

## Variables and types

Creating a variable in Python is achieved via an assignment. It's simpler than it sounds:

```{code-cell} ipython3
a = 10
print(a)
```

This creates a variable `a`, assigns the value 10 to it, and prints it. Sometimes you will hear variables referred to as *objects*. Everything that is not a literal value, such as `10`, is an object. In the above example, `a` is an object that has been assigned the value `10`.

How about this:

```{code-cell} ipython3
b = 'This is a string'
print(b)
```

It's the same thing but with a different **type** of data, a string instead of an integer. Python is *dynamically typed*, which you means it will guess what type of variable you're creating as you create it. This has pros and cons, with the main pro being that it makes for more concise code.

```{admonition} Important
Everything is an object, and every object has a type.
```

The most basic built-in data types that you'll need to know about are: integers `10`, floats `1.23`, strings `like this`, booleans `True`, and nothing `None`. Python also has a built-in types called a list `[10, 15, 20]` that can contain anything, even *different* types. So

```{code-cell} ipython3
list_example = [10, 1.23, 'like this', True, None]
print(list_example)
```

is completely valid code. As well as the built-in types, packages can define their own custom types.

If you ever want to check the type of a Python variable, you can call the `type` function on it like so:

```{code-cell} ipython3
type(list_example)
```

## Lists and slicing

Lists are a really useful way to work with lots of data at once. They're defined with square brackets, with entries separated by commas. You can also construct them by appending entries:

```{code-cell} ipython3
list_example.append('one more entry')
print(list_example)
```

And you can access earlier entries using an index, which begins at 0 and ends at one less than the length of the list (this is the convention in many programming languages). For instance, to print specific entries at the start, using `0`, and end, using `-1`:

```{code-cell} ipython3
print(list_example[0])
print(list_example[-1])
```

As well as accessing positions in lists using indexing, you can use *slices* on lists. This uses the colon character, `:`, to stand in for 'from the beginning' or 'until the end' (when only appearing once). For instance, to print just the last two entries, we would use the index `-2:` to mean from the second-to-last onwards. If we just want the first and last three entries to be printed, we can use:

```{code-cell} ipython3
print(list_example[:3])
print(list_example[-3:])
```

Slicing can be even more elaborate than that because we can jump entries using a second colon. Here's a full example that begins at the second entry (remember the index starts at 0), runs up until the second-to-last entry (exclusive), and jumps every other entry inbetween (range just produces a list of numbers):

```{code-cell} ipython3
list_of_numbers = list(range(1, 11))
start = 1
stop = -1
step = 2
print(list_of_numbers[start:stop:step])
```

A handy trick is that you can reverse a list entirely using this:

```{code-cell} ipython3
print(list_of_numbers[::-1])
```

## Operators

All of the basic operators you see in mathematics are available to use: `+` for addition, `-` for subtraction, `*` for multiplication, `**` for powers, `/` for division, and `%` for modulo. These work as you'd expect on numbers. But these operators are sometimes defined for other built-in data types too. For instance, we can 'sum' strings (which really concatenates them):

```{code-cell} ipython3
string_one = 'This is an example '
string_two = 'of string concatenation'
string_full = string_one + string_two
print(string_full)
```

It works for lists too:

```{code-cell} ipython3
list_one = ['apples', 'oranges']
list_two = ['pears', 'satsumas']
list_full = list_one + list_two
print(list_full)
```

Perhaps more surprisingly, you can multiply strings!

```{code-cell} ipython3
string = 'apples, '
print(string*3)
```

## Strings

In some ways, strings are treated a bit like lists, meaning you can access the individual characters via slicing and indexing. For example:

```{code-cell} ipython3
string = 'cheesecake'
print(string[-4:])
```

Both lists and strings will also allow you to use the `len` command to get their length:

```{code-cell} ipython3
string = 'cheesecake'
print('String has length:')
print(len(string))
list_of_numbers = range(1, 20)
print('List of numbers has length:')
print(len(list_of_numbers))
```

There are various functions built into Python to help you work with strings that are particularly useful for cleaning messy data. For example, imagine you have a variable name like 'This Is /A Variable   '. (You may think this is implausibly bad; I only wish that were true). Let's see if we can clean this up:

```{code-cell} ipython3
string = 'This Is /A Variable   '
string = string.replace('/', '').rstrip().lower()
print(string)
```

The steps above replace the character '/', strip out whitespace on the right hand-side of the string, and put everything in lower case. The brackets after the words signify that a function has been applied; we'll see more of functions later.

You'll often want to output one type of data as another, and Python generally knows what you're trying to achieve if you, for example, `print` a boolean value. For numbers, there are more options and you can see a big list of advice on string formatting of all kinds of things [here](https://pyformat.info/). For now, let's just see a simple example of something called an f-string, a string that combines a number and a string (these begin with an `f` for formatting):

```{code-cell} ipython3
value = 20
sqrt_val = 20**0.5
print(f'The square root of {value:d} is {sqrt_val:.2f}')
```

The formatting command `:d` is an instruction to treat `value` like an integer, while `:.2f` is an instruction to print it like a float with 2 decimal places.

```{note}
f-strings are only available in Python 3.6+
```

## Booleans and conditions

Some of the most important operations you will perform are with True and False values, also known as boolean data types. First, these behave as you'd expect: `True and False` evaluates to `False`, while `True or False` evaluates to `True`. There's also the `not` keyword. For example

```{code-cell} ipython3
not True
```

as you might expect.

Conditions are expressions that evaluate as booleans. A simple example is `10 == 20`. The `==` is yet another operator that compares the objects on either side and returns `True` if they have the same *values*--though be careful using it with different data types. The opposite of `==` is `!=`, which you can read as 'not equal to the value of'. Here's an example of `==`:

```{code-cell} ipython3
boolean_condition = (10 == 20)
print(boolean_condition)
```

The real power of conditions comes when we start to use them in more complex examples. Some of the keywords that evaluate conditions are `if`, `else`, `and`, `or`, `in`, `not`, and `is`. Here's an example showing how some of these conditional keywords work:

```{code-cell} ipython3
name = 'Ada'
score = 99

if name == 'Ada' and score > 90:
    print('Ada, you achieved a high score.')

if name == 'Smith' or score > 90:
    print('You could be called Smith or have a high score')

if name != 'Smith' and score > 90:
    print('You are not called Smith and you have a high score')

```

All three of these conditions evaluate as True, and so all three messages get printed. Given that `==` and `!=` test for equality and not equal, respectively, you may be wondering what the keywords `is` and `not` are for. Remember that everything in Python is an object, and that values can be assigned to objects. `==` and `!=` compare *values*, while `is` and `not` compare *objects*. For example,

```{code-cell} ipython3
name_list = ['Ada', 'Adam']
name_list_two = ['Ada', 'Adam']

# Compare values
print(name_list == name_list_two)

# Compare objects
print(name_list is name_list_two)
```

One of the most useful conditional keywords is `in`. I must use this one ten times a day to pick out a variable or make sure something is where it's supposed to be.

```{code-cell} ipython3
name_list = ['Lovelace', 'Smith', 'Hopper', 'Babbage']

print('Lovelace' in name_list)

print('Bob' in name_list)
```

The opposite is `not in`.

Finally, one conditional construct you're bound to use at *some* point, is the `if`...`else` structure:

```{code-cell} ipython3
score = 98

if score == 100:
    print('Top marks!')
elif score>90 and score<100:
    print('High score!')
elif score>10 and score<=90:
    pass
else:
    print('Better luck next time.')
```

Note that this does nothing if the score is between 11 and 90, and prints a message otherwise.

## Indentation

You'll have seen that certain parts of the code examples are indented. Code that is part of a function, conditional clause, or loop is indented. This isn't a code style choice, it's actually what tells the language that some code is to be executed as part of, say, a loop and not to executed after the loop is finished.

The standard for indentation is that each sub-statement should be indented by 4 spaces. It can be hard to keep track of these but, as usual, Visual Studio Code has you covered. Go to Settings (the cog in the bottom left-hand corner, then click Settings) and type 'Whitespace' into the search bar. Under 'Editor: Render Whitespace', select 'boundary'. This will show any whitespace that is more than one character long using faint grey dots. Each level of indentation in your Python code should now begin with four grey dots showing that it consists of four spaces.

## Loops and list comprehensions

A loop is a way of executing a similar piece of code over and over in a similar way. The most useful loops are `for` loops and list comprehensions.

A `for` loop does something *for* the time that the condition is satisfied. For example,

```{code-cell} ipython3
name_list = ['Lovelace', 'Smith', 'Pigou', 'Babbage']

for name in name_list:
    print(name)

```

prints out a name until all names have been printed out. A useful trick with for loops is the `enumerate` keyword, which runs through an index that keeps track of the items in a list:

```{code-cell} ipython3
name_list = ['Lovelace', 'Smith', 'Hopper', 'Babbage']

for i, name in enumerate(name_list):
    print(f'The name in position {i} is {name}')

```

High-level languages like Python and R do not get *compiled* into highly performant machine code ahead of being run, unlike C++ and FORTRAN. What this means is that although they are much less unwieldy to use, some types of operation can be very slow--and `for` loops are particularly cumbersome. (Although you may not notice this unless you're working on a bigger computation.)

But there is a way around this, and it's with something called a *list comprehension*. These can combine what a `for` loop and a `condition` do in a single line of efficiently executable code. Say we had a list of numbers and wanted to filter it according to whether the numbers divided by 3 or not:

```{code-cell} ipython3
number_list = range(1, 40)
divide_list = [x for x in number_list if x % 3 == 0]
print(divide_list)
```

Or if we only wanted to pick out names that end in 'Smith':

```{code-cell} ipython3
names_list = ['Joe Bloggs', 'Adam Smith', 'Sandra Noone', 'leonara smith']
smith_list = [x for x in names_list if 'smith' in x.lower()]
print(smith_list)
```

Note how we used 'smith' rather than 'Smith' and then used `lower()` to ensure we matched names regardless of the case they are written in. We can even do a whole `if` ... `else` construct *inside* a list comprehension:

```{code-cell} ipython3
names_list = ['Joe Bloggs', 'Adam Smith', 'Sandra Noone', 'leonara smith']
smith_list = [x if 'smith' in x.lower() else 'Not Smith!' for x in names_list]
print(smith_list)
```

Many of the constructs we've seen can be combined. For instance, there is no reason why we can't have a nested or repeated list comprehension, and, perhaps more surprisingly, sometimes these are useful!

```{code-cell} ipython3
first_names = ['Ada', 'Adam', 'Grace', 'Charles']
last_names = ['Lovelace', 'Smith', 'Hopper', 'Babbage']
names_list = [x + ' ' + y for x, y in zip(first_names, last_names)]
print(names_list)
```

The `zip` keyword is doing this magic; think of it like a zipper, bringing an element of each list together in turn.

Finally, an even more extreme use of list comprehensions can deliver nested structures:

```{code-cell} ipython3
first_names = ['Ada', 'Adam']
last_names = ['Lovelace', 'Smith']
names_list = [[x + ' ' + y for x in first_names] for y in last_names]
print(names_list)
```

This gives a nested structure that (in this case) iterates over `first_names` first, and then `last_names`. If you'd like to learn more about list comprehensions, check out these [short video tutorials](https://calmcode.io/comprehensions/introduction.html).

## Functions

If you're an economist, I hardly need to tell you what a function is. In coding, it's much the same as in mathematics: a function has inputs, it performs its function, and it returns any outputs. Functions begin with a `def` keyword for 'define a function'. The body of the function is then indented relative to the left-most text. Function arguments are defined in brackets following the name, with different inputs separated by commas. Any outputs are given with the `return` keyword, again with different variables separated by commas. Let's see a very simple example:

```{code-cell} ipython3

def welcome_message(name):
    return f'Hello {name}, and welcome!'

# Without indentation, this code is not part of function
name = 'Ada'
output_string = welcome_message(name)
print(output_string)
```

One powerful feature of functions is that we can define defaults for the input arguments. Let's see that in action by defining a default value for `name`, along with multiple outputs--a hello message and a score.

```{code-cell} ipython3

def score_message(score, name='student'):
    """This is a doc-string, a string describing a function.
    Args:
        score (float): Raw score
        name (str): Name of student
    Returns:
        str: A hello message.
        float: A normalised score.
    """
    norm_score = (score-50)/10
    return f'Hello {name}', norm_score

# Without indentation, this code is not part of function
name = 'Ada'
score = 98
# No name entered
print(score_message(score))
# Name entered
print(score_message(score, name=name))
```

In that last example, you'll notice that I added some text to the function. This is a doc-string. It's there to help users (and, most likely, future you) to understand what the function does. Let's see how this works in action by calling `help` on the `score_message` function:

```{code-cell} ipython3
help(score_message)
```

## Dictionaries

Another built-in Python type that is enormously useful is the *dictionary*. This provides a mapping one set of variables to another (either one-to-one or many-to-one). Let's see an example of defining a dictionary and using it:

```{code-cell} ipython3
fruit_dict = {'Jazz': 'Apple', 'Owari': 'Satsuma', 'Seto': 'Satsuma',
              'Pink Lady': 'Apple'}

# Add an entry
fruit_dict.update({'Cox': 'Apple'})

variety_list = ['Jazz', 'Jazz', 'Seto', 'Cox']

fruit_list = [fruit_dict[x] for x in variety_list]
print(fruit_list)
```

From an input list of varieties, we get an output list of their associated fruits. Another good trick to know with dictionaries is that you can iterate through their keys and values:

```{code-cell} ipython3

for key, value in fruit_dict.items():
    print(key + ' maps into ' + value)

```

## Using packages and modules

We already saw how to install packages in the previous chapter: using `pip install packagename` or `conda install packagename` on the command line. What about using a package that you've installed? That's what we'll look at now.

```{note}
If you want to install packages into a dedicated conda environment, remember to `conda activate environmentname` before using the package install command(s).
```

Let's see an example of using the powerful numerical library **numpy**. There are different ways to import packages, you can import the entire package in one go or just import the functions you need. When an entire package is imported, you can give it any name you like and the convention for **numpy** is to import it as the shortened 'np'. All of the functions and methods of the package can be accessed by typing `np` followed by `.` and then typing the function name. As well as demonstrating importing the whole package, the example below shows importing just one specific function.

```{code-cell} ipython3
import numpy as np
from numpy.linalg import inv

matrix = np.array([[4., 2., 4.], [4., 5., 6.], [7., 8., 9.]])

print('Matrix:')
print(matrix)

inv_mat = inv(matrix)
print('Inverse:')
print(inv_mat)
```

We could have imported all of **numpy** using `from numpy import *` but this is considered bad practice as it fills our 'namespace' with function names that might clash with other packages and it's less easy to parse which package's function is doing what. R also relies heavily on imported libraries but uses a different convention for namespaces: in that case, everything is imported but the *order* of package imports matters for what functions are default.

```{note}
If you want to check what packages you have installed in your Python environment, run `conda list` on the command line.
```

### Modules

Sometimes, you will want to call in some code from a different script. Imagine you have several code scripts (a, b, and c), all of which use the same underlying function that *you* have written. A central tenet of good coding is that you *do not repeat yourself*. Therefore, a bad solution to this problem would be to copy and paste the same code into all three of the scripts. A *good* solution is to write the code that's need just once in a separate 'utility' script and have the other scripts import that one function:

```{code-cell} ipython3
:tags: [remove-input]
import networkx as nx
import matplotlib.pyplot as plt
graph = nx.DiGraph()
graph.add_edges_from([("Utility script", "code file a"),
                      ("Utility script", "code file b"),
                      ("code file a", "code file c"),
                      ("code file b", "code file c"),
                      ("Utility script", "code file c")])
colour_node = '#AFCBFF'
fixed_pos = nx.spring_layout(graph, seed = 100)
nx.draw(graph, pos=fixed_pos, with_labels=True, node_size=5000, node_color=colour_node)
plt.xlim(-1.3, 1.3)
plt.ylim(-1.3, 1.3)
plt.show();
```

How would this work in practice? We would define a file 'utilities.py' that had the following:

```python
def really_useful_func(number):
    return number*10
```

Then, in 'code_script_a.py':

```{code-cell} ipython3
import utilities as utils

print(utils.really_useful_func(20))
```

An alternative is to *just* import the function we want, with the name we want:

```{code-cell} ipython3
from utilities import really_useful_func as ru_fn

print(ru_fn(30))
```

Another important example is the case where you want to run 'utilities.py' as a script, but still want to borrow functions from it to run in other scripts. There's a way to do this. Let's change utilities.py to

```python
def really_useful_func(number):
    return number*10


def default_func():
    print('Script has run')


if __name__ == '__main__':
    default_func()
```

What this says is that if we call 'utilities.py' from the command line, eg

```bash
python utilities.py
```

It will return `Script has run` because, by executing the script alone, we are asking for anything in the `main` block defined at the end of the file to be run. But we can still import anything from utilities into other scripts as before--and in this case it is not the main script, but an import, and so the `main` block will *not* be executed.

## Lambda functions

Lambda functions are a very old idea in programming, and part of the functional programming paradigm. Coding languages tend to be more object-oriented or functional, though high-level languages often mix both. For example, R leans slightly more toward being a functional language, while Python is slightly more object oriented. However, Python does have lambda functions, for example:

```{code-cell} ipython3
plus_one = lambda x: x+1
plus_one(3)
```

For a one-liner function that has a name it's actually better practice here to use `def plus_one(x): return x + 1`, so you shouldn't see this form of lambda function too much in the wild. However, you are likely to see lambda functions being used with dataframes and other objects. For example, if you had a dataframe with a column of string called 'strings' that you want to lower the case of and replace one phrase with another, you could use lambda functions to do that (there are better ways of doing this but this is useful as a simple example):

```{code-cell} ipython3
import pandas as pd
df = pd.DataFrame(data=[['hello my blah is Ada'], ['hElLo mY blah IS Adam']],
                  columns=['strings'],
                  dtype='string')
df['strings'].apply(lambda x: x.lower().title().replace('Blah', 'Name'))
```

More complex lambda functions can be constructed, eg `lambda x, y, z: x + y + z`. One of the best use cases of lambdas is when you *don't* want to go to the trouble of declaring a function. For example, let's say you want to compose a series of functions and you want to specify those functions in a list, one after the other. Using functions alone, you'd have to define a new function for each operation. With lambdas, it would look like this (again, there are easier ways to do this operation, but we'll use simple functions to demonstrate the principle):

```{code-cell} ipython3
number = 1
for func in [lambda x: x + 1, lambda x: x*2, lambda x: x**2]:
    number = func(number)
    print(number)
```

Note that people often use `x` by convention, but there's nothing to stop you writing `lambda horses: horses**2` (except the looks your co-authors will give you). If you want to learn more about lambda functions, check out these [short video tutorials](https://calmcode.io/lambda/introduction.html).

## Splat and splatty-splat

You read those right, yes. These are also known as unpacking operators for, respectively, arguments and dictionaries. For instance, if I have a function that takes two arguments I can send variables to it in different ways:

```{code-cell} ipython3

def add(a, b):
    return a + b

print(add(5, 10))

func_args = (6, 11)

print(add(*func_args))
```

The splat operator, `*`, unpacks the variable `func_args` into two different function arguments. Splatty-splat unpacks dictionaries into keyword arguments (aka kwargs):

```{code-cell} ipython3

def function_with_kwargs(a, x=0, y=0, z=0):
    return a + x + y + z

print(function_with_kwargs(5))

kwargs = {'x': 3, 'y': 4, 'z': 5}

print(function_with_kwargs(5, **kwargs))
```

Perhaps most surprisingly of all, we can use the splat operator *in the definition of a function*. For example:

```{code-cell} ipython3

def sum_elements(*elements):
    return sum(*elements)

nums = (1, 2, 3)

print(sum_elements(nums))

more_nums = (1, 2, 3, 4, 5)

print(sum_elements(more_nums))
```

To learn more about args and kwargs, check out these [short video tutorials](https://calmcode.io/args-kwargs/introduction.html).

## Miscellaneous fun

Here are some other bits of basic coding that might be useful. They really show why Python is such a delightful language.

You can use unicode characters for variables

```{code-cell} ipython3

α = 15
β = 30

print(α/β)
```

You can swap variables in a single assignment:

```{code-cell} ipython3
a = 10
b = 'This is a string'

a, b = b, a

print(a)
```

**iterools** offers counting, repeating, cycling, chaining, and slicing. Here's a cycling example that uses the `next` keyword to get the next iteraction:

```{code-cell} ipython3
from itertools import cycle

lorrys = ['red lorry', 'yellow lorry']
lorry_iter = cycle(lorrys)

print(next(lorry_iter))
print(next(lorry_iter))
print(next(lorry_iter))
```

**iterools** also offers products, combinations, combinations with replacement, and permutations. Here are the combinations of 'abc' of length 2:

```{code-cell} ipython3
from itertools import combinations
print(list(combinations('abc', 2)))
```

Find out what the date is! (Can pass a timezone as an argument.)

```{code-cell} ipython3
from datetime import date
print(date.today())
```

Because functions are just objects, you can iterate over them just like any other object:

```{code-cell} ipython3
functions = [str.isdigit, str.islower, str.isupper]

raw_str = 'asdfaa3fa'

for str_func in functions:
    print(f'Function name: {str_func.__name__}, value is:')
    print(str_func(raw_str))
```

Functions can be defined recursively. For instance, the Fibonacci sequence is defined such that $ a_n = a_{n-1} + a_{n-2} $ for $ n>1 $.

```{code-cell} ipython3
def fibonacci(n):
    if(n < 0):
        print('Please enter n>0')
        return 0
    elif(n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


[fibonacci(i) for i in range(10)]
```

This is just a taster of what can be done using 'batteries included' base Python; for more see the Advanced Coding Chapter.

## Review

If you now understand a bit about what objects, types, operators, conditional statements, loops, functions, and imports are, and *how* to use them, you are well on your way to becoming a coder. What you've seen in this chapter are the building blocks and you need to know a bit about them. But bricks by themselves do not a house make. In subsequent chapters, we'll see how to combine the elements here to do productive analysis in economics.
