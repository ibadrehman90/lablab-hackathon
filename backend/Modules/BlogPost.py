import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')


def ShortBlogIntro(title,tone,audience):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="<<PROMPT>>",
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text

def ShortBlogBody(title,outline,keywords):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="<<PROMPT>>",
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text