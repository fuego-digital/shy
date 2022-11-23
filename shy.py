from colorama import Fore as f
import os
import sys

def success(text):
    print(f'{f.GREEN}[+]{f.WHITE} {text}')

def error(text):
    print(f'{f.RED}[X]{f.WHITE} {text}')

def info(text):
    print(f'{f.BLUE}[i]{f.WHITE} {text}')

def warning(text):
    print(f'{f.YELLOW}[/]{f.WHITE}{text}')

def ask(text):
    print(f'{f.BLUE}[?]{f.WHITE} {text}')
    return input('> ')

os.system('cls')
try:
    filename = sys.argv[1]
except:
    error('Name not provided. Try running something like "shy project"')

info(f'Creating project "{filename}"...')
try:
    os.system(f'md {filename} && cd {filename}')
except:
    error('Something wrent wrong...')
info(f'Created dir.')

info('Changing directory...')

os.chdir(filename)

info('Running "npm init"...')
try:
    os.system(f'npm init -y')
except:
    error(f'Something wrent wrong...')

info('Creating "index.js"...')

os.system('echo console.log("Hello, World!"); > index.js')

modules = ask('Install any other modules? Split them with commas & no spaces. (express,chalk)')

modules = modules.split(',')

for module in modules:
    info(f'Installing "{module}"...')
    os.system(f'npm i {module}')
