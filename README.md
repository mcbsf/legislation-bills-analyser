## Summary
* [Introduction](#introduction)
* [Architecture](#architecture)
* [Dependencies](#dependencies)
* [How to execute](#how-to-execute)
* [Write up](#write-up)


## Introduction
This repository is an simple analyser of bills and legislators.

Given 4 input files(bills.csv, legislators.csv, vote_results.csv and votes.csv), the code generates 2 output files(bills-support-oppose-count.csv and legislators-support-oppose-count.csv)

## Achitecture
Since it's 2 simple analysis, I choosed to keep the folder structure simple as well. As the code grows(not expected), the architecture may change as well.

The repository is separated in 3 main folders: input, output and app. Outside the folders there's only config and documentation files.

## Dependencies
The OS is ubuntu 20.04, the Python version is 3.8. The only external lib used is pandas.

## How to execute
1. Clone the repository

```
git clone git@github.com:mcbsf/legislation-bills-analyser.git
```

2. Create environment

```
pip install virtualenv
cd legislation-bills-analyser
virtualenv venv
```

3. Activate environment
```
source venv/bin/activate
```

4. Install depedencies

```
pip install -r requirements.txt
```

5. Run

```
python app/main.py
```

## Write up
### Time complexity. What tradeoffs did I make:
1. instead of using nested functions(as in merge functions inside app/analysers), I choosed to do one call at once, loosing performance but with a more clear code.
2. also choosed Pandas instead using built in functions to abstract parsings, aggregations and joins code complexity. This may lose performance as well, but gain in development speed and readability.
3. I could have used Polars instead Pandas, wich is much faster and memory safer, but I'm not that used to it and would have cost a few hours more of study to implement this analysers. If you want to know more about Polars, you can read my [linkedin post](https://www.linkedin.com/posts/mario-cardoso-95393b175_polars-python-dataanalysis-activity-7042127297973207040-mrrQ?utm_source=share&utm_medium=member_desktop) about it
### How would I change my solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
Since the code tries to follow SOLID patterns(although it could be refactored to achieve better SOLID patterns), the Open Closed principle says it woulld not affect to much, since its open for new features but closed for modifications. 

Probably it would need only 2 lines to edit:
1. the pivot table creation to use this columns as index in bills_analyser.split_votes_count_by_vote_type function
2. the function order_columns_to_expected_output to add these columns

### How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
I would mount the dataframe from the lists, in the beginning of main.py, and would keep the dataframe as input in the analysers to do not lose previous work unless performance is a big priority.

### How long did I spend working on the assignment?
2 hours on development and 1 hour on documentation