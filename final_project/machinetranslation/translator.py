import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('vcIEht4zgylplesi758nkTkte8fBRKuKd2YDZmM82Zl-')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/edf436ef-933d-488b-b8b4-4c98e9d22f4c')


languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    # Translation code from English to French
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    # Translation code from French to English
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']
    return english_text
