#!/usr/bin/python3

import json
import pprint
import subprocess
import sys

def main(args):
    """ Main() """

    KEY = args[1]
    RHOST = args[2]
    COMMAND = args[3]

    ssh = subprocess.Popen(["ssh", "-i", KEY, RHOST, COMMAND],
                              shell=False,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

    osqdata = ssh.stdout.readlines()

    if osqdata == []:
        error = ssh.stderr.readlines()
        print(sys.stderr, " ERROR: %s ", error)
    else:
        results = jparse(osqdata)
        pprint.pprint(results)

def jparse(osqdata):
    results = []
    i = 1
    while i < (len(osqdata)-1):
        if i == (len(osqdata)-2):
            results.append(json.loads(osqdata[i].decode("utf-8")[:-1]))
        else: 
            results.append(json.loads(osqdata[i].decode("utf-8")[:-2]))
        i = i + 1
    return(results)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No Input: ./main <key-path> <user@rhost> <command>")
        sys.exit()
    else:
        main(sys.argv)