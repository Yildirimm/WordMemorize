import csv
import os.path
import tempfile

import pandas as pd

from tempfile import NamedTemporaryFile
import shutil

file_name = "word_files/words.csv"
file_name2 = "words_up.csv"
header = ["word_cat", "last_date", "word_itself", "en", "tr", "correct_count"]
ENCODING = "utf-32"

class word_class:

    def __init__(self, word_cat, last_date, word_itself, trans1, trans2, correct_count=0):
        #self.index = index
        self.word_cat = word_cat
        self.last_date = last_date
        self.word_itself = word_itself
        self.trans1 = trans1
        self.trans2 = trans2
        self.correct_count = correct_count

    def save_to_file(self):
        '''
        Saves the given word to a file
        '''
        word_record = [self.word_cat, self.last_date, self.word_itself,
                       self.trans1, self.trans2, self.correct_count]

        file_exists = os.path.isfile(file_name)

        with open(file_name, "a", newline="", encoding=ENCODING) as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(header)

            writer.writerow(word_record)

        print("Saved to file")

    def read_the_record(self, num):
        '''
        Gets num parameter and returns the regarding row
        :param num:
        :return: row of file [pandas]
        '''

        print('Read the records')
        data = pd.read_csv(file_name, encoding=ENCODING)
        interested_row = data.iloc[num, :]

        return interested_row

    def update_the_record(self, idx, data_frame):
        '''
        Takes a specific row and id of it and updates the recording
        :param idx: id of a row
        :param count:
        :param date:
        :return: None
        '''

        print(f"updated row is {data_frame.loc[idx,:]}")
        data_frame.to_csv(file_name, index=False, encoding=ENCODING)

        print('successfully updated\n')

    def is_exist(self, word_to_check):
        '''
        Gets a word to check the existence of it to avoid duplicates
        :param word_to_check:
        :return: True (Exist) or False (Dont Exist)
        '''

        with open(file_name, 'r', encoding=ENCODING) as f1:

            for line in f1:
                splits = line.split(',') # returns list

                if splits[2].strip().casefold() == word_to_check.strip().casefold():  # case insensitive comparison
                    #print(splits[2].strip().casefold(),
                    #      word_to_check.strip().casefold())
                    print('This word exists\n')
                    print('Add another word')
                else:
                    print('the word doesnt exist\n')
                    print("You can add this word")



