from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Add more routes as needed for your other pages
# @app.route('/another_page')
# def another_page():
#     return render_template('another_page.html')

if __name__ == '__main__':
    app.run(debug=True)
