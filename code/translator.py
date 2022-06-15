import json

# ------------------------------------------------------------------------------------- #
#                      Follows the standard of ISO 693-1                                #
#       More info + codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes        #
# ------------------------------------------------------------------------------------- #


# Defines Languages to dict ----------------------------------------------------------- # 
# -- Based on data from https://www.statista.com/statistics/957319/steam-user-language/ #    
lang_en = 'lang/source.en.json'     # English                                           
lang_sv = 'lang/source.sv.json'     # Swedish                                           
lang_de = 'lang/source.de.json'     # German                                            
lang_zh = 'lang/source.zh.json'     # Chinese (Simplified)                              
lang_ru = 'lang/source.ru.json'     # Russian                                         
# Spanish - es                                                                          
# portuguese (Brazil) - pr                                                              
# french - fr                                                                           
# japanese - jp                                                                         
                                                                                        
                                                                                        
languages = {
    0: lang_en, 
    1: lang_sv,
    2: lang_de,
    3: lang_zh,
    4: lang_ru
}
current_language = languages[0] # Defaults to English 


# Setters and getters ----------------------------------------------------------------- # 
def set_language(index):
    global current_language
    current_language = index

def get_language(key):
    f = open(current_language, encoding='utf-8')
    data = json.load(f)

    keys = key.split("/")
    for key in keys:
        if key not in data: 
            print("ERROR: \"{k}\" missing from data! ".format(k=key), data)
            return ""
        tmp_data = data[key]

    f.close()
    return tmp_data



