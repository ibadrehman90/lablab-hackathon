import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')

def generateColdEmailBody(recepient, company, product, action, proposition, tone, sender):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="<<PROMPT>>",
        temperature=0.6,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text