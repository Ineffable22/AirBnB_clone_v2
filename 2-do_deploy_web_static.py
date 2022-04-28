#!/usr/bin/python3
"""This script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""


from fabric.operations import env, put, run
from os.path import exists
env.hosts = ['35.185.108.180', '34.229.169.234']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_exc = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exc))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_exc))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exc))
        run('rm -rf {}{}/web_static'.format(path, no_exc))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exc))
        return True
    except Exception:
        return False
