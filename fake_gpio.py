import sys

sys.stderr.write("WARNING: using fake GPIO\n")

BOARD="board"
OUT="out"

def setmode(mode):
    print("Fake setmode({})".format(mode))

def setup(pin, direction):
    print("Fake setup({}, {})".format(pin, direction))

def output(pin, value):
    print("Fake output({}, {})".format(pin, value))

def cleanup():
    print("Fake cleanup()")
