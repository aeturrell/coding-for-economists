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

# Sharing Data

There are many times when you want to share data with a much wider audience. In this chapter, we'll find out about some ways to share data in ways that are *fast*, *easy for users*, and follow *best practices*. Because it's by far the most common case, we'll focus on sharing *tabular data*.

When might you want to share your data? If you've just finished writing a paper, you might want to share derived series; perhaps the data are the result of the paper if you're working in a field such as economic history. If you're working at a firm or in the public sector, perhaps there are datasets that you've decided to put out into the public domain and you want a cost effective way to share them. Perhaps you've got a slightly larger or more complex dataset that you'd like to put online, password protected, for a large number of co-authors.

## Datasette for sharing data

[Datasette](https://datasette.io/) is an extraordinary tool for exploring, sharing, and publishing data. It helps you take data of any shape or size, analyze and explore it, and publish it as an interactive website and accompanying API. Remember, API stands for application programming interface, which in this case means the data can be accessed directly through programming languages.

Datasette is aimed at data journalists, museum curators, archivists, local governments, *economists*, and anyone else who has data that they wish to share with the world.

An example datasette instance is [available here](https://global-power-plants.datasettes.com/); it shows a dataset of power stations.

So, how does it work? Let's assume you have some data in a CSV file. The first step in creating a datasette website is to turn that CSV file into a SQL-lite database (don't worry if you don't know what that is). The second step is to publish the data either *locally* (on your own computer) or on the internet (using a cloud service provider). Once the data are published, you and/or others can interact with them in several different ways.

To use datasette, you'll need a Python installation. Then, to install the datasette package run

```python
pip install csvs-to-sqlite datasette 
```

on the command line. To convert a CSV file called `data.csv` into a SQL-lite database (extension .db), use

```bash
csvs-to-sqlite data.csv data.db
```

on the command line.

### Run locally

To run the data as an interactive website on your own computer, use

```bash
datasette data.db
```

on the command line. You should see a browser link appear; click it to start interactively exploring your data!

### Run on the web

There are many different cloud providers for datasettes but here we'll focus on using Google Cloud Platform (GCP), specifically the Cloud Run service. To run a datasette instance on the web, you will need a GCP account with Cloud Run enabled. You will need to pay to run a datasette instance on Cloud Run, but there is a free tier covering, at the time of writing, the first 180,000 CPU-seconds per month and 2 million requests per month. Note that cloud run only counts time when an instance is serving users.

To launch your dataset on the web as a *datasette*, install and configure the Google Cloud Command Line Interface tools by following the instructions [here](https://cloud.google.com/sdk/). Then run

```bash
datasette publish cloudrun data.db --service=mydata
```

This will create a docker container and deploy it to the Cloud Run service. You may be prompted to give a preferred region. Once it's ready, a website URL will appear: this is your data being served up on the web!

### Here's one I made earlier

If you want to follow a full example of serving up data end-to-end, take a look at the [particulate matter datasette](https://github.com/aeturrell/datasette_particulate_matter) github repo. These data were constructed by downloading files of estimates of 2.5 micron particulate matter concentration in the UK from the DEFRA website and combining them into a CSV.

**You can see how the data in this repo get served up by datasette at [this link](https://particulatematter-fsx2r7puuq-nw.a.run.app/).**

### Benefits of datasette

[**datasette**](https://datasette.io/) is an extremely quick and cost-efficient way to serve up large datasets to anyone with an internet connection. The full utility comes from the ways that people can then use the data. Using the particulate matter example from the previous section, people can:

- Manually browse the data, making cuts by choosing from the filtering options or editing the equivalent SQL code.

- Manually download the data (and cuts thereof) as CSV or JSON files.

- Once data are filtered, copy the generated SQL code to reproduce the same filters programmatically in future. (This makes getting certain cuts *reproducible* for users.)

- Programmatically download cuts of the data using the generated CSV, SQL, or JSON endpoints. For example, to get the anthropogenic numbers for Southwark in 2018 from the particulate matter datasette instance:
  - CSV, `df = pd.read_csv("https://particulatematter-fsx2r7puuq-nw.a.run.app/uk_particulate_matter.csv?sql=select+rowid%2C+local_authority_code%2C+pm_anthropogenic%2C+pm_total%2C+pm_non_anthropogenic%2C+local_authority_name%2C+year%2C+region%2C+country+from+uk_particulate_matter+where+%22local_authority_name%22+like+%3Ap0+and+%22year%22+%3D+%3Ap1+order+by+rowid+limit+101&p0=%25southwark%25&p1=2018&_size=max")`
  - SQL,`select rowid, local_authority_code, pm_anthropogenic, pm_total, pm_non_anthropogenic, local_authority_name, year, region, country from uk_particulate_matter where "local_authority_name" like '%southwark%' and "year" = '2018' order by rowid limit 101`
  - JSON, `df = pd.read_json("https://particulatematter-fsx2r7puuq-nw.a.run.app/uk_particulate_matter/uk_particulate_matter.json?_sort=rowid&local_authority_name__contains=southwark&year__exact=2018&_shape=array")`

- By integrating with github or other tools, datasette can be automated so that when the raw data change, the instance being served online is updated too. (For an example github action that does this, [see here](https://github.com/simonw/global-power-plants-datasette/actions/runs/843939473/workflow).)

- If you are building dashboards that are also deployed on the web, you can use a datasette website as the back-end to serve up the data to the dashboard (making use of the automatic API features of datasette).

Publishing data with datasette is *fast*: we only needed a CSV file and a couple of commands. It's also *easy for end users* who can access the data via a website and filter it or download it however they like, and access it both manually and programmatically. By having several options to access data, by allowing users to filter to just the data they need, and by allowing for the inclusion of [metadata](https://docs.datasette.io/en/latest/metadata.html) and information [on units](https://docs.datasette.io/en/latest/metadata.html#specifying-units-for-a-column), datasette also makes it easier to follow *best practices*.

Datasette also has add-ons that provide extra support for geospatial data, password protection, and more; see the [plug-ins](https://datasette.io/plugins) page.

The *downsides* of datasette are that you have to pay to serve up the data (at least if it becomes very popular) and that it is built around *tabular data*.
