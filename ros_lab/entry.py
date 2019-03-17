from .lab_shell.lab_shell import lab_shell

def main():
    shell = lab_shell()
    shell.cmdloop()