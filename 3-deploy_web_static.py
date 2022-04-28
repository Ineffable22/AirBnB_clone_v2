#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers, using the
function deploy:"""


from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists
env.hosts = ['35.185.108.180', '34.229.169.234']
env.user = 'ubuntu'


def do_pack():
    """ All archives must be stored in the folder versions
    (your function should create this folder if it doesn’t exist) """
    try:
        local("mkdir -p versions")
        date = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)"""
    if exists(archive_path) is False:
        return False
    try:
        exc = archive_path.split("/")[-1]
        filename = exc.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, filename))
        run('sudo tar -xzf /tmp/{0} -C {1}{2}/'.format(exc, path, filename))
        run('rm /tmp/{}'.format(exc))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, filename))
        run('rm -rf {}{}/web_static'.format(path, filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, filename))
        return True
    except Exception:
        return False


def deploy():
    """Distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
