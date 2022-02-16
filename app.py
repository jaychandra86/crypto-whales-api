import gitup
import requests
import getTweet
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/v3/git/update")
def update():

    data = getTweet.getTweet(getTweet.loginToTwitter())
    res = "[" + ','.join(data) + "]"

    print("--- writing the data into api.json file")
    #f = open("/home/6reposts9/mysite/urls.txt", "w")
    f = open("api.json", "w")
    f.write(res)
    f.close()
    print("--- write complete")

    print("--- updating the file on github repo")
    gitup.updateRepo("res", "api.json", "update api.json")


    return "<p>404 not found</p>"

if __name__ == "__main__":
    app.run(port=3000, debug=True)
