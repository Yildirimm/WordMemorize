'''
Author: Yildirimm
'''

# link: https://zetcode.com/python/googletrans/
# https://pypi.org/project/googletrans/

import random
from datetime import date

import pandas as pd
from googletrans import Translator
# working version pip install googletrans==3.1.0a0

import word_operations as Wo
from word_operations import *
import utils
import file_operations

LANGUAGES= {0: 'de', 1: 'en', 2: 'tr'}
translator = Translator()

my_word = Wo.word_class
last_date = str(date.today())


print(50*"*")
print("Welcome to WordMemorize program...")
print("Choose the language that you want to practice!")

for i in LANGUAGES:
    print(i, LANGUAGES[i])
print(50*"*")

lang_choice = int(input("Please put the number of the language you want to practice:  "))

desired_lang = LANGUAGES[lang_choice]
other_langs = utils.get_other_languages(desired_lang, LANGUAGES)

# Ask the file name
file_to_study = file_operations.ask_file_name()

# ask for word input OR word_memorize
x = str(input("Would you like to add a word or memorize a word, press [a] or [m]\n"))


if x == "a":
    print(f'\n you pressed {x}\n')

    # if INPUT, then use INPUT operations
    # save the file
    while True:
        input_type, input_word = str(input("the input as word or sentence [w,s]: ")).split(",")
        print(type(input_word), input_word)

        source_lang = translator.detect(input_word).lang

        trans1 = translator.translate(input_word, src=source_lang, dest=other_langs[0]).text # en
        trans2 = translator.translate(input_word, src=source_lang, dest=other_langs[1]).text # tr

        my_word = Wo.word_class(word_cat=input_type, last_date=last_date,
                                word_itself=input_word, trans1=trans1, trans2=trans2)

        print(my_word.word_cat, "\n", my_word.word_itself,
              "\n", my_word.trans1, "\n", my_word.trans2)

        my_word.save_to_file()

        b = input("if you want to break entering words press b")
        if b == "b":
            break
        else:
            print('Unexpected error! Couldn\'t break the input loop')

elif x == "m":
    print(f'\n you pressed {x}\n')
    # if MEMORIZE, then use memorize operations
    # save the rows of file

    data = pd.read_csv(file_name, encoding="utf-32")

    row_size = round(len(data)/20)
    row_size = 2
    print(len(data), row_size)

    numbers = [random.randint(0, len(data)) for x in range(row_size)]
    print(numbers)

    for i, number in enumerate(numbers):

        the_date = str(data.loc[number, 'last_date'])
        the_word = str(data.loc[number, 'word_itself'])
        lang_trans_1 = str(data.loc[number, 'en'])
        lang_trans_2 = str(data.loc[number, 'tr'])
        the_count = data.loc[number, 'correct_count']
        # print(type(the_count))

        print(f'\nthe index {number}, {the_date}, {the_word}, {lang_trans_1}, {lang_trans_2}, {the_count}')

        # ask user for input
        the_input = str(input(f"\n ''{the_word}'' means in {other_langs[0].capitalize()} what? \n({lang_trans_1})"))

        if lang_trans_1.strip().casefold() == the_input.strip().casefold():
            print('Correct!')
            print(data.loc[number,:])
            the_count += 1
            the_count = str(the_count)
            the_date = last_date
            print(the_count, the_date)


            data.loc[number, ['correct_count']] = the_count
            data.loc[number, ['last_date']] = the_date

            my_word.update_the_record(self=my_word, idx=number, data_frame=data)
            print(data.loc[number,:])

        else:
            print('You entered it wrong')  # do nothing
            continue
else:
    raise "An error occurred while pressing key!"



# TODO: Get words from websites by requests
# TODO: Make different files for different word groups
# TODO: Record word score and update the file update function
# TODO: get words by image processing


