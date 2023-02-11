from flask import Flask, render_template, url_for


app = Flask(__name__)
posts = [
    {
        'author': 'Florin Hegedus',
        'title': 'First Blog Post',
        'content': 'Content 1',
        'date': 'April 20, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog Post',
        'content': 'Content 2',
        'date': 'April 21, 2023'
    },
]


@app.route('/')
@app.route('/home')
def hello():
   return render_template('home.html', posts=posts)


@app.route('/about')
def about():
   return render_template('about.html', title='About')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9090, debug=True)