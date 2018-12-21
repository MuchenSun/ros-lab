import sys
sys.path.append("..")
from src.labShell import labShell

def test():
    shell = labShell()
    shell.cmdloop()

test()