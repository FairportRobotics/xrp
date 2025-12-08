# Fairport Robotics XRP Code

---

## Getting Started

The following steps need to be taken. The command prompt commands are given, however your IDE might have other ways of
doing this.

### 1. Clone this repository to your computer

`git clone https://github.com/FairportRobotics/xrp`

Once the repository is cloned, you will want to change into the xrp directory

`cd xrp`

### 2. Create a Python virtual environment

We want to create a self-contained environment

`python -m venv .venv`

### 3. Activate the virtual environment

You want the packages installed to the virtual environment so you need to activate it

Windows:

`.venv\Scripts\activate`

On Mac:

`source .venv/bin/activate`

### 4. Install robotpy

Install the package with pip to your virtual environment with

`pip install robotpy`

If you have previously installed this package, update it with

`pip install --upgrade robotpy`

### 5. Create your own branch and push it to GitHub

It takes a couple of steps: Create the branch

`git branch YOUR_BRANCH_NAME_HERE`

Checkout the branch

`git checkout YOUR_BRANCH_NAME_HERE`

Push the branch to GitHub

`git push origin YOUR_BRANCH_NAME_HERE`

### 6. Initialize your robot project

We can get some boilerplate by using this command

`python -m robotpy init`

This creates pyproject.toml and robot.py files

### 7. Commit and push these initial files to your branch

First add your changes

`git add .`

Commit your changes with a helpful message

`git commit -m "Initial commit"`

Then push the changes to GitHub

`git push`
