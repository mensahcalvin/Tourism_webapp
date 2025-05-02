from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

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

# Route to handle user form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save user details to the database
    new_user = User(name=name, email=email, message=message)
    db.session.add(new_user)
    db.session.commit()

    return "Thank you for contacting us!"

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

@app.route("/vacation/food")
def food():
    return render_template('food.html')

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
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

@app.route("/vacation/food")
def food():
    return render_template('food.html')

if __name__ == '__main__':
    app.run()