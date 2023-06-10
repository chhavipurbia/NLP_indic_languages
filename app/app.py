from flask import Flask, render_template, request, jsonify
from indicnlp.tokenize import sentence_tokenize

app = Flask(__name__)

sentences = []  # List to store the sentences

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']
        sentences.clear()  # Clear the sentences list before populating it again
        sentences.extend([(sentence, False) for sentence in sentence_tokenize.sentence_split(text, lang=lang)])

        return render_template('index.html', sentences=sentences)

    return render_template('index.html')

@app.route('/edit', methods=['POST'])
def edit():
    sentence_number = int(request.form['sentence_number'])
    edited_sentence = request.form['edited_sentence']

    if sentence_number < 1 or sentence_number > len(sentences):
        return jsonify({'error': 'Invalid sentence number.'}), 400

    sentences[sentence_number - 1] = (edited_sentence, True)

    return render_template('index.html', sentences=sentences)

if __name__ == '__main__':
    app.run(debug=True)
