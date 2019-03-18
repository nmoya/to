#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import subprocess
import re
import os
from colorama import Fore, Style

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

def cprint(color, text):
    sys.stderr.write(color + text + Style.RESET_ALL)

def build_cd(args):
    cd_cmd = BASE_URL
    prefix = ''
    last_used_index = 0
    for i, letter in enumerate(args):
        prefix += letter
        all_paths = ls(cd_cmd)
        available_paths = list(filter(lambda p: startsWith(prefix, p), all_paths))
        if len(available_paths) == 0:
            if i < len(args):
                cprint(Fore.YELLOW, "[WARNING]: arg %s not used\nMoved to: %s\n" % (
                    args[last_used_index:], cd_cmd))
            return cd_cmd
        elif len(available_paths) == 1:
            cd_cmd = os.path.join(cd_cmd, available_paths[0])
            prefix = ''
            last_used_index = i+1
    if len(prefix) != 0:
        cprint(Fore.RED, str(map(str, available_paths)))
        sys.exit(-1)
    return cd_cmd

def main():
    args = check_args()
    cmd = build_cd(args)
    print ("cd " + cmd)

main()
