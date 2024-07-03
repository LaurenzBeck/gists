<p align="center">
    <img alt="treasure chest banner image" src="docs/artwork/isometric_chest_by_sephiroth_art_da0mr89-375w-2x.jpg">
</p>

<h1 align="center">🐍📦 Python Gists Importing</h1>

<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/📦_version-1.0.0-blue">
    <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.11-yellow?logo=python"></a>
    <a href="https://python-poetry.org/"><img alt="Poetry" src="https://img.shields.io/badge/Poetry-1.8.3-blue?logo=Poetry"></a>
    <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
</p>
<p align="center">
    <a href="https://www.repostatus.org/#active"><img src="https://www.repostatus.org/badges/latest/active.svg" alt="Project Status: Active – The project has reached a stable, usable state and is being actively developed." /></a>
    <img alt="Static Badge" src="https://badges.frapsoft.com/os/v3/open-source.svg">
    <a href="https://opensource.org/license/mit/"><img alt="MIT" src="https://img.shields.io/badge/🗝️_license-MIT-blue"></a>
</p>

<p align="center">
  <a href="https://github.com/LaurenzBeck/gists?tab=readme-ov-file#-usage">📦 Usage</a> •
  <a href="https://github.com/laurenzbeck/gists?tab=readme-ov-file#-installation">🐍 Installation</a> •
  <a href="https://github.com/laurenzbeck/gists?tab=readme-ov-file#-motivation">💡 Motivation</a> •
  <a href="https://github.com/laurenzbeck/gists?tab=readme-ov-file#-publishing-a-gist">🆙 Publishing a Gist</a>
</p>

## 📦 Usage

This package provides a very convenient way to import [GitHub gists](https://docs.github.com/de/get-started/writing-on-github/editing-and-sharing-content-with-gists) directly from Python:

```python
from gists import <gist_id>
```

The first time a gist is imported this way, it will be downloaded using GitHub's API and saved locally as `gists/<gist_id>.py` (The description of the gist will be saved as `gists/<gist_id>.md`). Every subsequent import will not require internet access, as the local copy of the gist will be used.

## 🐍 Installation

The package is published on PyPi, so it can be installed with pip using:

```sh
$pip install python-gists
```

## 💡 Motivation

During my PhD, I had many ideas and felt confident to work on a few full packages. I discovered that developing packages and everything that comes with them requires a lot of effort and diverse skills including:

+ managing dependencies
+ configuring linters, formatters, task runners ...
+ setting up CI/CD, pre-commit
+ writing technical documentation
+ planning your code organization and namespaces
+ implementing your ideas
+ testing your implementation
+ choosing evocative artwork and emojis 😉
+ choosing a license
+ preparing a repository for contributions by adhering to [community guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)

One also has to be creative and lucky in finding a short and fitting name, that is still available on PyPi.

That the motivation and energy for working on personal projects and ideas often comes in bursts, does not help either.

While writing a proper Python package is without a doubt the appropriate way to implement and share your moderately complex ideas, smaller ideas suffer from a few problems:

+ the package development overhead is too high
+ bundling all of your ideas into one utility package can quickly become chaotic
+ how do you properly name and advertise a package consisting of a single class or function?

[GitHub gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists#about-gists) provide a lightweight deployment alternative to building and publishing a package on PyPi. The user experience of creating and managing them is as easy as it can get (amazing work there 💖). Another big advantage is the guaranteed collision-free (though arguably un-relatable) "package name", you get from the gist id.

No one stops you from just downloading a gist manually and placing it in your codebase, but there are other alternatives. [`gist-import`](https://github.com/matteoferla/gist-import/tree/main) is a package very similar in functionality to this one (shout-out to https://github.com/matteoferla for his work on the package 💪). I even use it in the background because it already contained the gist fetching logic 😅. I recently watched a [PyCon talk](https://www.youtube.com/watch?v=ItOUx7zTcgo) where the Python import machinery was explained in detail, and I simply wanted to play around with the new concepts in my free time.

## 🆙 Publishing a Gist

GitHub has good [documentation on how to create and manage gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists) 📖.

I will give some additional considerations that are often overlooked.

### 🗝️ Licensing

When you want your gist to be used by as many people as possible, it is important to add a license to your gists.

> 🤚 If you want an uncomplicated license that gives your users a lot of freedom, the [MIT license](https://opensource.org/license/mit) is a good default choice.

According to a [blog post](https://zebracatzebra.com/oss/getting-the-gist-of-github-gist-licensing/) from Jeff Luszcz there are two good options:

+ state a default license in the README of your GitHub profile
+ state the license in the gist itself

Because the full license text can be quite large, which would diminish the visual appeal of shorter gists, one can also just mention the name of the license with a copyright date and the copyright owner.

I included an example of this approach in the [📝 Template](https://github.com/laurenzbeck/gists?tab=readme-ov-file#-template)

### 📖 Referencing

Unfortunately, [getting a DOI](https://docs.github.com/de/repositories/archiving-a-github-repository/referencing-and-citing-content) (document object identifier) from Zenodo only works with repositories.

You can, however, include a bibitem in the description of your gist (see the [📝 Template](https://github.com/laurenzbeck/gists?tab=readme-ov-file#-template)):

```bibtex
@misc{<bibkey>,
  author={<your name>},
  title={<the title of your gist>},
  year={<year of publication>},
  url={https://gist.github.com/<user name>/<gist id>},
} 
```

### 📝 Template

#### Description

````markdown
# Title

> 🚮 feel free to delete any section that is not helpful for your description (including this message).

Short description.

## 📦 Usage

How to use the gist with code examples.

## 🤔 Statement of Need

Describe why the code in your gist is needed.

## 🐍 Installation

This gist can be installed using the [`python-gists`]() package:

```sh
$pip install python-gists
``` 

After that, simply import the gist in your code via:

```python
from gists import <gist id>
```

### 📄 Requirements

If your gist depends on other Python packages, include a list of those dependencies here. Users have to manually make sure that they have these dependencies installed. I would suggest using version specifiers used by [poetry](https://python-poetry.org/docs/dependency-specification/):

```toml
python = "^3.11"
```

## 🗝️ License and Copyright ©️

The code inside this gist is licensed under the [MIT](https://opensource.org/license/mit) license.

Copyright <YEAR> <COPYRIGHT HOLDER>

## 📝 Cite Me

```bibtex
@misc{<bibkey>,
  author={<your name>},
  title={<the title of your gist>},
  year={<year of publication>},
  url={https://gist.github.com/<user name>/<gist id>},
}
```

````

#### Code

```python
"""# module title

module description.
"""
# Copyright <YEAR> <COPYRIGHT HOLDER>
#
# Licensed under the [MIT](https://opensource.org/license/mit) license.

def hello(name: str = "world") -> None:
  """🗣️ says hello to `name`."""
  print(f"hello, {name}!")
```

---

## 🖼️ ©️ Banner Artwork Attribution

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br />The art in the banner of this README is licensed under a [Creative Commons Attribution-NonCommercial-No Derivatives Works 3.0 License](https://creativecommons.org/licenses/by-nc-nd/3.0/). It was made by [sephiroth-art](https://www.deviantart.com/sephiroth-art). Check out his beautiful artwork ❤️
