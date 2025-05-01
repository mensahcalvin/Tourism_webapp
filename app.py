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

@app.route('/vacation/Beach')
def Beach():
    return render_template('Beach.html')

@app.route('/vacation/familytravel')
def familytravel():
    return render_template('familytravel.html')

@app.route('/vacation/budget')
def budget():
    return render_template('budget.html')

@app.route("\vacation/food")
def food():
     return render_template('food.html')

if __name__ == '__main__':
    app.run(debug=True)