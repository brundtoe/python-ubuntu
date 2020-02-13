# Tjek installationen af et program
def is_tool(name):
    from shutil import which
    return which(name) is not None

if __name__ == "__main__":
    print(is_tool('curl'))
    print(is_tool('wget'))
    print(is_tool('synaptic'))

## todo which kan kun finde programmer eksempelvis finder den ikke
## libsqlite3-dev selvom det er installeret





