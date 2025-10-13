from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "This is a sample K8 Deployment Web-Page!!"

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
