#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pelican Plug-in for generating TAO wiki pages
"""
import os
import shutil
import yaml

from pelican import signals


def gen_gdc_pages(output_gen_folder):
    """
    Make sure that we start with a clean slate each time
    """
    path_to_gdc_data = os.path.join('data', 'gdc', 'sessions.yaml')

    with open(path_to_gdc_data, 'r') as data:
        gdc_data = yaml.load(data, Loader=yaml.FullLoader)

    for track_name, sessions_by_year in gdc_data.items():
        track_content = f"""Title: {track_name} GDC Sessions
Date: 01-01-01 00:33
Category: Wiki
Slug: gdc-{track_name.lower().replace(' ', '-')}-sessions\n\n"""

        track_content += "[Back to GDC Wiki](/gdc-wiki)" 
        for year, sessions in sorted(sessions_by_year.items()):
            track_content += f'<br><br><br><hr>\n\n### {year}\n\n'
            for session_data in sessions:
                title = session_data["title"]
                url = session_data["video_url"]
                track_content += f'- [{title}]({url}){{:target="_blank"}}\n'
        track_sessions_name = f'gdc_sessions_{track_name.lower().replace(" ", "_")}.md'
        path = os.path.join(output_gen_folder, track_sessions_name)
        with open(path, 'w') as out:
            out.write(track_content)


def clear_generated_folder(output_gen_folder):
    """
    Make sure that we start with a clean slate each time
    """
    pass
    # shutil.rmtree(output_gen_folder)


def render_data_driven_pages(sender):
    """
    Render data driven pages
    """
    output_gen_folder = os.path.join('content', 'gen')
    if os.path.isdir(output_gen_folder):
        clear_generated_folder(output_gen_folder)
    else:
        os.mkdir(output_gen_folder)

    gen_gdc_pages(output_gen_folder)


def register():
    """
    Register Pelican plug-in
    """
    signals.initialized.connect(render_data_driven_pages)
