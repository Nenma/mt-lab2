import nlpcloud

key = open('keys.txt', 'r').readline()
client = nlpcloud.Client("nllb-200-3-3b", key)


# Default set of languages to have the text pass through
def default_pass(file):
    content = open(file, 'r').read()

    to_french = client.translation(content, 'eng_Latn', 'fra_Latn')
    to_french = to_french['translation_text']

    to_spanish = client.translation(to_french, 'fra_Latn', 'spa_Latn')
    to_spanish = to_spanish['translation_text']

    to_italian = client.translation(to_spanish, 'spa_Latn', 'ita_Latn')
    to_italian = to_italian['translation_text']

    to_german = client.translation(to_italian, 'ita_Latn', 'deu_Latn')
    to_german = to_german['translation_text']

    to_danish = client.translation(to_german, 'deu_Latn', 'dan_Latn')
    to_danish = to_danish['translation_text']

    to_hindi = client.translation(to_danish, 'dan_Latn', 'hin_Deva')
    to_hindi = to_hindi['translation_text']

    to_japanese = client.translation(to_hindi, 'hin_Deva', 'jpn_Jpan')
    to_japanese = to_japanese['translation_text']

    to_chinese = client.translation(to_japanese, 'jpn_Jpan', 'zho_Hans')
    to_chinese = to_chinese['translation_text']

    to_korean = client.translation(to_chinese, 'zho_Hans', 'kor_Hang')
    to_korean = to_korean['translation_text']

    to_romanian = client.translation(to_korean, 'kor_Hang', 'ron_Latn')
    to_romanian = to_romanian['translation_text']

    back_to_english = client.translation(to_romanian, 'ron_Latn', 'eng_Latn')
    back_to_english = back_to_english['translation_text']

    return back_to_english


if __name__ == '__main__':
    # def = default_pass('text.txt')

    txt = open('text.txt', 'r').read()
    prev_lang = 'eng_Latn'
    next_lang = str(input('Enter target language: '))
    while(next_lang != 'stop'):
        translation = client.translation(txt, prev_lang, next_lang)
        translation = translation['translation_text']
        print(translation)
        prev_lang = next_lang
        next_lang = str(input('Enter target language: '))
