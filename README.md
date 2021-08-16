# Exercise
## Parsing and visualizing USGS Gage Data
This exercise is meant to provide some more realistic real-world practice with 
your new python coding skills by having learners load and parse  real USGS 
gage data.

## Overview
1. You will clone this repository, which contains the data and these instructions,
   to your local computer.
2. Next, you will create a local branch in which to make your code and edits.
3. Then, you will create python code to load and manipulate the supplied data.
4. Finally, you will share your results back to the repository by creating and uploading your work to a 
   remote git branch and issuing a pull request.

## Step one: Cloning this repository
Use the skills you learned during Day 1 of the 
[Software Carpentries Workshop](https://annajiat.github.io/2021-08-17-usgs-ngwos-online)
to clone this repository to your local machine. The project page for this repository is:
<https://github.com/frank-engel-usgs/softwarecarpentry-usgs-aug2021>

**Hint:** You will want to `clone` this repo using git bash or other git client. 

<details>
  <summary>Solution</summary>
  
  Open a git bash window in the location you wish your clone of the repository to live.
  Then, issue the command:

  ```bash
  git clone https://annajiat.github.io/2021-08-17-usgs-ngwos-online/
  ```

  Conversely, if using ssh, the command would be:
```bash
git clone git@github.com:frank-engel-usgs/softwarecarpentry-usgs-aug2021.git
```
</details>

## Step two: Create a local branch
Although not explicitly discussed in the Software Carpentries workshop, typically collaborative coding work
in git is handled through branching. There are a couple of different approaches to branching, but probably
the most popular, and certainly most used among USGS is the 
[feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).

In this wrokflow, the `master` (or `main` if using github) branch of the repository always represents the most up-to-date and fully
functioning code. In essence, the `main` branch should be deployable code, software, or whatever is the 
focus of your collaborative work. When someone wishes to edit code to create a new feature, fix a bug, or
update documentation, they will create a branch off of the `main` in which to do any edits. This way, the main
copy of the code is always the most recent *working* copy, and any changes you do in a branch will not break
the code for any other users. 

In this step, we will create a new feature branch in your repo called `fp-<lastname>`, where `fp` is short
for "feature branch" and `<lastname>` is your name. So, for example, I would create a branch called `fb-engel`.

Let's do this for our repo. The steps are well discussed and outlined in the 
[feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).
 article linked above. Here's a short review. 

First, make sure your repo is up to date. If you just did Step One, you should be good to go, but just in case, you can 
issue the following commands from a git bash window:

```bash
git checkout main
git fetch origin
git reset --hard origin/main
```

Technically, this is a heavy handed approach, but it ensures we are all on the same page. In practice, I typically
just do:

```bash
git fetch --all
git pull
```

The `--all` tag just ensures that my local repo copy has all of the remote branches in the repo. Another useful command
is `--prune`, which will delete local branches that are not active and/or already closed or merged in the remote 
copy of the repo. This is handy for large repos where several feature updates and/or issues have been addressed. 

Now that you have the most up to date version of the repo on your machine, you can create a new branch from the currnet
version of the `master` by (replace `engel` with your last name):

```bash
git checkout -b fb-engel
```

This will create a new branch called `fb-engel`, which is an exact copy of `main` and move you into that branch.
Your git bash should now look something like this:

```bash
fengel@IGSKIKCWLTFENG2 MINGW64 /c/REPOS/softwarecarpentry-usgs-aug2021 (main)
$ git checkout -b fb-engel
Switched to a new branch 'fb-engel'

fengel@IGSKIKCWLTFENG2 MINGW64 /c/REPOS/softwarecarpentry-usgs-aug2021 (fb-engel)
$

```

Now you are working in your own local feature branch of the code, and the `main` branch is safe! 

## Step three: create python code

Now we can work on creating the python code necessary to read the supplied data and visualize some 
USGS streamflow information. The data are in the `/data/` folder and consist of comma separated values (CSV)
tables with 10-years of daily values gage data for two streamgages. 

```bash
$ ls data/
 080167500_Guadalupe_SpringBranch_DailyMeanGH.csv
 080167500_Guadalupe_SpringBranch_DailyMeanQ.csv
 080167500_Guadalupe_SpringBranch_DailyMeanQ_GH.csv
'Discharge.Mean@02035000.csv'
```

The structure of each file is similar (but not exactly the same, so beware). Let's use `/data/080167500_Guadalupe_SpringBranch_DailyMeanQ.csv`
first. This CSV has 365 rows corresponding to day of the year, and 10 columns, corresponding the daily mean discharge (Q) per year. The data span 
2011-01-01 to 202-12-30. 

Your job is to use the skills obtained during the first half of the Software Carpentries workshop to:

1. Load the file `/data/080167500_Guadalupe_SpringBranch_DailyMeanQ.csv` into a numpy array
2. Summarize the following statistic for each year of record supplied: mean, minimum, maximum, and range
3. Plot the yearly statistics

<details>
  <summary>Solution #1</summary>
  
  Load the data using numpy. Don't forget to import necessary modules!

  ```python
%matplotlib inline
import matplotlib.pyplot
import numpy


data = numpy.loadtxt(fname='data/080167500_Guadalupe_SpringBranch_DailyMeanQ.csv', delimiter=',')
print(data)

[[123.   37.3  44.9 ...  82.3 734.   81.2]
 [117.   34.8  44.7 ...  81.8 737.   79.1]
 [115.   36.   46.9 ...  81.8 939.   79.2]
 ...
 [ 41.   41.8  52.9 ... 920.   84.7  49.1]
 [ 40.4  38.5  48.  ... 816.   82.9  48.3]
 [ 38.3  40.2  46.8 ... 775.   84.3  50.7]]
  ```

</details>

<details>
    <summary>Solution #2</summary>
  Compute the yearly statistics by recalling the `axis=` keyword funtionality in numpy. 

```python
mean = numpy.mean(data, axis=0)
min = numpy.min(data, axis=0)
max = numpy.max(data, axis=0)
range = max - min
print(mean)
print(min)
print(max)
print(range)

[ 38.15153425  95.49547945  56.09271233  38.25443836 574.71616438
 596.44109589 195.93150685 299.62241096 294.57369863  83.39668493]
[  0.     0.57   0.     0.    38.4  147.    26.8    0.    53.8    9.35]
[  159.  2420.  1890.   955. 39200. 11400.  1030. 17800.  2580.   856.]
[  159.    2419.43  1890.     955.   39161.6  11253.    1003.2  17800.
  2526.2    846.65]
```
</details>

<details>
    <summary>Solution #3</summary>
   Make a plot of the yearly statistics using matplotlib and numpy.

```python
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 4, 1)
axes2 = fig.add_subplot(1, 4, 2)
axes3 = fig.add_subplot(1, 4, 3)
axes4 = fig.add_subplot(1, 4, 4)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

axes4.set_ylabel('range')
axes4.plot(numpy.max(data, axis=0) - numpy.min(data, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()
```

![plot of gage stats](assets/step3img1.png)

</details>

### Stretch Goals
Although beyond the skills that you have learned so far in the Software Carpentries workshop, there are some 
interesting stretch goals you can attempt if you want. Solutions to the first 3 stretch goals are given below.
1. Make a nicer print statement for the statistics printout using the `.format` approach.
2. Change the plot style to a tight sub-plot of bar graphs rather than the line graphs
3. Better yet, make a grouped bar graph of the results by year.
4. Parse the other files, noticing that the format is different for some of them (e.g., the `Discharge.Mean@02035000.csv`
   file contains a index of each day in the first columm, and `080167500_Guadalupe_SpringBranch_DailyMeanQ_GH.csv`
   is has 20 columns, corresponding to Q & GH per year).

<details>
  <summary>Solution</summary>
  
  Open a git bash window in the location you wish your clone of the repository to live.
  Then, issue the command:

  ```bash
  git clone https://annajiat.github.io/2021-08-17-usgs-ngwos-online/
  ```

  Conversely, if using ssh, the command would be:
```bash
git clone git@github.com:frank-engel-usgs/softwarecarpentry-usgs-aug2021.git test
```
</details>