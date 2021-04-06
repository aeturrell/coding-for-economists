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

In this chapter, you'll learn about the basics of objects, types, operations, conditions, loops, functions, and imports. These are the basic building blocks of almost all programming languages.

This chapter has benefited from the excellent [*Python Programming for Data Science*](https://www.tomasbeuzen.com/python-programming-for-data-science/README.html) book by Tomas Beuzen.

```{admonition}
:class: tip
Remember, you can download this notebook (to run it on your own computer) using the 'download .ipynb' button at the top of the page.
```


## If you get stuck

It's worth saying at the outset that, *no-one*, and I mean no-one, memorises half of the stuff you'll see in this book. 80% or more of time spent programming is actually time spent looking up how to do this or that online, 'debugging' a code for errors, or testing code. This applies to all programmers, regardless of level. You are here to learn the skills and concepts of programming, not the precise syntax (which is easy to look up later).

![xkcd-what-did-you-see](https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png)

Knowing how to Google is one of the most important skills of any coder. No-one remembers every function from every library. Here are some useful coding resources:

- when you have an error, look on Stack Overflow to see if anyone else had the same error (they probably did) and how they overcame it.

- if you're having trouble navigating a new package or library, look up the documentation online. The best libraries put as much effort into documentation as they do the code base.

- use cheat sheets to get on top of a range of functionality quickly. For instance, this excellent (mostly) base Python [Cheat Sheet](https://gto76.github.io/python-cheatsheet/).

- if you're having a coding issue, take a walk to think about the problem, or explain your problem to an animal toy on your desk ([traditionally](https://en.wikipedia.org/wiki/Rubber_duck_debugging) a rubber duck, but other animals are available).

## Values, variables, and types

A value is datum such as a number or text. There are different types of values: 352.3 is known as a float or double, 22 is an integer, and "Hello World!" is a string. A variable is a name that refers to a value: you can think of a variable as a box that has a value, or multiple values, packed inside it. 

Almost word can be a variable name as long as it starts with a letter or an underscore, although there are some special keywords that can't be used because they already have a role in the Python language: these include `if`, `while`, `class`, and `lambda`.

Creating a variable in Python is achieved via an assignment (putting a value in the box), and this assignment is done via the `=` operator. The box, or variable, goes on the left while the value we wish to store appears on the right. It's simpler than it sounds:

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

It's the same thing but with a different **type** of data, a string instead of an integer. Python is *dynamically typed*, which means it will guess what type of variable you're creating as you create it. This has pros and cons, with the main pro being that it makes for more concise code.

```{admonition} Important
Everything is an object, and every object has a type.
```

The most basic built-in data types that you'll need to know about are: integers `10`, floats `1.23`, strings `like this`, booleans `True`, and nothing `None`. Python also has a built-in type called a list `[10, 15, 20]` that can contain anything, even *different* types. So

```{code-cell} ipython3
list_example = [10, 1.23, 'like this', True, None]
print(list_example)
```

is completely valid code. `None` is a special type of nothingness, and represents an object with no value. It has type `NoneType` and is more useful than you might think! 

As well as the built-in types, packages can define their own custom types. If you ever want to check the type of a Python variable, you can call the `type` function on it like so:

```{code-cell} ipython3
type(list_example)
```

This is especially useful for debugging `ValueError` messages.

Below is a table of common data types in Python:

| Name          | Type name  | Type Category  | Description                                   | Example                                    |
| :-------------------- | :--------- | :------------- | :-------------------------------------------- | :----------------------------------------- |
| integer               | `int`      | Numeric Type   | positive/negative whole numbers               | `22`                                       |
| floating point number | `float`    | Numeric Type   | real number in decimal form                   | `3.14159`                                  |
| boolean               | `bool`     | Boolean Values | true or false                                 | `True`                                     |
| string                | `str`      | Sequence Type  | text                                          | `"Hello World!"`                 |
| list                  | `list`     | Sequence Type  | a collection of objects - mutable & ordered   | `['text entry', True, 16]`               |
| tuple                 | `tuple`    | Sequence Type  | a collection of objects - immutable & ordered | `(51.02, -0.98)`                 |
| dictionary            | `dict`     | Mapping Type   | mapping of key-value pairs                    | `{'name':'Ada', 'subject':'computer science'}` |
| none                  | `NoneType` | Null Object    | represents no value                           | `None`                                     |
| function                  | `function` | Function   | Represents a function                           | `def add_one(x): return x+1`                                     |

### Brackets

You may notice that there are several kinds of brackets that appear in the code we've seen so far, including `[]`, `{}`, and `()`. These can play different roles depending on the context, but the most common uses are:

- `[]` is used to denote a list, eg `['a', 'b']`, or to signify accessing a position using an index, eg `vector[0]` to get the first entry of a variable called vector.

- `{}` is used to denote a set, eg `{'a', 'b'}`, or a dictionary (with pairs of terms), eg `{'first_letter': 'a', 'second_letter': 'b'}`.

- `()` is used to denote a tuple, eg `('a', 'b')`, or the arguments to a function, eg `function(x)` where `x` is the input passed to the function, *or* to indicate the order operations are carried out.

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

You can 

As well as accessing positions in lists using indexing, you can use *slices* on lists. This uses the colon character, `:`, to stand in for 'from the beginning' or 'until the end' (when only appearing once). For instance, to print just the last two entries, we would use the index `-2:` to mean from the second-to-last onwards. Here are two distinct examples: getting the first three and last three entries to be successively printed:

```{code-cell} ipython3
print(list_example[:3])
print(list_example[-3:])
```

Slicing can be even more elaborate than that because we can jump entries using a second colon. Here's a full example that begins at the second entry (remember the index starts at 0), runs up until the second-to-last entry (exclusive), and jumps every other entry inbetween (range just produces a list of integers from the value to one less than the last):

```{code-cell} ipython3
list_of_numbers = list(range(1, 11))
start = 1
stop = -1
step = 2
print(list_of_numbers[start:stop:step])
```

A handy trick is that you can print a reversed list entirely using double colons:

```{code-cell} ipython3
print(list_of_numbers[::-1])
```

What's amazing about lists is that they can hold any type, including other lists! Here's a valid example of a list that's got a lot going on:

```{code-cell} ipython3
wacky_list = [3.1415, 16, ["five", 4, 3], "Hello World!", True, None, {"key": "value", "key2": "value2"}]
wacky_list
```

Can you identify the types of each of the entries (and entries of entries)?

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

Below is a table of the basic arithmetic operations.

| Operator |   Description    |
| :------: | :--------------: |
|   `+`    |     addition     |
|   `-`    |   subtraction    |
|   `*`    |  multiplication  |
|   `/`    |     division     |
|   `**`   |  exponentiation  |
|   `//`   | integer division / floor division |
|   `%`    |      modulo      |
|   `@`    |     matrix multiplication |

As well as the usual operators, Python supports *assignment operators*. An example of one is `x+=3`, which is equivalent to running `x = x + 3`. Pretty much all of the operators can be used in this way.


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

Strings have type `string` and can be defined by single or double quotes, eg `string = "cheesecake"` would have been equally valid above.

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

Some of the most important operations you will perform are with `True` and `False` values, also known as boolean data types. There are two types of operation that are associated with booleans: boolean operations, in which existing booleans are combined, and condition operations, which create a boolean when executed.

Boolean operators that return booleans are as follows:

| Operator | Description |
| :---: | :--- |
|`x and y`| are `x` and `y` both True? |
|`x or y` | is at least one of `x` and `y` True? |
| `not x` | is `x` False? | 

These behave as you'd expect: `True and False` evaluates to `False`, while `True or False` evaluates to `True`. There's also the `not` keyword. For example

```{code-cell} ipython3
not True
```

as you would expect.

Conditions are expressions that evaluate as booleans. A simple example is `10 == 20`. The `==` is an operator that compares the objects on either side and returns `True` if they have the same *values*--though be careful using it with different data types.

Here's a table of conditions that return booleans:

| Operator  | Description                          |
| :-------- | :----------------------------------- |
| `x == y ` | is `x` equal to `y`?                 |
| `x != y`  | is `x` not equal to `y`?             |
| `x > y`   | is `x` greater than `y`?             |
| `x >= y`  | is `x` greater than or equal to `y`? |
| `x < y`   | is `x` less than `y`?                |
| `x <= y`  | is `x` less than or equal to `y`?    |
| `x is y`  | is `x` the same object as `y`?       |


As you can see from the table, the opposite of `==` is `!=`, which you can read as 'not equal to the value of'. Here's an example of `==`:

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

One nice feature of Python is that you can make multiple boolean comparisons in a single line.

```{code-cell} ipython3
a, b = 3, 6

1 < a < b < 20
```

## Casting variables

Sometimes we need to explicitly cast a value from one type to another. We can do this using functions like `str()`, `int()`, and `float()`. If you try these, Python will do its best to interpret the input and convert it to the output type you'd like and, if they can't, the code will throw a great big error.

Here's an example of casting a `float` as an `int`:

```{code-cell} ipython3
orig_number = 4.39898498
type(orig_number)
```

Now we cast it to an int:

```{code-cell} ipython3
mod_number = int(orig_number)
mod_number
```

which looks like it became an integer, but we can double check that:

```{code-cell} ipython3
type(mod_number)
```

## Tuples and (im)mutability

A tuple is an object that is defined by parentheses and entries that are separated by commas, for example `(15, 20, 32)`. (They are of type `tuple`.) As such, they have a lot in common with lists-but there's a big and important difference.

Tuples are immutable, while lists are mutable. This means that, once defined, we can always modify a list using slicing and indexing, e.g. to change the first entry of a list called `listy` we would use `listy[0] = 5`. But trying to do this with a tuple will result in an error.

*Immutable* objects, such as tuples, can't have their elements changed, appended, extended, or removed. Lists can do all of these things. Tuples aren't the only immutable objects in Python; strings are immutable too.

You may wonder why both are needed given lists seem to provide a superset of functionality: sometimes in coding, lack of flexibility is a *good* thing because it restricts the number of ways a process can go awry. I dare say there are other reasons too, but you don't need to worry about them and using lists is a good default most of the time.

## Indentation

You'll have seen that certain parts of the code examples are indented. Code that is part of a function, a conditional clause, or loop is indented. This isn't a code style choice, it's actually what tells the language that some code is to be executed as part of, say, a loop and not to executed after the loop is finished.

Here's a basic example of indentation as part of an `if` loop. The `print` statement that is indented only executes if the condition evaluates to true.

```{code-cell} ipython3
x = 10

if x > 2:
    print('x is greater than 2')
```

When functions, conditional clauses, or loops are combined together, they each cause an *increase* in the level of indentation. Here's a double indent.

```{code-cell} ipython3
if x > 2:
    print('outer conditional cause')
    for i in range(4):
        print('inner loop')
```

The standard practice for indentation is that each sub-statement should be indented by 4 spaces. It can be hard to keep track of these but, as usual, Visual Studio Code has you covered. Go to Settings (the cog in the bottom left-hand corner, then click Settings) and type 'Whitespace' into the search bar. Under 'Editor: Render Whitespace', select 'boundary'. This will show any whitespace that is more than one character long using faint grey dots. Each level of indentation in your Python code should now begin with four grey dots showing that it consists of four spaces. To make it even easier, you can install the 'indent-rainbow' extension in VS Code-this shows different levels of indentation in different colours.

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

Remember, Python indexes from 0 so the first entry of `i` will be zero. But, if you'd like to index from a different number, you can:

```{code-cell} ipython3
for i, name in enumerate(name_list, start=1):
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

The `zip` keyword is doing this magic; think of it like a zipper, bringing an element of each list together in turn. It can also be used directly in a for loop:

```{code-cell} ipython3
for first_nm, last_nm in zip(first_names, last_names):
    print(first_nm, last_nm)
```

Finally, an even more extreme use of list comprehensions can deliver nested structures:

```{code-cell} ipython3
first_names = ['Ada', 'Adam']
last_names = ['Lovelace', 'Smith']
names_list = [[x + ' ' + y for x in first_names] for y in last_names]
print(names_list)
```

This gives a nested structure that (in this case) iterates over `first_names` first, and then `last_names`. If you'd like to learn more about list comprehensions, check out these [short video tutorials](https://calmcode.io/comprehensions/introduction.html).

## While loops

`while` loops continue to execute code until their conditional expression evaluates to `False`. (Of course, if it evaluates to `True` forever, your code will just continue to execute...)


```{code-cell} ipython3
n = 10
while n > 0:
    print(n)
    n -= 1

print('execution complete')
```

NB: in case you're wondering what `-=` does, it's a compound assignment that sets the left-hand side equal to the left-hand side minus the right-hand side.

You can use the keyword `break` to break out of a while loop, for example if it's reached a certain number of iterations without converging.

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

## Running on empty

Being able to create empty containers is sometimes useful. The commands to create empty lists, tuples, dictionaries, and sets are `lst = []`, `tup=()`, `dic={}`, and `st = set()` respectively.

## Functions

If you're an economist, I hardly need to tell you what a function is. In coding, it's much the same as in mathematics: a function has inputs, it performs its function, and it returns any outputs. Functions begin with a `def` keyword for 'define a function'. It then has a name, followed by brackets, `()`, which may contain *function arguments* and *function keyword arguments*. The body of the function is then indented relative to the left-most text. Function arguments are defined in brackets following the name, with different inputs separated by commas. Any outputs are given with the `return` keyword, again with different variables separated by commas. Let's see a very simple example:

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

## Scope

Scope refers to what parts of your code can see what other parts. If you define a variable inside a function, the rest of your code won't be able to 'see' it or use it. For example, here's a function that creates a variable and then an example of calling that variable:

```python
def var_func():
    str_variable = 'Hello World!'

var_func()
print(str_variable)
```

This would raise an error, because as far as your general code is concerned `str_variable` doesn't exist outside of the function. If you want to create variables inside a function and have them persist, you need to explicitly pass them out using, for example `return str_variable` like this:

```{code-cell} ipython3
def var_func():
    str_variable = 'Hello World!'
    return str_variable

returned_var = var_func()
print(returned_var)
```

Or, if you only want to modify a variable, you can declare the variable before the function is run, pass it into the function, and then return it.


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
# Contents of utilities.py file
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
# Contents of utilities.py file
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

It will return `Script has run` because, by executing the script alone, we are asking for anything in the `main` block defined at the end of the file to be run. But we can still import anything from utilities into other scripts as before--and in that case it is not the main script, but an import, and so the `main` block will *not* be executed.

You can important several functions at once from a module (aka another script file) like this:

```python
from utilities import really_useful_func, default_func
```

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

## Time

Let's do a quick dive into how to deal with dates and times. This is only going to scratch the surface, but should give a sense of what's possible.

The built-in library that deals with datetimes is called `datetime`. Let's import it and ask it to give us a very precise account of the datetime (when the code is executed):


```{code-cell} ipython3
from datetime import datetime
now = datetime.now()
print(now)
```

You can pick out bits of the datetime that you need:

```{code-cell} ipython3
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
print(f'{year}/{month}/{day}, {hour}:{minute}')
```

To add or subtract time to a datetime, use `timedelta`:

```{code-cell} ipython3
from datetime import timedelta

new_time = now + timedelta(days=365, hours=5)
print(new_time)
```

To take the difference of two dates:

```{code-cell} ipython3
from datetime import date

new_year = date(year=2022, month=1, day=1)
time_till_ny = new_year - date.today()
print(f'{time_till_ny.days} days until New Year')
```

Note that date and datetime are two different types of objects-a datetime includes information on the date and time, whereas a date does not.

## Reading and writing files

Although most applications in economics will probably use the **pandas** package to read and write tabular data, it's sometimes useful to know how to read and write arbitrary files using the built-in Python libraries too. To open a file

```python
open('filename', mode)
```

where `mode` could be `r` for read, `a` for append, `w` for write, and `x` to create a file. Create a file called `text_example.txt` and write a single line in it, 'hello world'. To open the file and print the text, use:

```python
with open('text_example.txt') as f:
    text_in = f.read()

print(text_in)
```

```python
'hello world!\n'
```

`\n` is the new line character. Now let's try adding a line to the file:

```python
with open('text_example.txt', 'a') as f:
    f.write('this is another line\n')
```

Writing and reading files using the `with` command is a quick and convenient shorthand for the less concise open, action, close pattern. For example, the above example can also be written as:

```python
f = open('text_example.txt', 'a')
f.write('this is another line\n')
f.close()
```

Although this short example shows opening and writing a text file, this approach can be used to edit a wide range of file extensions including .json, .xml, .csv, .tsv, and many more, including binary files in addition to plain text files.

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
