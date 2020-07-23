# GitHub Pages Pelican Build Action

This action builds a Pelican project and deploys it to GitHub Pages.

Please ensure a `requirements.txt` is present for your site and installs
`pelican` and other requirements needed to build your site.

A `requirements.txt` can be generated by running `pip freeze > requirements.txt`
in the virtual environment your pelican site is developed in.

## Environment variables

  - `GH_PAGES_BRANCH` (optional): override the default `gh-pages` deployment branch
  - `PELICAN_CONFIG_FILE` (optional): override the default `pelicanconf.py` config file

## Demo

Repository: https://github.com/nelsonjchen/pelican-action-demo

Website: https://pelican-action-demo.mindflakes.com/

## History

Extracted from https://github.com/desertpy/desertpy-pelican.

It is not used there anymore though. For most sites though, this should
suffice.

[1]: https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys