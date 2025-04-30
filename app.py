from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/vacation')
def vacation():
    return render_template('vacation.html')

@app.route('/flight')
def flight():
    return render_template('flight.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Tourism')
def Tourism():
    return render_template('Tourism.html')

@app.route('/blog/category1')
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