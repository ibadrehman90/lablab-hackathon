import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')


def blogOutline(title, audience,buss_id):
    model, penalty, prompt_text = switch_buss_models(buss_id, title, audience)
    response = openai.Completion.create(
        model=model,
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=penalty,
        presence_penalty=0,
        stop=["END"]
    )
    text = response['choices'][0]['text'].strip()
    return text


def switch_buss_models(buss_id, title, audience):
    if buss_id == '1':
        return "<<custom model name>>",1,"<<PROMPT>>"
    elif buss_id == '2':
        return "<<custom model name>>",1
    else:
        return "text-davinci-003",0,"<<Prompt>>"