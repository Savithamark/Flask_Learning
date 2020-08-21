from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")
# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')

app.config.from_object('config.Config')
# Flask app creation
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Actual app logic 
@app.route('/')
def home():
    return render_template('index.html')