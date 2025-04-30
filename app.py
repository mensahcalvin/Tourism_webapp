from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog/category2')
def category1():
    return render_template('category1.html')

@app.route('/blog/category2')
def category2():
    return render_template('category2.html')

@app.route('/blog/category3')
def category3():
    return render_template('category3.html')

if __name__ == '__main__':
    app.run(debug=True)