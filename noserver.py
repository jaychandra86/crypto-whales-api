import gitup
import getTweet

print("--- getting the tweets and creating a json")
data = getTweet.getTweet(getTweet.loginToTwitter())
res = "[" + ','.join(data) + "]"

print("--- writing the data into api.json file")
f = open("api.json", "w")
f.write(res)
f.close()
print("--- write complete")

print("--- updating the file on github repo")
gitup.updateRepo("res", "api.json", "update api.json")
print("--- update successful")
