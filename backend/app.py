from Modules.BlogPost import ShortBlogIntro,ShortBlogBody
from Modules.TextBlob import generateTextBlob
from Modules.BlogOutline import blogOutline
from Modules.ContentImprover import improveContent,CWrewritten
from Modules.ColdEmail import generateColdEmailBody
from Modules.Commands import generateCommands
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.app_context().push()
CORS(app,support_credentials=True)


@app.route("/blogpost/intro",methods=['POST'])
def shortBlogPostIntro():
    title = request.json['title']
    tone = request.json['tone']
    audience = request.json['audience']
    res = ShortBlogIntro(title,tone,audience)
    return jsonify(res)

@app.route("/blogpost/body",methods=['POST'])
def shortBlogPostBody():
    title = request.json['title']
    outline = request.json['outline']
    keywords = request.json['keyword']
    res = ShortBlogBody(title,outline,keywords)
    return jsonify(res)

@app.route("/textblob/content",methods=['POST'])
def genTextBlob():
    topic = request.json['topic']
    kw = request.json['kw']
    buss_id = request.json['buss_id']
    res = generateTextBlob(topic,kw,buss_id)
    return jsonify(res)

@app.route("/contentimprover/content",methods=['POST'])
def contentImprover():
    text = request.json['text']
    tone = request.json['tone']
    buss_id = request.json['buss_id']
    if (buss_id == "1"):
        res = CWrewritten(text,tone)
    else:
        res = improveContent(text,tone)
    return jsonify(data=res)

@app.route("/article/outline",methods=['POST'])
def articleOutline():
    title = request.json['title']
    audience = request.json['audience']
    buss_id = request.json['buss_id']
    res = blogOutline(title,audience,buss_id)
    return jsonify(data=res)

@app.route("/coldemail/body",methods=['POST'])
def genColdEmailBody():
    recepient = request.json['recepient']
    company = request.json['company']
    product = request.json['product']
    action = request.json['action']
    proposition = request.json['proposition']
    tone = request.json['tone']
    sender = request.json['sender']
    res = generateColdEmailBody(recepient,company,product,action,proposition,tone,sender)
    return jsonify(data=res)

@app.route("/commands/content",methods=['POST'])
def genCommands():
    prompt = request.json['prompt']
    commands = request.json['commands']
    res = generateCommands(prompt,commands)
    return jsonify(data=res)