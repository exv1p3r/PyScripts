#!/usr/bin/env python
from obtinfofun import disk_fun
import subprocess

def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print "Espacio usado en el directorio %s" % path
    subprocess.call([tmp_usage, tmp_arg, path])
def main():
       tmp_space()
if __name__ == '__main__':
    main()