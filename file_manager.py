import os
import json

global dir_name, data_file, options_file

# Creates data files
def create_files():
    global dir_name, data_file, options_file

    data_file = 'data.txt'
    options_file = 'options.txt'

    if os.path.isfile(options_file):
        options = get_options()
        dir_name = str(options['DirName'])
    else:
        dir_name = 'Dir'
        print ('Error getting options...')

    if not os.path.exists(dir_name) and os.path.isfile(options_file):
        os.mkdir(dir_name)
        print('Creating directory...')

    if not os.path.isfile(os.path.join(dir_name, data_file)) and os.path.isfile(options_file):
        create_data_file()
        print('Creating data file...')

    if not os.path.isfile(options_file):
        create_options_file()
        print('Creating options file...')
        print('Please edit the options, then start the program again.')


# Create data file
def create_data_file():
    with open(os.path.join(dir_name, data_file), 'w') as f:
        f.write('')
        f.close()


# Create options file
def create_options_file():
    options = {
        'Timer': 10,
        'DirName': 'DataCollectorFiles'
    }

    with open(options_file, 'w') as f:
        json.dump(options, f)
        f.close()


# Write to data file
def write_to_data(data):
    with open(os.path.join(dir_name, data_file), 'w') as f:
        for item in data:
            f.write(item + '\n')
        f.close()


# Returns options
def get_options():
    with open(options_file, 'r') as f:
        data = json.load(f)
        f.close()

    return data
