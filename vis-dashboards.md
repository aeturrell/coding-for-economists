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
  display_name: 'Python 3.10.12 64-bit (''codeforecon'': conda)'
  language: python
  name: python3
---
(dashboards)=
# Dashboards

In this chapter, you'll see how to get started with creating your very own dashboards. While there are a few tools for creating dashboards in Python, we'll focus on one of the simplest and easiest options, a tool called [**streamlit**](https://streamlit.io/).

## Introduction

Dashboards provide a visual representation of data that is interactive and/or updated as the underlying data source changes. Their main purpose is to deliver insights to their users, usually via a web page (which can be private or public). Sometimes, they also provide convenient and programmatic access to the data that supports them. An excellent example is the [UK's coronavirus dashboard](https://coronavirus.data.gov.uk/) from Public Health England.

It's worth being aware that dashboards provoke strong feelings, so we'll explore the pros and cons of them in this chapter too.

What might you use a dashboard for? Here are some classic use cases (not mutually exclusive):

- Business metrics and monitoring
- Dissemination of information in real time
- Providing an interactive way to vary assumptions behind a model
- Dissemination of complex information to non-expert audiences
- Provide access to a wide range of disparate but related data or analysis

When considering whether to create a dashboard, it's important to bear in mind some of their failure modes. Indeed, dashboards have had a [lot of criticism](https://towardsdatascience.com/dashboards-are-dead-b9f12eeb2ad2) from the analytical community, and there's a lot of [intelligent discussion](https://www.getdbt.com/blog/are-dashboards-dead/) of the pros and cons. The criticism usually falls along the following lines:

- They are mistakenly used as a replacement for access to the underlying data, but can never provide the level of flexibility needed to run all queries users could possibly want. Comments like, "After a dashboard had gone live, we were immediately flooded with requests for new views, filters, fields, pages, everything" are common. Effectively, they cannot anticipate all users' needs.
- They don’t have the transparency of a traditional database query, so users cannot have trust in what they see.
- They are hard to maintain (especially historically, when the tools were less easy to use) so the up-front costs of development are never paid back and legacy dashboards that no longer have value can proliferate. The difficulty in maintaining them is both due to factors like the original creator moving job leaving an impenetrable code behind, and organisations not always have the institutional capital to maintain dashboards in perpetuity.
- They often do not meet the strictest standards of accessibility—a problem that stands today.
- They can encourage people to chase metrics, which is unwise, as famously captured by (economist and former Bank of England Monetary Policy Committee member) Charles Goodhart in what is known as Goodhart's law: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."

This book is somewhat sceptical of dashboards. Often, a report or one-off analysis that can be put up as a static webpage or circulated via email can cover the same need with less fuss. Those problems of maintainability can be very real.

So, depending on the need and 'user stories', good alternatives to dashboards might be notebooks, automated static reports, or static webpages; there's information elsewhere in this book on all of those.

However, dashboards they do have their place, especially when:

- The metrics and visualisations needed are unlikely to change frequently.
- Interactivity is useful, rather than a distraction (there is a trade-off between interactivity and analytical storytelling).
- The data are changing over time.
- A wide range of information brought together in one place will be more informative than the same information analysed separately.
- You are conveying information to users who are not able to use the data directly.

These are, unsurprisingly, similar to the use cases above.

## Getting Started with Dashboards

### Streamlit

We'll be using [**streamlit**](https://streamlit.io/), which is relatively powerful but perhaps the most simple dashboarding tool there is, and so has a high return on investment. Other tools like [**dash**](https://plotly.com/dash/) are probably more popular in enterprise environments and can be better for accessibility, certainly at the time of writing, but streamlit can do a lot and, as well as being easy to write, it's also easy to deploy.

You can find a gallery of very good dashboards over at [awesome streamlit](http://awesome-streamlit.org/) or at the official streamlit [gallery](https://streamlit.io/gallery).

### Hello World in Streamlit

In this section, we're going to see how to create a simple dashboard and view it locally on your computer.

First up, note that the code needed for different dashboard tools is bespoke so although some of the ideas (eg of widgets) are translatable across different dashboarding solutions, much of the syntax is not. But you do get the gist from having tried out one of the many dashboarding solutions out there.

First, you'll need to install streamlit into your Python environment. As ever, it's a good idea to use an isolated Python environment for each project you do. To install streamlit, enter `pip install streamlit` into the command line with your Python environment activated.

Next, you'll need to create a new Python script. Name the new script what you like, but we'll assume you've called it `app.py`. Within the script, enter the following:

```python
import streamlit as st

st.title("My first dashboard")
st.write("Hello World!")
```

Now, open the command line (remember there's an integrated command line in Visual Studio Code—see the chapter on {ref}`wrkflow-command-line` for more) and (with the relevant Python environment activated) type

```bash
streamlit run app.py
```

You should see a message saying "You can now view your Streamlit app in your browser" followed by a link within your terminal. Click on that link and you will be transported to a browser window with your very first, rather sparse, dashboard!

Notice that the elements appear in the order that they are written in the script. This is generally true of streamlit components, though [more complex layouts](https://docs.streamlit.io/library/api-reference/layout) are possible: for example, expandables, sidebars, and columns.

As we take this simple dashboard and add more features, if you kept your app running in the command line you should be able to just go back to the browser window showing the app and hit the 'rerun' button to update what is displayed.

### Text, Data, and Visualisations

There are a large number of "widgets" or "components" available that offer different functionality. You can find a full list of all the widgets [here](https://docs.streamlit.io/library/api-reference). You've already seen two widgets that [add text](https://docs.streamlit.io/library/api-reference/text). Three extra text widgets that are useful are `st.markdown`, `st.latex`, and `st.code`. For example, to add some latex to the page, it would be

```python
st.latex(r"Y = \beta_0 + \beta_1X + \varepsilon")
```

where the latex string is preceded by "r" to tell Python to treat it as a raw string; necessary because otherwise the backslashes would be interpreted as escape characters.

You may also find yourself wanting to display numerical or other values directly in a table. There are multiple ways to do this using **pandas** dataframes as the underlying data structure. For example, `st.dataframe` displays a dataframe. If you're going for a sharp dashboard with key metrics on, there's a widget for creating the numerical equivalent of a pull-quote in a newspaper article. The following code lays out three metrics in a row when used in a script.

```python
col1, col2, col3 = st.columns(3)
col1.metric("Temperature","70 °F","1.2 °F")
col2.metric("Wind","9 mph","-8%")
col3.metric("Humidity","86%","4%")
```

Let's move on now to visualisations. Streamlit supports a wide range of visualisation options, including packages such as **altair**, **matplotlib**, **plotly**, **bokeh**, and even graph viz (a tool used to draw directed cyclic graphs). Because they are so widely used for dashboards, we'll look at visualisations using **matplotlib**, **altair**, and **plotly**. The functional form of the command used to display a chart is going to be similar in each case, along the lines of `st.method(chart object)`.

First, we need some data to visualise though. Let's create some.

```python
seed_for_prng = 78557
prng = np.random.default_rng(seed_for_prng)  # prng=probabilistic random number generator
x = np.linspace(0, 8, 16)
y1 = 3 + 4*x/8 + prng.uniform(0.0, 0.5, len(x))
y2 = 1 + 2*x/8 + prng.uniform(0.0, 0.5, len(x))
```

Here's an example of a chart of this data using **matplotlib**. Within your script, create the chart using the code almost as normal. The only difference is that to display the created chart you'll need to use the special method `st.pyplot`.

```python
# usual code for plot
fig, ax = plt.subplots()
ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, (y1 + y2)/2, linewidth=2)
ax.set_title("Chart with forecast bands", loc="left")
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax.set_xlabel("Time")
ax.set_ylabel("Value")
# Show the chart on the streamlit dashboard
st.pyplot(fig)
```

Now let's look at the plotting library **altair**, which is particularly well-suited to dashboards and live web elements. You'll need to have the **altair** package installed to run this. Note that the tooltip option makes the chart interactive, while the `use_container_width=True` option changes the size of the figure to fit the streamlit container that it's in. All of the usual interactivity available in this package works. There are some other nice features too, like providing users with an easy way to save the figure in png or svg. **altair** works less well with large datasets though.

```python
df = pd.DataFrame(
     prng.standard_normal(size=(200, 3)),
     columns=['a', 'b', 'c'])
alt_chart = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
     )
st.altair_chart(alt_chart, use_container_width=True)
```

Finally, let's try **plotly**, which also has interactivity built-in.

```python
import plotly.express as px
df = px.data.iris()
pxfig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
st.plotly_chart(pxfig, use_container_width=True)
```

### Interactivity

Although we've already seen built-in interactivity via a couple of the chart packages, there is a much deeper level of interactivity available in **streamlit**. It's possible to build anything from an almost static report with a few fixed options implemented via radio buttons all the way to something as complex as a game (eg a treasure hunt where each correct input unlocks the next stage). You are really only limited by your own creativity!

What's quite amazing is how simple this interactivity is to implement. For example, a button that displays a message is clicked into the 'on' position is as simple as:

```python
if st.button('Say Hello'):
    st.write('Hello!')
```

There's some magic going on here: if a user clicks the button marked "Say Hello" then `st.button("Say Hello")` returns true and `st.write("Hello!")` is executed. While this is a simple example, you could execute anything in that block.

That's quite a simple and straightforward case; what if there are multiple options? Radio buttons offer several different options at once and have the syntax, `st.radio(question, list or pandas series of categories)`. For example:

```python

genre = st.radio(
     "What's your favourite movie genre",
     ('Comedy', 'Drama', 'Documentary'))
if genre == (answer := 'Comedy'):
    st.write(f'You selected {answer}.')
elif genre == (answer := 'Drama'):
    st.write(f'You selected {answer}.')
else:
    st.write("You didn't select comedy or drama.")
```

Note how the value of the `genre` variable is available after the radio function is run, and how it can then be used in other subsequent steps. (Note that the syntax `answer := 'comedy'` is known as the Walrus operator or an assignment expression: it combines assignment with an expression.)

There are lots of different input widgets that provide interactivity. A few of those that are available are:

- Download Button
- Checkbox
- Select box
- Multi-select
- Slider
- Free text input
- Number
- Date
- Image upload
- File upload
- custom widgets made by other users, eg [timelines](https://github.com/giswqs/streamlit-timeline) ()

To give you some ideas of how you might use some of these elements, you could:

- Use a multi-select box to decide what sectors to include in a stacked area chart of output
- Use a checkbox to switch between linear and log scales
- Use the file upload to get users to upload data which is then used to make a forecast, which users can then download using the download button.

We're not going to cover this in detail (check out the excellent [documentation](https://docs.streamlit.io/library/api-reference) for further information), but there is also functionality within **streamlit** dashboards for:

- audio
- viewing images
- video
- persisting state across re-runs for each user session
- caching results from 'expensive' functions
- [theming](https://docs.streamlit.io/library/advanced-features/theming) the dashboard with different colours

## Deploying a Dashboard

The real value of a dashboard can only be unlocked if other people can access it too, and this means 'serving' it not just on your local laptop but on the internet (or private office network). Serving up a dashboard on the internet is the most common use case. For this, you need a service that will 'host' your dashboard: a service that runs the code on their servers and provides a URL where anyone can see it (or a select few in the case of a private dashboard).

Streamlit the company (who make the package) offer free hosting for some dashboards, at least at the time of writing. The easiest way to deploy using their hosting service is to create a github repository with your code in a file called `app.py` along with a reproducible package file such as a requirements.txt or an environment.yml if you're using the Anaconda distribution of Python (which this book uses throughout). You can find out more about environment.yml files in the chapter on {ref}`wrkflow-environments`.

Once your app is written, head to the [streamlit cloud](https://docs.streamlit.io/streamlit-cloud) documentation and follow the instructions to launch an app. Typically, the process will be to create an account with streamlit the company, point them at the GitHub repo that contains the code you'd like to deploy, and then hit 'go!'.

If you would prefer another deployment solution, there are plenty of others; for example, Google App Engine, Heroku, and Azure.

## See Also

**streamlit** is not the only option for building dashboards.

A really good alternative choice, which has some purported advantages, is [Shiny for Python](https://shiny.posit.co/py/). Shiny began as the most popular dashboard solution in the popular statistical programming language R, but is now available for Python too, and its creators have moved it on a lot in a very short space of time: well worth checking out.

Another alternative is [**Dash**](https://plotly.com/dash/), made by Plotly. It supports Python and R. Dash has a steeper learning curve than streamlit but offers more customisation in style in return. You can find a Plotly tutorial [here](https://dash.plotly.com/introduction), or a tutorial on RealPython [here](https://realpython.com/python-dash/). There are further resources over at [**awesome dash**](https://github.com/ucg8j/awesome-dash).

Yet another Python dashboarding solution is [**Panel**](https://panel.holoviz.org/), for which you can find examples over at [**awesome panel**](https://awesome-panel.org/gallery).
