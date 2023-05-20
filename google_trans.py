'''
Author: Yildirimm
'''

## link: https://zetcode.com/python/googletrans/
## https://pypi.org/project/googletrans/

import random
from datetime import date

import pandas as pd
from googletrans import Translator
# working version pip install googletrans==3.1.0a0

import Word_operations as wo
from Word_operations import *

LANGUAGE_SET = {'de', 'en', 'tr'}
translator = Translator()

my_word = wo.word_class
last_date = str(date.today())

## TODO: ask for word input OR word_memorize
x = str(input("Would you like to add a word or memorize a word, press [a] or [m]\n"))


if x == "a":
    print('\n you pressed a\n')

    ## TODO: if INPUT, then use INPUT operations
    ## TODO: save the file
    while True:
        input_type, input_word = str(input("the word as word or sentence [w,s]: ")).split(",")
        print(type(input_word), input_word)

        source_lang = translator.detect(input_word).lang

        trans1 = translator.translate(input_word, src=source_lang, dest="en").text
        trans2 = translator.translate(input_word, src=source_lang, dest="tr").text

        my_word = wo.word_class(word_cat=input_type, last_date=last_date,
                                word_itself=input_word, trans1=trans1, trans2=trans2)

        print(my_word.word_cat, "\n", my_word.word_itself,
              "\n", my_word.trans1, "\n", my_word.trans2)

        my_word.save_to_file()





        b = input("if you want to break entering words press b")
        if b == "b":
            break
        else:
            print('wo.read_the_record(10)')



elif x == "m":
    print('\n you pressed m\n')
    ## TODO: if MEMORIZE, then use memorize operations
    ## TODO: save the rows of file

    data = pd.read_csv(file_name, encoding='unicode_escape')
    the_size = round(len(data)/20)
    print(len(data), the_size)

    numbers = [random.randint(0, len(data)) for x in range(the_size)]
    print(numbers)

    for i, number in enumerate(numbers):

        the_date = str(data.loc[number, 'last_date'])
        the_word = str(data.loc[number, 'word_itself'])
        the_en = str(data.loc[number, 'en'])
        the_tr = str(data.loc[number, 'tr'])
        the_count = data.loc[number, 'correct_count']
        # print(type(the_count))

        print(f'\nthe index {number}, {the_date}, {the_word}, {the_en}, {the_tr}, {the_count}')

        # ask user for input
        the_input = str(input(f"\n{the_word} means in English what? \n({the_en})"))

        if the_en == the_input:
            the_count += 1
            the_count = str(the_count)
            the_date = last_date
            print(the_count, the_date)

            ## TODO: Record the counts to the csv file (currently misisng)
            # data.to_csv(file_name, index=False)
        else:
            print('You entered it wrong')  # do nothing

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

## TODO: close the program
'''
# data = ['Dobrý deň', 'majestátny orol', 'krehká dohoda']
data = str(input('put the word you want to translate: '))

source_lang = translator.detect(data).lang
translated = translator.translate(data, src=source_lang, dest='en')
print(translated.text)#, '\n',translated.parts.__getitem__(0) )#,'\n', str(translated.extra_data['parts']))
'''
