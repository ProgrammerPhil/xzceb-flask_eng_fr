""" Translator Python Code using IBM Language Translator"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-15',
    authenticator=authenticator
)

language_translator.set_service_url(url)

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

def english_to_french(english_text):
    """ English to French Translation Code """

    e2f_translation = language_translator.translate(
        text=str(english_text),
        model_id='en-fr').get_result()
    #print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    french_text = e2f_translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ French to English Translation Code """

    f2e_translation = language_translator.translate(
        text=str(french_text),
        model_id='fr-en').get_result()
    #print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    english_text = f2e_translation['translations'][0]['translation']
    return english_text

if __name__ == '__main__':
    english_to_french("Hello")
