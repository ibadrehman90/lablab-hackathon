import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')

# generate headline for the ad
def generateCommands(prompt_txt,command):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="<<PROMPT>>",
        temperature=0.5,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    count = len(text.split())
    return text