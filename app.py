from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return render_template('index.html', name=name)

### For reference, this is the /<name> route without render_template
# @app.route('/<name>', methods=['GET'])
# def hello_name(name):
#     return f'Hello, {name}!\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
