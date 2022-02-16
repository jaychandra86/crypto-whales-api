from github import Github

def loginToGitHub():
    g = Github("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")
    print("--- Login successful")

    return g


def createRepo(repoName, fileName, commitMessage, branchName):
    g = loginToGitHub()

    user = g.get_user()

    repo = user.create_repo(repoName)
    print(f"--- {repoName} created successfully")

    #get the repo
    repo = g.get_repo(f"{user.login}/{repoName}")

    f = open("api.json", "r")
    fileContent = f.read()
    f.close()

    #create a file
    repo.create_file(fileName, commitMessage, fileContent, branch=branchName)
    print(f"--- File {fileName} created on {branchName} branch")



def updateRepo(repoName, fileName, commitMessage):
    g = loginToGitHub()

    user = g.get_user()

    repo = g.get_repo(f"{user.login}/{repoName}")

    fileContents = repo.get_contents(f"./{fileName}")

    f = open(fileName, "r")
    newContent = f.read()
    f.close()

    repo.update_file(fileContents.path, commitMessage, newContent, fileContents.sha)
    print("--- File updated successfully")


#updateRepo("res", "api.json", "update api.json")
#createRepo("test", "api.json", "first commit", "master")

if __name__ == "__main__":
    print("--- no method specified")
