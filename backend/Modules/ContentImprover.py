import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')

# convesio text generation
def improveContent(text,tone):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="<<PROMPT>>",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text

def CWrewritten(text,tone):
    response = openai.Completion.create(
        model="<<custom model>>",
        prompt="<<PROMPT>>",
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.9,
        presence_penalty=0,
        stop=["END"]
    )
    text = response['choices'][0]['text'].strip()
    return text


def switch_buss_models(buss_id):
    if buss_id == '1':
        return "<<custom model>>",1
    elif buss_id == '2':
        return "<<custom model>>",1
    else:
        return "text-davinci-003",0