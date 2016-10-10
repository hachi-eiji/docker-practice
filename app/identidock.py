from flask import Flask, Response
import requests

app = Flask(__name__)

defalut_name = 'Joe Bloggs'

@app.route('/')
def mainpage():
    name = defalut_name

    html = '''<html>
    <head><title>Identidock</title></head>
    <body>
    <form method="POST">
    Hello <input type="text" name="name" value="{}"/>
    <input type="submit" value="submit" />
    </form>
    <p> you look like a:
    <img src="/monster/monster.png" />
    </body>
    </html>
    '''.format(name)
    return html

@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = r.content
    return Response(image, mimetype='image/png')

def hello_world():
    return 'Hello world\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
