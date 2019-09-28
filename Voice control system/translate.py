from google.cloud import translate

client = translate.Client()
def detect(str1):
    return client.detect_language(str1)["language"]
def translate(str1):
    return client.translate(str1)["translatedText"]#,target_language="en-US")
def translate_hindi(str1):
    return client.translate(str1,target_language="hi")["translatedText"]#,target_language="en-US")
