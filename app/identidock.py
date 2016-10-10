from flask import Flask
app = Flask(__name__)

defalut_name = 'Joe Bloggs'

@app.route('/')
def get_identicion():
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

def hello_world():
    return 'Hello world\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
