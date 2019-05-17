#!/usr/bin/python3
import os
import time
import tarfile

t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
BACKUP_NAME = ("backup-" + timestamp)
print(BACKUP_NAME)


def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))
tardir('/var/log', '%s.tar.gz' % BACKUP_NAME)
tar.close()

