#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive"""
from fabric.api import local, env, put, run
from datetime import datetime
import os

env.hosts = ['54.237.207.109', '54.87.255.39']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local('mkdir -p versions')
        filename = 'web_static_{}.tgz'.format(date)
        local('tar -cvzf versions/{} web_static'.format(filename))
        return ("versions/{}".format(filename))
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not archive_path or not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp')
    arch_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(ar_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                arch_name, arch_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(arch_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(arch_name))
        print("New version deployed!")
        return True
    except Exception:
        return False
