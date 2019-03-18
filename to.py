#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import subprocess
import re
import os

BASE_URL = "~/"

def check_args():
    if len(sys.argv) <= 1:
        print ("Missing compressed path argument")
        sys.exit(-1)

    return sys.argv[1]

def build_url(segment):
    return BASE_URL + segment

def shquote(s):
    return s.replace("'", "'\\''")

def ls(path):
    command = "find %s -maxdepth 1 -type d" % (shquote(path))
    folders = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode('utf-8').split("\n")
    return filter(lambda f: len(f) != 0, map(lambda f: f.split("/")[-1], folders))

def startsWith(prefix, value):
    return bool(re.match(prefix, value, re.I))

def build_cd(args):
    cd_cmd = BASE_URL
    prefix = ''
    for letter in args:
        prefix += letter
        all_paths = ls(cd_cmd)
        available_paths = list(filter(lambda p: startsWith(prefix, p), all_paths))
        if len(available_paths) == 0:
            return cd_cmd
        elif len(available_paths) == 1:
            cd_cmd = os.path.join(cd_cmd, available_paths[0])
            prefix = ''
    if len(prefix) != 0:
        print (map(str, available_paths))
        sys.exit(-1)
    return cd_cmd

def main():
    args = check_args()
    cmd = build_cd(args)
    print ("cd " + cmd)

main()
