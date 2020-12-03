#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pelican Plug-in for working around a issue with mixing 
HTML formatting and Markdown.

At the time of make this the Python markdown module had issues with
formatting like this (even though it is supported)

<div class="row" markdown="1">
<div class="col-md-4" markdown="1">
### Some markdown
</div>
<div class="col-md-4" markdown="1">
### Some more markdown
</div>
</div>

The second nested div would not be formatted.

The workaround is 

Step 1.
Comment the HTML in a special way
example:

<!-- tao-post-format <div class="row" markdown="1"> -->
<!-- tao-post-format <div class="col-md-4" markdown="1"> -->
### Some markdown
<!-- tao-post-format </div> -->
<!-- tao-post-format <div class="col-md-4" markdown="1"> -->
### Some more markdown
<!-- tao-post-format </div> -->
<!-- tao-post-format </div> -->

Step 2.
Add `tao-post-format: True` to the header config of the .md file

example:
Title: Tech Art Job Descriptions in Games
Date: 01-01-20 16:40
Template: wiki_leaf_page
Tags: job, games
tao-post-format: True

Step 3.
Let this plugin uncomment the HTML after the Python
Markdown processor is done.

"""
import re

from pelican import signals


def insert_formatting(path):
    """
    Find the commented out formatting and 
    remove the comments
    """
    html_text = open(path, 'r').read()

    html_text = re.sub(r'<!--\s*tao-post-format\s*(.+)\s*-->', r'\1', html_text)
    open(path, 'w').write(html_text)


def run_post_formating(path, context):
    """
    Process formatting on pages that have 
    `tao-post-format`
    set in the header config.
    """
    if 'page' in context:
        if context['page'].url_format.get('tao-post-format'):
            insert_formatting(path)


def register():
    """
    Register Pelican plug-in
    """
    signals.content_written.connect(run_post_formating)
