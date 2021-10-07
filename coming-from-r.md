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
  display_name: 'Python 3.8.12 64-bit (''codeforecon'': conda)'
  language: python
  name: python3
---

# Coming from R

If you're coming from R, then you're probably already familiar with coding and with integrated developer environments. Overall, Python and R are more similar than they are different, especially when it comes to economics and data science.

There are, however, some fundamental differences between the two languages. The biggest difference between Python and R is that Python is a general purpose programming language, while R began as a statistical language. But you won't really notice this unless you're writing something that looks more like production-grade software. (And, despite being a general language, Python has really fantastic support for statistics.) A second difference is that Python is more object-oriented while R is more functional. These are two different programming paradigms. Actually, both languages do a bit of both and, again, you're unlikely to notice any difference most of the time.

Actually, the biggest practical difference I have found in an economics and data science context is that Python has more of a flavour of the bazaar--there are lots of people, and you can find everything under the Sun, but it can be a *little bit* chaotic--while R has the feel of a curated garden--there is a chief gardener (RStudio) tending a smaller number of more beautiful things, but the garden has boundaries.

There's a list of differences at the end of this chapter, but a couple of important gotchas to be aware of up front: first, R uses vectors, arrays, etc., that are indexed from 1. Like C++, Python is numbered from zero, with, eg, `a[0]` as the first element. Second, `<-` is the preferred assignment operator in R but in Python it's `=` (and `<-` isn't used). In fact, in R `a<-5` assigns `a` the value `5`, while `a<-5` in Python would return `True` or `False` based on whether `a` was less than `-5` or not!

## Tools similar to those found in an R workflow

If you are coming from R, you're likely familiar with **dplyr** for data analysis and **ggplot2** for plotting. There are Python equivalents that have very similar syntax to these that you can use to help you to become productive quickly in Python--though these libraries are not so popular in Python. Here are the Python equivalents to those R libraries:

- **dplyr**: This book recommends learning at least some [**pandas**](https://pandas.pydata.org/pandas-docs/stable/index.html) for data analysis in Python because it is a package that is comprehensive and ubiquitous, and it's the most popular Python library that performs similar functions to **dplyr**. **pandas** also has unrivaled documentation. However, if you want something closer to **dplyr** in terms of philosophy and syntax, there are a host of options available to you:
  - a Python package that is very similar to **dplyr** is [**plydata**](https://plydata.readthedocs.io/en/stable/index.html). It is created to be consistent with visualisation package **plotnine** (featured below).
  - another library that gets close to **dplylr** is [**datar**](https://github.com/pwwang/datar). Because it uses a consistent framework for data piping under the hood called [**pipda**](https://github.com/pwwang/pipda), **datar** seems highly extensible too. It also integrates with **plotnine** for visualisation.
  - [**siuba**](https://siuba.readthedocs.io/en/latest/) is a port of dplyr, tidyr, and other R libraries for data analysis.
  - [**dfplyr**](https://github.com/kieferk/dfply) is another attempt to replicate the syntax of **dplyr**, but it doesn't seem to be maintained.
  - [**pyjanitor**](https://ericmjl.github.io/pyjanitor/index.html) builds a range of extra features on top of **pandas**. Two of the things it adds are likely to make anyone coming from **dplyr** feel a bit more at home: better support for method chaining and some functions with the same names as the ones in **dplyr** and which do the same things.

- **ggplot2**: the most similar Python version of this library is [**plotnine**](https://plotnine.readthedocs.io/en/stable/index.html), while the most popular Python library that performs similar functions is a combination of [**matplolib**](https://matplotlib.org/) and [**seaborn**](https://seaborn.pydata.org/), which builds on **matplotlib**. I think either those two together or **plotnine** are good choices, though **plotnine**'s documentation is not (yet) as good and it's certainly not as widely used. (It's gaining popularity though.)

- **data.table**: if you use this library instead of **dplyr**, have no fear as there's an almost identical library in Python called [**datatable**](https://datatable.readthedocs.io/en/latest/). It's not nearly as popular in Python as **data.table** is in R, but it's a very high quality library.

- **here**: Lots of people switching from R to Python ask what the equivalent of the `here()` function is. The "best practice" answer is that you shouldn't need one! It's good practice to have your Visual Studio Code (or other IDE) console and interactive Python window automatically start *within* the directory of your project; that is, you should always be "here" automatically. In Visual Studio Code, you can ensure that the interactive window starts in the root directory of your project by setting "Jupyter: Notebook File Root" to "`${workspaceFolder}`" in the Settings menu. For the integrated command line, change "Terminal › Integrated: Cwd" to "`${workspaceFolder}`" too. If you still need a replacement for `here`, then the [pyprojroot](https://github.com/chendaniely/pyprojroot) package has you covered.

## Need a specific library that's in R but not in Python?

You can run a full R session from Python (if you already have R installed). Here's an example:

```python
import rpy2.robjects as ro
from rpy2.robjects.packages import importr

base = importr('base')

fit_full = ro.r("lm('mpg ~ wt + cyl', data=mtcars)")
print(base.summary(fit_full))
```

To install R packages, use this:

```python
from rpy2.robjects.packages import importr
utils = importr('utils')
utils.install_packages('packagename')
```

## R <==> Python

Here are some tables of translations between base R and Python code. For more, see [hyperpolyglot](https://hyperpolyglot.org/numerical-analysis).

### General

| R      | Python |
| ----------- | ----------- |
| <code> new_function <- function(a, b=5) { <br>return (a+b) <br>} </code>  | <code> def new_function(a, b=5): <br> &nbsp;&nbsp;&nbsp;&nbsp;return a+b </code> |
| <code> for (val in c(1,3,5)){ <br>  print(val) <br> } </code>  | <code> for val in [1,3,5]:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(val)</code>   |
| `a <- c(1,3,5,7)`   | `a = [1,3,5,7]`  |
| `a <- c(3:9)`   | `a = list(range(3,9))` |
| `class(a)`   | `type(a)`    |
| `a <- 5`   | `a = 5` |
| `a^2` | `a**2` |
| `a%%5` | `a%5`|
| `a & b` | `a and b` |
| `a | b` | `a or b` |
| `rev(a)` | `a[::-1]` |
| `a %*% b` | `a @ b` |
| `paste("one", "two", "three", sep="")` | `'one' + 'two' + 'three'` |
| `substr("hello", 1, 4)` | `'hello'[:4]` |
| `strsplit('foo,bar,baz', ',')` | `'foo,bar,baz'.split(',')` |
| `paste(c('foo', 'bar', 'baz'), collapse=',')` | `','.join(['foo', 'bar', 'baz'])` |
| `gsub("(^[\n\t ]+|[\n\t ]+$)", "", " foo ")` | `' foo '.strip()` |
| `sprintf("%10s", "lorem")` | `'lorem'.rjust(10)` |
| `paste("value: ", toString("8"))` | `'value: ' + str(8)` |
| `toupper("foo")` | `'foo'.upper()` |
| `nchar("hello")` | `len('hello')` |
| `substr("hello", 1, 1)` | `'hello'[0]` |
| `a = rbind(c(1, 2, 3), c('a', 'b', 'c'))` | `a = zip([1, 2, 3], ['a', 'b', 'c'])`|
| `d = list(n=10, avg=3.7, sd=0.4)` | `d = {'n': 10, 'avg': 3.7, 'sd': 0.4}` |
| `quit()` | `exit()`

### Dataframes

Assuming the use of **pandas** in Python, and the **dplyr** and **tidyr** packages in R.

| R      | Python |
| ----------- | ----------- |
| `head(df)` | `df.head()` |
| `tail(df)` | `df.tail()` |
| `nrow(df)`   | `df.shape[0]` or `len(df)` |
| `ncol(df)`   | `df.shape[1]` or `len(df.columns)` |
| `df$col_name` | `df['col_name']` or `df.col_name` |
| None  | `df.info()`    |
| `summary(df)`   | `df.describe()` (not exactly the same) |
| `df %>% arrange(c1, desc(c2))` | `df.sort_values(by=['c1','c2'], ascending=[True, False])` |
| `df %>% rename(new_col = old_col)` | `df.rename(columns={'old_col': 'new_col'}) ` |
| <code>df$smoker <- mapvalues(df$smoker,<br> &nbsp;from=c('yes', 'no'),<br>&nbsp;to=c(0,1))</code> | `df['smoker'] = df['smoker'].map({'yes':0, 'no':1})` |
| `df$c1 <- as.character(df$c1)` | `df['c1'] = df['c1'].astype(str)` |
|`unique(df$c1)` | `df['c1'].unique()` |
| `length(unique(df$c1))` | `len(df['c1'].unique())` |
| `max(df$c1,  na.rm = TRUE)` | `df['c1'].max()` |
| `df$c1[is.na(df$c1)] <- 0` | `df['c1'] = df['c1'].fillna(0)` |
|  <code>col_a <- c('a','b','c')<br>col_b <- c(1,2,3)<br>df <- data.frame(col_a, col_b)</code> | `df = pd.DataFrame(dict(col_a=['a', 'b', 'c'], col_b=[1, 2, 3]))` |
| <code> df <- read.csv("input.csv", <br>&nbsp; header = TRUE, <br> &nbsp; na.strings=c("","NA"), sep = ",")</code> | `df = pd.read_csv("input.csv")` |
| `write.csv(df, "output.csv", row.names = FALSE)` | `df.to_csv("output.csv", index = False)`|
| `df[c(4:6)]` | `df.iloc[:, 3:6]` |
| `mutate(df, c=a-b)` | `df.assign(c=df['a']-df['b'])` |
| `distinct(select(df, col1))` | `df[['col1']].drop_duplicates()`|

### Object types

| R      | Python |
| ----------- | ----------- |
| character | string, aka `str` |
| integer | integer, aka `int` |
| logical | boolean, aka `bool` |
| numeric | `float` or `double` |
| complex | `complex` |
| Single-element vector | Scalar |
| Multi-element vector | List |
| List of multiple types | Tuple |
| Named list | Dict |
| Matrix/Array | numpy ndarray |
| `NULL`, `TRUE`, `FALSE` | `None`, `True`, `False` |
| Inf | `inf` |
| NaN | `nan` |

### Other important differences

| R      | Python |
| ----------- | ----------- |
| `<-` works as an assignment operator | `=` is the assignment operator |
|Dots are valid in variable names, eg `var.iable` | Dots precede methods, eg `'  strip whitespace   '.strip()` |
| use of `$`, eg `df$col_name` | Equivalent is usually `.`, eg `df.col_name` |
| Does not have compound assignments | `+=`, `-=`, `*=`, etc. are compound assignment operators |
| `FALSE`, `F`, `0`, and `0.0` are false | `False`, `None`, `0`, `0.0`, `''`, `[]`, and `{}` are false|
| Tends to fail silently, eg `a = c()`, `a[10]` evaluates as NA | Python tends to fail loudly, eg `a=[]`, `a[10]` throws an error |
| No built-in decorator operator, but see [decorator](https://github.com/klmr/decorator) | Function decorator, `@` |
| Walrus operator, `:=`, used in quasiquations | Walrus operator, `=:`, combines an expression with an assignment (Python 3.8+) |
| Pipe operator, `%>%`  | No built-in pipe operator. Method chaining and `.pipe` used as partial replacements for dataframes, and there are pipe extensions like [pipetools](https://github.com/0101/pipetools) and [sspipe](https://sspipe.github.io/), but they're not widely used. |
