import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')


def generateTextBlob(topic,kw,buss_id):
    model, penalty, prompt_text = switch_buss_models(buss_id, topic, kw)
    response = openai.Completion.create(
        model=model,
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=250,
        top_p=1,
        frequency_penalty=penalty,
        presence_penalty=0,
        stop=["END"]
    )
    text = response['choices'][0]['text'].strip()
    return text

def switch_buss_models(buss_id,topic,kw):
    if buss_id == '1':
        return "<<custom model>>",1, "<<PROMPT>>"
    elif buss_id == '2':
        return "<<custom model>>",1
    else:
        return "text-davinci-003",0, "<<PROMPT>>"