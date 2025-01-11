def append_to_file(address, txt):
    try:
        with open(address, 'a') as file:
            file.write(str(txt))
    except IOError:
        print('Error: Unable to access the file')

def write_to_file(address, txt='Empty'):
    try:
        with open(address, 'w') as file:
            file.write(str(txt))
    except IOError:
        print('Error: Unable to access the file')

def read_from_file(address):
    try:
        with open(address, 'r') as file:
            return file.read()
    except IOError:
        print('Error: Unable to access the file')
