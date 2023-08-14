

def get_other_languages(chosen_lang_val, dict_name):
    ohter_lang_names= []

    for key, value in dict_name.items():
        if value != chosen_lang_val:
           ohter_lang_names.append(value)

    return ohter_lang_names