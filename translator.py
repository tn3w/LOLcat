import json
import re

TRANSLATIONS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lolcat_language_mapping.json")

with open(TRANSLATIONS_PATH, "r") as file:
    translations = json.load(file)

def translate_english_to_lolcat(english_text: str) -> str:
    """
    Translate English to LOLcat
    :param english_text: The text to be translated in English
    """

    def capitalize_first_letter(text):
        return text[0].upper() + text[1:]

    result = ''
    parts = re.split('(<.*?>)', english_text)
    
    for part in parts:
        if part.startswith('<'):
            result += part
        else:
            words = part.split(' ')
            translated_words = []
            
            for word in words:
                if word == '':
                    translated_words.append('')
                    continue
                
                translation_found = False
                
                for translation in lolcat_data:
                    if str(word).lower() == str(translation["q"]).lower():
                        translation_found = True
                        translated_words.append(translation["r"])
                        break
                
                if not translation_found:
                    translated_words.append(word)
                    
            result += ' '.join(translated_words)
    
    return capitalize_first_letter(result)
