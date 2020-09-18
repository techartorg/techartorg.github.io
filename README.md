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

---

# Licenses

### Code from "GitHub Pages Pelican Build Action"
origin: https://github.com/nelsonjchen/gh-pages-pelican-action

path: `.gh_actions`

licenses:
- APACHE (text `.gh_actions/LICENSE-APACHE`)
- MIT (text `.gh_actions/LICENSE-MIT`)

changes:
- run site gen 2 time; This is needed to process the pages that were generated on the first run.

### Code from "bootstrap-next"
origin: https://github.com/shvchk/bootstrap-next

path: `themes/tao-wiki-bootstrap-next`

licenses:
- MIT (text `themes/tao-wiki-bootstrap-next/LICENSE`)

changes:
- create TAO theme

### Code from "I18N Sub-sites Plugin"
origin: https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites

path: `plugins/pelican-plugins/i18n_subsites`

licenses:
- AGPL-3.0 License (text `plugins/pelican-plugins/LICENSE`)

### Code from "Page Hierarchy"
origin: https://github.com/akhayyat/pelican-page-hierarchy

path: `plugins/pelican-plugins/pelican-page-hierarchy`

licenses:
- BSD-2-Clause License (text `plugins/pelican-plugins/pelican-page-hierarchy/LICENSE`)
