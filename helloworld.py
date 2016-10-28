# helloworld
import sys


def GetArgs(else_string):
    """Returns all parameters (if there's any) with spaces between them,
    or the string specified.
    """
    args = ""
    if len(sys.argv) > 1:
        for s in sys.argv[1:]:  # ignoring first argument, aka the filename
            args += ' ' + s
        return args
    else:
        return " " + else_string


def main():
    name = GetArgs("world")
    print("Hello" + name + "!")

main()
