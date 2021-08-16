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

  ```buildoutcfg
  git clone https://annajiat.github.io/2021-08-17-usgs-ngwos-online/
  ```

  Conversely, if using ssh, the command would be:
```buildoutcfg
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

```buildoutcfg
git checkout main
git fetch origin
git reset --hard origin/main
```

Technically, this is a heavy handed approach, but it ensures we are all on the same page. In practice, I typically
just do:

```buildoutcfg
git fetch --all
git pull
```

The `--all` tag just ensures that my local repo copy has all of the remote branches in the repo. Another useful command
is `--prune`, which will delete local branches that are not active and/or already closed or merged in the remote 
copy of the repo. This is handy for large repos where several feature updates and/or issues have been addressed. 

Now that you have the most up to date version of the repo on your machine, you can create a new branch from the currnet
version of the `master` by (replace `engel` with your last name):

```buildoutcfg
git checkout -b fb-engel
```


