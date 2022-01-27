# Genetic-DnD
<p align="center">
  <img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/HadsyC/Genetic-DnD">
  <a href="https://github.com/HadsyC/Genetic-DnD/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/HadsyC/Genetic-DnD"></a>
</p>

<!-- To add more shields visit shields.io and copy them as html -->

This repository stores our journey to find the best builds for DnD using Genetic Algorithms!

## Project Setup
First, you need to install pipenv if not installed you can install it using: 

Python devs [recommend](https://packaging.python.org/en/latest/guides/tool-recommendations/#application-dependency-management) the use of pipenv!
>Use Pipenv to manage library dependencies when developing Python applications. See Managing Application Dependencies for more details on using pipenv.


```
$ pip install pipenv
```

To install all the required packages into your environment, go to the folder where you cloned this repository and run:
```
$ pipenv install
```

To activate the environment within your repository-clone, use:

```
$ pipenv shell
```
or
```
$ pipenv run python main.py
```

### Where is my Virtual Environment?
[Normally](https://pipenv.pypa.io/en/latest/install/#virtualenv-mapping-caveat), pipenv will store the virtual environment globally in a folder using the name of the project and a hash code. 

I prefer having my environments stored locally within the project files, this behaviour can be convieniently changed using:

```
$ export PIPENV_VENV_IN_PROJECT=1
```
In Windows you'll need to add the environment variable manually. Follow these [steps](https://letmegooglethat.com/?q=Bro+I+need+them+environment+variables+in+windows+changed) to do it.

## External data
The [data](https://github.com/HadsyC/Genetic-DnD/tree/main/data) folder was  extracted from the [5e-tools repository](https://github.com/5etools-mirror-1/5etools-mirror-1.github.io).
