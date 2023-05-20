import csv
import os.path
import tempfile

import pandas as pd

from tempfile import NamedTemporaryFile
import shutil

file_name = "words.csv"
file_name2 = "words_up.csv"
header = ["word_cat", "last_date", "word_itself", "en", "tr", "correct_count"]


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
        word_record = [self.word_cat, self.last_date, self.word_itself,
                       self.trans1, self.trans2, self.correct_count]

        file_exists = os.path.isfile(file_name)

        with open(file_name, "a", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(header)

            writer.writerow(word_record)

        print("saved to file")

    def read_the_record(self, num):
        '''
        with open(file=file_name) as f_r:
            reader_r = csv.reader(f_r)
            interested_row = [row for idx, row in enumerate(reader_r) if idx == num]

            return interested_row'''

        print('read the records')
        data = pd.read_csv(file_name)
        interested_row = data.iloc[num, :]
        return interested_row

    def update_the_record(self, idx, row):
        '''with open(file_name, 'w') as output:
            writer = csv.DictWriter(output, fieldnames=header)
            writer.writerow({'word_cat': the_row[0][0],
                             'last_date': [0][1], 'word_itself': [0][2], 'en': [0][3],
                             'tr': [0][4], 'correct_count': [0][5]})

        with open(file_name, 'w') as upd:
            upd.writelines(the_row)
        '''

        with open(file_name, 'r', encoding='utf-8') as csvfile:
            with open(file_name, 'w', encoding='utf-8') as tempfile:
                reader = csv.DictReader(csvfile, fieldnames=header)
                writer = csv.DictWriter(tempfile, fieldnames=header)

                for row in reader:
                    # if row['ID'] == str(stud_ID):
                    #    print('updating row', row['ID'])
                    #    row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
                    # row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
                    # writer.writerow(row)
                    row = {"word_cat": row["word_cat"], "last_date": row["last_dat"],
                           "word_itself": row["word_itself"], "en": row["en"],
                           "tr": row["tr"], "correct_count": row["correct_count"]}
                    writer.writerow(row)

        shutil.move(tempfile.name, file_name)

        print('successfully updated\n')

    def is_exist(self, word_to_check):
        '''
        Gets a word to check the existence of it to avoid duplicates
        :param word_to_check:
        :return: True (Exist) or False (Dont Exist)
        '''
