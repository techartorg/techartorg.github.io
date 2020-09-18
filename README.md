# TAO-Wiki

Welcome to the TAO-Wiki!

You can find it at wiki.tech-artists.org

Within these grand confines you will find an eclectic array of how to's and documentation on the arcane art of technology.

"E pluribus unum"
-Tech Art

----

## Setting up your workspace

To start contributing you will need to have the following:
- [Python3](https://www.python.org/downloads/)
- [tox](https://pypi.org/project/tox/)

---

### Setting up on macOS & Linux
1. Clone this repo: \
`git clone https://github.com/techartorg/techartorg.github.io.git && cd techartorg.github.io`
2. Init the `tox` environment for the Python you have installed: \
`python3 -m tox -e py38`
3. Activate the `virtual env` that tox created for you: \
`. .tox/py38/bin/activate`
4. Use make to generate the website and start hosting it locally: \
`make devserver`
5. goto `localhost:8000` in a webrowser


---

### Setting up on Windows

1. Clone this repo: \
`git clone https://github.com/techartorg/techartorg.github.io.git && cd techartorg.github.io`
2. Init the `tox` environment for the Python you have installed: \
`python3 -m tox -e py38`
3. Run `win_run_pelican.bat`
4. goto `localhost:8000` in a webrowser


---

# How To Contribute

- [How to edit a page](https://techartorg.github.io/contribute/how_to_edit_page/)
- [How to add a page](https://techartorg.github.io/contribute/how_to_add_page/)
