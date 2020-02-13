# tjek for installation
import subprocess

def is_installed(program):
    res = subprocess.run(['which',program], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode is 0


if __name__ == "__main__":
    program = 'wget'
    if is_installed(program):
        print( f"{program} er installeret")
        exit(0)
    print(f'{program} er ikke installeret')
