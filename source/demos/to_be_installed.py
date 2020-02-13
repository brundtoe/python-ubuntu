import subprocess

programs = {
    "build-essentials",
    "dkms",
    "gdebi",
    "gparted",
    "acl",
    "curl",
    "wget",
    "git",
    "hplip",
    "cifs-utils",
    "sqlite3",
    "libsqlite3-dev",
    "python3-pip",
    "patch",
    "libmysqlclient-dev"
}

def is_tool(name):
    from shutil import which
    return which(name) is None


installable = {program for program in programs if is_tool(program)}
#res = subprocess.run(["apt","policy","git"], capture_output=True)
print(installable)
