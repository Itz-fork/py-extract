# Copyright (c) 2021 - Itz-fork
# Project: py_extract
import subprocess

def run_cmd(command):
    run = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    shell_ouput = run.stdout.read()[:-1].decode("utf-8")
    return shell_ouput