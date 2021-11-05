# Story Board

## Title Page
- About me
- Cardiff University
- THIS Institute

## How to build an awesome python package
- **Motivation**: Make this `pip-installable`
- Talk based on: https://antonz.org/python-packaging/
- Not only how to make a package, but how to make an awesome package
- `AWESOME`: `automation`, `documentation`, `testing`, `packaging` and more
- There are a lot of concepts in this talk that could be a talk by itself
- `VScode`, `Command line`, `Python`, `Packaging`, `Git`, `GitHub`
- Basic Usage of the `Command line`


## Git and GitHub
- Version control
- Time and Space: `https://ljvmiranda921.github.io/notebook/2021/06/05/avengers-git/`
- `Change`, `Add`, `Commit`, `Push` 
- Cool git-GitHub slide here
- Practical steps

## Python
- Packages
- how to install a package
  - `pip` - built into python
- `PYPI` - `testPyPI`


## Rock-Paper-Scissors
- How the game is played
- Structure of the code


## `Flit`
- Simple way to put Python packages on PyPI.
- Less thought about packaging
- Helps avoid common mistakes
- *Make the easy things easy and the hard things possible* 


## README.md and CHANGELOG.md
- `README.md`
- `CHANGELOG.md`


## Testing
- Test driven development
- Write test - Write code - Fix test
- `pytest`


## Other software
- `black`: PEP8 convention code formatter
- `flake8`: Style Guide Enforcement tool (collection of other tools)
- `mypy`: Static type checker (using annotations)
- `pylint`: Static code analysis tool:
  - looks for programming errors
  - helps enforcing a coding standard 
  - sniffs for code smells
  - offers simple refactoring suggestions
- Examples of all these tools


## `Tox`
- Brings everything together
- Task automation tool


## GitHub Actions
- Easy to automate tasks
- Examples of GitHub Actions using my ED-EMS Paper
- Nicolas Cage: `https://twitter.com/tartanllama/status/1163927778376462337`




# Practical Steps (Name - `pgr_lib`)
## Before talk
- Delete `pgr_lib` folder, GitHub repo and PyPI package
- Need to have `.pypirc`, `src code`, `test code`, `.pypirc`, `tox.ini`
- `Windows Terminal` -> `Run As Administrator`
- Activate `conda` environment -> `pgr_env`
- `VScode` -> Large fonts

## How to make a package
- Initialise `git` repository
- Start GitHub repo
  - Create repository
  - `.gitignore`
  - git remote add origin `https://github.com/11michalis11/pgr_talk.git`
- Start up rock paper scissors game in python in `src/pgr_lib`
  - `git status`
  - `git add`
  - `git commit -m "Initial commit"`
  - `git push -u origin main`
- Flit
  - `python -m pip install flit`
  - `flit init`
  - Push `pyproject` and `License`
  - `python -m flit install --symlink`
  - Add generated files to `.gitignore` 
  - Play a round of rock paper scissors
- `PyPI` and `TestPyPI`
  - `.pypirc`
  - https://flit.readthedocs.io/en/latest/upload.html#using-pypirc
- Publish to `TestPyPI`
  - `flit publish --repository pypitest`
  - (DO NOT RUN) `flit publish`

## Awesomeness

### Part 1 (Readme and Changelog)
- `README.md`
  - Write a basic `README.md` (Description, Installation, Usage)
  - `readme = "README.md"`
- `CHANGELOG.md`
  - \# v0.0.1 Initial commit
  - \# v0.0.2 Add Readme file
  - __init__.py -> version == 0.0.2
  - Commit all changes "Update to version 0.0.2"
- `flit publish --repository pypitest`

### Part 2 (Tests and linters)
- Tests
  - `python -m pip install pytest`
  - Add tests for `play_round()`
  - Run tests
  - Commit
- Linters
  - `python -m pip install black pylint tox`
  - Run black
  - Run pylint and add docstrings
  - Commit
- `Tox`
  - Create `tox.ini`
  - `Run tox`
  - Commit
- Other tests and linters
  - `flake8`
  - `mypy`
  - `mccabe`
  - `coverage`
- New version: `flit publish --repository pypitest`


### Part 3 (Cloud build and test)
- GitHub Actions
  - Create `.github/workflows/tests.yml`
  - `tests.yml`
    - Pre-face (all the stuff that go before the `steps`)
    - Step 1: Checkout sources -> `actions/checkout@v2` (to be able to use the actual repository)
    - Step 2: Set up Python ${{ matrix.python-version }} -> `actions/setup-python@v2 with: python-version: ${{ matrix.python-version }}`
    - Step 3: Update pip -> `python -m pip install --upgrade pip`
    - Step 4: Install tox -> `python -m pip install tox tox-gh-actions`
    - Step 5: Run tox -> `python -m tox`
  - Edit `tox` -> `gh-actions`
  - `Commit` and show tests running
- New version: `flit publish --repository pypitest`