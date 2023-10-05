#!/usr/bin/python3
'''
This module is a fabfile for downloading a tgz from a webserver
'''

from datetime import datetime
from fabric.api import local, lcd


def do_pack():
    '''
    The function generates a .tgz file from the web_static folder
    '''

    # create a folder called versions
    local('mkdir -p versions')

    # create the filename to store the generated .tgz file
    archive = 'versions/web_static_' + datetime.now().strftime(
        "%Y%m%d%H%M%S") + '.tgz'

    # generate the file
    cmd = local(f'tar czvf {archive} web_static')

    # return the file path if command succeeded
    if cmd.succeeded:
        return archive

    # return none
    else:
        return None
