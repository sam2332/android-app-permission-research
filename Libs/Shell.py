import subprocess, json, os,sys
import re


def run_shell(
    cmd,
    debug=False,
    returns_POpen=False,
    close_fds=False,
    splitlines=True,
    split_other=None,
    split_type="str",
    extraction=None,
    cwd=None
):
    if cwd is None:
        cwd = os.getcwd()
        
    if debug:
        print(cmd)

    if returns_POpen:
        process = subprocess.Popen(cmd, close_fds=close_fds)
        return process
    if type(cmd) == str:
        cmd = cmd.split(" ")
    process = subprocess.run(cmd, stdout=subprocess.PIPE, cwd=cwd)
    data = process.stdout.decode("utf-8").strip()
    if split_other is not None and not splitlines:
        if split_type == "str":
            data = data.split(split_other)
        elif split_type == "regex":
            data = re.split(split_other, data)

    if splitlines and split_other is None:
        data = data.splitlines()

    if extraction is not None:
        results = []
        for line in data:
            out = re.match(extraction, line)
            if out is not None:
                results.append(out.groups())

        return results
    return data
