# Basic Git Workflow

This document outlines the basic steps for using Git, including how to clone a repository, pull updates, push changes, and check the status and history of your repository.

## Table of Contents
1. [Cloning a Repository](#cloning-a-repository)
2. [Making Changes](#making-changes)
3. [Checking Status](#checking-status)
4. [Pulling Changes](#pulling-changes)
5. [Pushing Changes](#pushing-changes)
6. [Viewing Commit History](#viewing-commit-history)
7. [Conclusion](#conclusion)

## Cloning a Repository

To start working on a project, you first need to clone the repository to your local machine. This creates a local copy of the repository.

    git clone <repository-url>
    
    # To clone this repo
    git clone https://github.com/devidmazeeta/PythonTutorial.git

## Making Changes

Once you have cloned the repository, navigate to the project directory:

    cd repo
    
    Eg:
    cd PythonTraining

## Checking Status

To see the status of your changes, use the following command:

    git status

This command will show you which files are staged for commit, which are modified, and which are untracked.

## Pulling Changes

Before pushing your changes, it's good practice to pull the latest changes from the remote repository to ensure you're working with the most up-to-date version.

    git pull origin <branch-name>

Replace <branch-name> with the name of the branch you are working on (e.g., main).

    git pull origin main

## Pushing Changes

After making your changes and committing them locally, you can push them to the remote repository.

i. First, stage your changes:

    git add .

ii. Then commit your changes with a meaningful message:

    git commit -m "Your commit message here"

iii. Finally, push your changes to the remote repository:

    git push origin <branch-name>

Again, replace <branch-name> with the appropriate branch name.

## Viewing Commit History

To view the commit history of your repository, use:

    git log

This command will display a list of commits, along with their commit messages, authors, and timestamps. You can use various options with git log to customize the output.

## Conclusion

These basic Git commands will help you clone repositories, make changes, check the status, pull updates, view commit history, and push your contributions to remote repositories. Familiarizing yourself with these commands is essential for effective collaboration in software development.
