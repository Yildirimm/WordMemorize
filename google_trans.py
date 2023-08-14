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

import Word_operations as Wo
from Word_operations import *
import utils


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

    data = pd.read_csv(file_name, encoding='unicode_escape')
    row_size = round(len(data)/20)
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

        if lang_trans_2.strip().casefold() == the_input.strip().casefold():
            print('Correct!')
            print(data.loc[number,:])
            the_count += 1
            the_count = str(the_count)
            the_date = last_date
            print(the_count, the_date)

            # TODO: Record the counts to the csv file (currently missing)
            # data.to_csv(file_name, index=False)
            data.loc[number, ['correct_count']] = the_count
            data.loc[number, ['last_date']] = the_date

            my_word.update_the_record(idx=number, row=data.loc[number,:])

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



'''
    op = open(file_name, "r")
    dt = csv.DictReader(op)

    up_dt = []
    numbers = [random.randint(1, len(data)) for x in range(3)]

    flag = True

    for idn, number in enumerate(numbers):
        # number = random.randint(1, len(data))
        print(idn, numbers)

        r = data.iloc[number, :]

        #print(idx, number)
        the_date = str(r['last_date'])
        the_word = str(r['word_itself'])
        the_en = str(r['en'])
        the_tr = str(r['tr'])
        the_count = int(r['correct_count'])
        print(type(the_count))

        print(f'the index {number}, {the_date}, {the_word}, {the_en}, {the_tr}, {the_count}')

        # ask user for input
        the_input = str(input(f"\nwhat does {the_word} mean in English? \n({the_en})"))

        if the_en == the_input:
            the_count += 1
            the_count = str(the_count)
            the_date = last_date
            print(the_count, the_date)

        row = {'word_cat': r['word_cat'],
               'last_date': the_date,
               'word_itself': r['word_itself'],
               'en': r['en'],
               'tr': r['tr'],
               'correct_count': the_count
               }
        up_dt.append(row)

        print("HERE YOU ARE")
        
        a = input("to break the cycle put b")
        if a == "b":
            flag = False
        else:
            flag = True
            idx = 0
            continue'''

'''

    print("out of the while")
    print(up_dt)
    op.close()

    op = open(file_name2, "a", newline='')
    headers = ['word_cat', 'last_date', 'word_itself', 'en', 'tr', 'correct_count']
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    data.writerows(up_dt)

    op.close()

'''

# TODO: close the program
'''
# data = ['Dobrý deň', 'majestátny orol', 'krehká dohoda']
data = str(input('put the word you want to translate: '))

source_lang = translator.detect(data).lang
translated = translator.translate(data, src=source_lang, dest='en')
print(translated.text)#, '\n',translated.parts.__getitem__(0) )#,'\n', str(translated.extra_data['parts']))
'''
