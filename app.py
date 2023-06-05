from flask_cors import cross_origin
from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
@cross_origin()

def homepage():
    if request.method == 'POST':
        text = request.form['speech']
        language = 'en'

        myobj = gTTS(text=text, lang=language, slow=False)

        myobj.save("static/welcome.mp3")

        os.system("mpg321 welcome.mp3")
        path='static/welcome.mp3'


        return send_file(path, as_attachment=True)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(port=5000, debug=True)