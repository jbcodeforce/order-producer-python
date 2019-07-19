from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Jbcodeforce on Openshift Hello to you!"

if __name__ == "__main__":
    application.run()
