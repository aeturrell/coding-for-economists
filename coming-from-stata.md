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

# Coming from Stata

This chapter has benefitted enormously from [Daniel M. Sullivan's](http://www.danielmsullivan.com/pages/tutorial_stata_to_python.html) excellent notes.

The biggest difference between Python and Stata is that Python is a fully-fledged programming language, which means it can do *lots* of things, while Stata is really just for data analysis. What this means in practice is that sometimes the notation to do this or that operation in Python (or any other general purpose programming language) is less concise than in Stata. There is greater competition for each command in Python because it does many more things.

Another difference is that, in Stata, there is one dataset in memory that is represented as matrix where each column is a "variable" with a unique name. In Python, variables can be anything, even functions! But most data analysis in Python is done using dataframes, which are objects that are somewhat similar to a single dataset in Stata. In Python, you can have as many DataFrames as you like in action at once. This causes the first major notational differences; in Python, you need to specify *which* dataframe you want to perform an operation on, in addition to which column (or row, or entry).

Finally, Python and its data analysis packages are free.

Regardless of Python not being a programming language solely dedicated to data analysis, it really does have first class support for data analysis via its **pandas** package.

## Stata <==> Python

What follows is a giant table of translations between Stata code and Python's [**pandas**](https://pandas.pydata.org/)(panel-data-analysis) package. The econometrics examples below use Daniel M Sullivan's [**econtools**](https://www.danielmsullivan.com/econtools/metrics.html) package, but you could also use [**statsmodels**](https://www.statsmodels.org/). Bear in mind, it's certainly not meant to be exhaustive but it should give you a flavour of the syntax differences and, in some cases, I've pointed out where to find further information.

Following Daniel's treatment, the Stata-to-Python translations assume that, in Python, you have a **pandas** DataFrame called `df`. We will use placeholders like `varname` for Stata variables and `df['varname']` for the Python equivalent. Remember that you need to `import pandas as pd` before running any of the examples that use `pd`. For the econometrics examples, you will need `import econtools.metrics as mt`.

| Stata      | Python (pandas) |
| ----------- | ----------- |
| `help command`      | `help(command)`       |
| `cd directory`   | <code>import os<br>os.chdir('directory') </code> <br> Best practice: don't do this; bring the data to you!        |
| `use dtafile`   | `df = pd.read_stata('dtafile')`       |
| `use varlist using dtafile`   | <code>df = pd.read_stata('dtafile', columns=varlist) </code>       |
| `import excel using excelfile`   | <code>df = pd.read_excel('excelfile') </code>       |
| `import delimited using csvfile`   | <code>df = pd.read_csv('csvfile') </code>       |
| `save filename, replace`   | <code>df.to_stata('filename') </code> <br> Best practice: don't save data in .dta files.       |
| `outsheet using filename, comma`   | <code>df.to_csv('filename') </code> |
| `export excel using filename`   | <code>df.to_excel('filename') </code> <br> Best practice: don't save data in Excel files.       |
| `keep if condition`   | `df = df[condition]`      |
| `drop if condition`   | `df = df[~condition]`      |
| `keep variable`   | `df = df['variable']`      |
| `keep varstem*`   | `df = df.filter(like='varstem*')`      |
| `drop variable`   | `df = df.drop('variable', axis=1)`      |
| `drop varstem*`   | `df = df.drop(df.filter(like='varstem*').columns, axis=1)`      |
| `describe`   | `df.info()`      |
| `describe variable`   | `df['variable'].dtype`      |
| `count`   | `len(df)`      |
| `count if condition`   | `df[condition].shape[0]`      |
| `summ variable`   | `df['variable'].describe()`      |
| `summ variable if condition`   | `df.loc[condition, 'variable'].describe()`      |
| `gen newvar = expression`   | `df['newvar'] = expression`      |
| `gen newvar = expression if condition`   | `df.loc[condition, 'newvar'] = expression`      |
| `replace newvar = expression if condition`   | `df.loc[condition, 'newvar'] = expression`      |
| `rename var newvar`   | `df = df.rename(columns={var: newvar})` or `df.columns=list_new_columns`      |
| `subinstr(string, " ", "_", .)`   | `df['var'].str.replace(' ', '_')`      |
| `egen newvar = statistic(var), by(groupvars)`   | `df['newvar'] = df.groupby(groupvars)['var'].transform('statistic')`      |
| `collapse (sd) var (median) var (max) var (min) <var>, by(groupvars)`   | `df.groupby(groupvars)['var'].agg(['std', 'median', 'min', 'max', 'sum'])`      |
| `collapse (sd) var (median) var (max) var (min) <var>, by(groupvars)`   | `df.groupby(groupvars)['var'].agg(['std', 'median', 'min', 'max', 'sum'])`      |
| `append using filename`  | `df = df1.append(df2)`      |
| `merge 1:1 vars using filename`  | `df = pd.merge(df1, df2, on=vars)` but there are very rich options for merging dataframes (Python is similar to SQL in this respect) and you should check the [full documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html).     |
| `reshape <wide/long> <stubs>, i(<vars>) j(<var>)`  | **pandas** has several reshaping functions, including `df.unstack('level')` for going to wide, `df.stack('column_level')` for going to long, `pd.melt`, and `df.pivot`. It's best to check the excellent [reshaping](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html) documentation to find what best suits your needs.    |
| `xi: i.var`  | `pd.get_dummies(df['var'])`|
| `reg yvar xvar if condition, r`  | <code>import econtools.metrics as mt<br> results = mt.reg(df[condition], 'yvar', 'xvar', robust=True) </code> |
| `reg yvar xvar if condition, vce(cluster clustervar)`  | `results = mt.reg(df[condition], 'yvar', 'xvar', cluster='clustervar')` |
| `reg yvar xvar if condition, vce(cluster clustervar)`  | `results = mt.reg(df[condition], 'yvar', 'xvar', cluster='clustervar')` |
| `areg yvar xvar, absorb(fe_var)`  | `results = mt.reg(df, 'yvar', 'xvar', a_name=fe_var)` |
| `predict newvar, resid`  | `newvar = results.resid` |
| `predict newvar, xb`  | `newvar = results.yhat` |
| `_b[var], _se[var]`  | `results.beta['var'], results.se['var']` |
| `test varlist`  | `results.Ftest(varlist)` |
| `test varlist, equal`  | `results.Ftest(varlist, equal=True)` |
| `ivreg2`  | `mt.ivreg` |
| `outreg2`  | `econtools.outreg` |
| `binscatter`  | `econtools.binscatter` |
| `twoway scatter var1 var2`  | `df.scatter(var2, var1)` |
