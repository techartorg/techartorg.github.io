#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pelican Plug-in for generating tags for TAO wiki pages
"""
import collections
import datetime
import logging
import os

from pelican import signals


def should_run():
    """
    To make sure that we don't run the page gen in an infinite loop,
    we check the last time we ran this plugin.
    """
    run = True

    cur_dir = os.path.dirname(__file__)
    track_file = os.path.join(cur_dir, '.gen_page_tags')
    if os.path.isfile(track_file):
        mtime = os.path.getmtime(track_file)
        mtime = datetime.datetime.fromtimestamp(mtime)
        now = datetime.datetime.now()
        elapsed = now - mtime

        if elapsed.seconds < 30:
            run = False

    with open(track_file, 'w'): pass
    return run


def gen_page_tags(generator, output_gen_folder):
    """
    Collect all of the tags from the pages and
    generate tag md files with links to the pages.
    """
    if not should_run():
        return

    tags = collections.defaultdict(list)
    for page in generator.pages:
        if 'tags' in page.metadata:
            for tag in page.metadata['tags']:
                tags[tag.name].append({
                    'url': page.url,
                    'title': page.title
                })
    
    for tag, page_data in tags.items():
        logging.debug(f'tag: {tag}')

        page_md = f'Title: Pages with "{tag}" tag\n'
        page_md += f"Date: 01-01-01 00:33\n"
        page_md += f"Slug: tag/{tag}\n\n<hr><br><br>"
        for page in page_data:
            logging.debug(f'\t{page}')
            page_md += f'[{page["title"]}](/{page["url"]})' + '{:target="_blank"}\n'

        tag_md_name = f'tag_{tag}.md'
        path = os.path.join(output_gen_folder, tag_md_name)
        with open(path, 'w') as out:
            out.write(page_md)


def render_tag_pages(generator):
    """
    Render tag pages
    """
    output_gen_folder = os.path.join('content', 'gen')
    if not os.path.isdir(output_gen_folder):
        os.mkdir(output_gen_folder)

    gen_page_tags(generator, output_gen_folder)


def register():
    """
    Register Pelican plug-in
    """
    signals.page_generator_finalized.connect(render_tag_pages)
