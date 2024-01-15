#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.decorators import task
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["100.25.215.229", "3.84.237.147"]


@task
def do_pack():
    """generates a .tgz archive from web_static"""
    datestring = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(datestring)
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static/".format(file_name)).succeeded:
        return file_name
    return None


@task
def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""
    try:
        if not os.path.exists(archive_path):
            return False
        with_ext = archive_path.split("/")[-1]
        without_ext = archive_path.split("/")[-1].split(".")[0]
        pth = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p " + pth + without_ext)
        run("tar -xzf /tmp/{} -C {}{}/".format(with_ext, pth, without_ext))
        run("rm /tmp/{}".format(with_ext))
        run("mv {1}{0}/web_static/* {1}{0}/".format(without_ext, pth))
        run("rm -rf {}{}/web_static".format(pth, without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(pth, without_ext))
        return True
    except Exception:
        return False


@task
def deploy():
    """Creates and distributes an archive to webserver"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


@runs_once
def remove_local(number):
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    local("ls -dt versions/* | tail -n +{} | sudo xargs rm -fr".format(number))


@task
def do_clean(number=0):
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    if int(number) == 0:
        number = 1
    number = int(number) + 1
    remove_local(number)
    rem_path = "/data/web_static/releases/*"
    run("ls -dt {} | tail -n +{} | sudo xargs rm -fr".format(rem_path, number))
