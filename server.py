from flask import render_template, Flask
from video import video
from login import login

# Create the application instance
#app = connexion.FlaskApp(__name__, specification_dir='./')
app = Flask(__name__)
app.register_blueprint(video)
app.register_blueprint(login)
app.secret_key = 'REPLACE ME - this value is here as a placeholder.'
#app.secret_key = 'REPLACE ME - this value is here as a placeholder.'
# Read the swagger.yml file to configure the endpoints
#app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':


    app.run(host='0.0.0.0', port=5000, debug=True)
