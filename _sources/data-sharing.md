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

(data-sharing)=
# Sharing Data

There are many times when you want to share data with a much wider audience. In this chapter, we'll find out about some ways to share data in ways that are *fast*, *easy for users*, and follow *best practices*. Because it's by far the most common case, we'll focus on sharing *tabular data*.

When might you want to share your data? If you've just finished writing a paper, you might want to share derived series; perhaps the data are the result of the paper if you're working in a field such as economic history. If you're working at a firm or in the public sector, perhaps there are datasets that you've decided to put out into the public domain and you want a cost effective way to share them. Perhaps you've got a slightly larger or more complex dataset that you'd like to put online, password protected, for a large number of co-authors.

One part of best practice when sharing data is following the FAIR principles:

- Findable: The first step in allowing people to re-use data is for those people to be able to find them. Metadata and data should be easy to find for both humans and computers. This includes registering data (and meta-data) in a searchable source.

- Accessible: Once a user finds the required data, they need to know how those data can accessed, possibly including authentication and authorisation. So the data should be retrievable by their identifiers using a standardised protocol that is open, free, and universally implementable.

- Interoperable: The data usually need to be integrated with other data. In addition, the data need to interoperate with applications or workflows for analysis, storage, and processing.  Although there are free tools to open Excel and Stata files, data stored in those formats are that bit more difficult than truly open formats like CSV or parquet. Universally implementable means that Python's pickle format or R's .rds format shouldn't be used to share data either. Interoperability means using open formats that can be accessed using free tools across different languages and operating systems.

- Reusable: The ultimate goal of FAIR is to optimise the reuse of data. To achieve this, metadata and data should be well-described so that they can be replicated and/or combined in different settings.

Different ways of sharing data are inevitably better or worse across the four principles.

Another part of best practice in sharing data is following the 'five safes':

1. Safe projects –– Is this use of the data appropriate, lawful, ethical, and sensible?
2. Safe people –– Can the user be trusted to use the data in an appropriate manner?
3. Safe data –– Is there a disclosure risk in the data itself?
4. Safe settings –– Does the means of access limit unauthorised use?
5. Safe outputs –– Are the statistical results non-disclosive?

You can find out more about data sharing policies and best practice at [FAIRsharing](https://fairsharing.org/).

## Datasette for sharing data

[Datasette](https://datasette.io/) is an extraordinary tool for exploring, sharing, and publishing data. It helps you take data of any shape or size, analyze and explore it, and publish it as an interactive website and accompanying API. Remember, API stands for application programming interface, which in this case means the data can be accessed directly through programming languages. Datasette is aimed at data journalists, museum curators, archivists, local governments, *economists*, and anyone else who has data that they wish to share with the world.

An example datasette instance is [available here](https://global-power-plants.datasettes.com/); it shows a dataset of power stations.

So, how does it work? Let's assume you have some data in a CSV file. The first step in creating a datasette website is to turn that CSV file into a SQL-lite database (don't worry if you don't know what that is). The second step is to publish the data either *locally* (on your own computer) or on the internet (using a cloud service provider). Once the data are published, you and/or others can interact with them in several different ways.

To use datasette, you'll need a Python installation and to install some extra packages. (There's a brief guide to installing packages in the Chapter on {ref}`code-preliminaries`.). Then, to install the datasette package run

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

```{admonition} Exercises
1. Download the CSV file from the [particulate matter repo](https://github.com/aeturrell/datasette_particulate_matter) and run it as a datasette locally on your own computer.
2. (Advanced) Run the same set of data via a datasette instance on the web using Google Cloud Run. (This requires a Google Cloud Account; you may be billed for excessive use of this service so remember to shut it down via the Google Cloud Console once you're done.)
```

### Pros and cons of datasette

[**datasette**](https://datasette.io/) is an extremely quick and cost-efficient way to serve up large datasets to anyone with an internet connection. The full utility comes from the ways that people can then use the data. Using the particulate matter example from the previous section, people can:

- Manually browse the data, making cuts by choosing from the filtering options or editing the equivalent SQL code.

- Manually download the data (and cuts thereof) as CSV or JSON files.

- Once data are filtered, copy the generated SQL code to reproduce the same filters programmatically in future. (This makes getting certain cuts *reproducible* for users.)

- Programmatically download cuts of the data using the generated CSV, SQL, or JSON endpoints. For example, to get the anthropogenic numbers for Southwark in 2018 from the particulate matter datasette instance:
  - CSV, `df = pd.read_csv("https://particulatematter-fsx2r7puuq-nw.a.run.app/uk_particulate_matter.csv?sql=select+rowid%2C+local_authority_code%2C+pm_anthropogenic%2C+pm_total%2C+pm_non_anthropogenic%2C+local_authority_name%2C+year%2C+region%2C+country+from+uk_particulate_matter+where+%22local_authority_name%22+like+%3Ap0+and+%22year%22+%3D+%3Ap1+order+by+rowid+limit+101&p0=%25southwark%25&p1=2018&_size=max")`
  - SQL,`select rowid, local_authority_code, pm_anthropogenic, pm_total, pm_non_anthropogenic, local_authority_name, year, region, country from uk_particulate_matter where "local_authority_name" like '%southwark%' and "year" = '2018' order by rowid limit 101`
  - JSON, `df = pd.read_json("https://particulatematter-fsx2r7puuq-nw.a.run.app/uk_particulate_matter/uk_particulate_matter.json?_sort=rowid&local_authority_name__contains=southwark&year__exact=2018&_shape=array")`

- By integrating with GitHub or other tools, datasette can be automated so that when the raw data change, the instance being served online is updated too.

- If you are building dashboards that are also deployed on the web, you can use a datasette website as the back-end to serve up the data to the dashboard (making use of the automatic API features of datasette).

Publishing data with datasette is *fast*: we only needed a CSV file and a couple of commands. It's also *easy for end users* who can access the data via a website and filter it or download it however they like, and access it both manually and programmatically. By having several options to access data, by allowing users to filter to just the data they need, and by allowing for the inclusion of [metadata](https://docs.datasette.io/en/latest/metadata.html) and information [on units](https://docs.datasette.io/en/latest/metadata.html#specifying-units-for-a-column), datasette also makes it easier to follow *best practices*.

Datasette also has add-ons that provide extra support for geospatial data, password protection, and more; see the [plug-ins](https://datasette.io/plugins) page.

The *downsides* of datasette are that you have to pay to serve up the data (at least if it becomes very popular), that it is built around *tabular data*, and that the data are not very findable (one of the four data principles): they may be available online through a website, but unless you do some work in sharing, promoting, and registering the link where they can be found, people are unlikely to find them.

## Data repositories for sharing data

Putting your data in a managed data repository is another way to ensure others can find it and re-use it. Data repositories are websites where you can deposit a dataset, and its metadata, and others can come along and download it. The repositories are managed by third party organisations, and, typically, they are used to lodge a dataset that won't be updated, eg if you have a dataset that was used for a paper that's been published. Some of the benefits of data repositories are:

- You may get a permalink, eg a digital object identifier (DOI), and citation information to help people recognise and refer to your contribution

- Unless you are lodging *extremely* large datasets, you will likely not have to pay anything to host your data

- Data repositories are searchable, both within the site itself and in the sense of being indexed by Google-so people will potentially be able to find your data via a Google search.

Some of the less good things, or at least things to bear in mind, about data repositories are:

- They are much less suitable for data that are being updated, and not at all suited to automatic updates (datasette is a better tool for this)

- They do not always provide good accessibility options; usually the only option is to download *all* of the data in a single format rather than the cut you want in the format you want.

- Whether or not the data are interoperable comes down to how the user chose to provide the data. Sometimes you will find repositories with closed data formats that require special tools. You can choose to put data in interoperable formats, but you aren't compelled to.

So the canonical use case for a data repository is static data that's associated with a paper and which you don't think many people will want to access a lot, or in different ways, but which needs to exist as a matter of record.

If you're interested in exploring some data repositories, there are lists [here](https://authorservices.taylorandfrancis.com/data-sharing-policies/repositories/) and [here](https://www.springernature.com/gp/authors/research-data-policy/repositories/12327124). If you'd like to see how one works, [check out Zenodo](https://zenodo.org/) which, at the time of writing, accepts up to 50GB per dataset and may accept larger files following discussion. Zenodo accepts both code and data, and gives each repo a DOI. Zenodo is run and hosted by CERN, the European Organization for Nuclear Research.

## GitHub Flat Data

GitHub, the remote code repository service, recently launched its [Flat Data tool](https://octo.github.com/projects/flat-data). In the launch document they explain that *they* were inspired by Simon Willison, the creator of the **Datasette** package featured above. Flat Data actually comprises three different tools: ['flat action'](https://github.com/marketplace/actions/flat-data), which fetches and transforms data using GitHub Actions (don't worry if you don't know what that is), ['flat editor'](https://marketplace.visualstudio.com/items?itemName=GitHubOCTO.flat) which is a Visual Studio Code-based graphical interface for creating workflows with flat actions, and 'flat viewer' which allows anyone to browse, filter, and access data from flat files stored in a GitHub repo.

The genius of Flat Data viewer is that any GitHub repository that has a file in the compatible format can be viewed using the tool by using the prefix "flatgithub.com" instead of the usual path to the file. To take a specific example using the particulate matter that we've already seen in this chapter,

[https://github.com/aeturrell/datasette_particulate_matter/blob/main/uk_particulate_matter.csv](https://github.com/aeturrell/datasette_particulate_matter/blob/main/uk_particulate_matter.csv)

becomes

[https://flatgithub.com/aeturrell/datasette_particulate_matter?filename=uk_particulate_matter.csv](https://flatgithub.com/aeturrell/datasette_particulate_matter?filename=uk_particulate_matter.csv)

Not only that but, just as with datasette, you can easily download the data in a format that suits you, and perform rudimentary data filtering.

Some useful features of **flat data viewer** are that it integrates with your existing GitHub workflow and that it is free. However, the maximum size of dataset that you can lodge in a GitHub repo is limited to 100 Mb.
