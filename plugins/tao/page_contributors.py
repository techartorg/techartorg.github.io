"""
This plugin retrieves the git contributors to a file and updates the page metadata.
"""

import logging
import datetime

from pelican import signals, contents

import configparser
from pydriller import RepositoryMining
from git import Repo


def get_default_author():
    """
    Retrive the default author from the git config and
    the current date
    """
    try:
        repo = Repo('.')
        reader = repo.config_reader()
        default_author = reader.get_value('user', 'name')
    except configparser.NoSectionError as exc:
        msg = f'Failed to retrive user name from git config.\n{str(exc)}'
        logging.warning(msg)
        default_author = 'Default User'

    logging.debug('Default author from git config: {}'.format(default_author))
    default_date = datetime.datetime.now().strftime('%D')
    return default_author, default_date


def set_git_contributors(generator):
    """
    Set the git contributors for a given page
    """
    default_author, default_date = get_default_author()

    # initialize git page stats
    for page in generator.pages:
        page.git_author = None
        page.git_created_on = None
        page.git_contributors = []
        page.git_revision_count = 0

    for page in generator.pages:
        revision_count = 0
        contributors = set()
        for commit in RepositoryMining(".", filepath=page.filename).traverse_commits():
            if page.git_author == None:
                page.git_author = commit.author.name
                page.git_created_on = commit.author_date.strftime('%D')
            contributors.add(commit.author.name)
            revision_count += 1
        
        if revision_count > 1:
            page.git_revision_count = f'{revision_count} revisions'
        else:
            page.git_revision_count = f'{revision_count} revision'

        page.git_contributors = list(contributors)
        
        # if page is not added to git
        if page.git_author == None:
            page.git_author = default_author
            page.git_created_on = default_date


def register():
    signals.page_generator_finalized.connect(set_git_contributors)
