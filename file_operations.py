'''
Handles file operations regarding the txt files
'''

import os


def read_txt_file_names(directory="./word_files"):
    """
    Retuns the names of files in a directory as a list
    :param directory: [string]
    :return: [list]
    """
    txt_files = os.listdir(directory)
    return txt_files

def ask_file_name():
    """
    Ask user to choose the txt/csv file for studying. Words of the chosen file will be asked
    :return: file name
    """
    files = read_txt_file_names()
    for i, file_name in enumerate(files):
        print(i, file_name)
    choice = int(input("Please put the number of the file that you want to work on: "))
    return files[choice]

