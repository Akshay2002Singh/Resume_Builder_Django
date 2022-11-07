import requests
import json

username = "Akshay2002Singh"
apistring = f"https://api.github.com/users/{username}/repos"
key = "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"
headers = {"Authorization": f"Bearer {key}"}
jsonresponse = requests.get(apistring, headers=headers).json()
# print(jsonresponse)
best_repos = list()
all_repos = list()
c = 1
for repos in jsonresponse:
    if repos["fork"] == False and repos["name"] != username:
        repo_name = repos["name"]
        if repos["description"] != None:
            best_repos.append(
                {
                    "name": repos["name"],
                    "description": repos["description"],
                }
            )
            c += 1
        else:
            all_repos.append({"name": repos["name"]})

if len(best_repos) < 6:
    for i in range(0, len(all_repos)):
        repo_dict = all_repos[i]
        repo_name = repo_dict["name"]
        repo_url = f"https://api.github.com/repos/{username}/{repo_name}/contributors"
        repojson = requests.get(repo_url, headers=headers).json()
        all_repos[i].update({"commits": repojson[0]["contributions"]})
    all_repos.sort(key=lambda r: r["commits"], reverse=True)
    all_repos = all_repos[:6]
    # print(all_repos)
    for j in range(len(best_repos), len(all_repos)):
        repo_name = all_repos[j]["name"]
        languages_used = list()
        languagejson = requests.get(
            f"https://api.github.com/repos/{username}/{repo_name}/languages",
            headers=headers,
        ).json()
        for key in languagejson:
            languages_used.append(key)

        desc = "This project is made using "
        desc += str(languages_used[0])
        if len(languages_used) == 1:
            desc += "."
        else:
            for i in range(1, len(languages_used) - 1):
                desc = desc + ", " + str(languages_used[i])
            desc = desc +", " + str(languages_used[-1]) + "."
        # all_repos[j].update({"languages_used": languages_used})
        best_repos.append({
            "name": repo_name,
            "description": desc,
        })
    print(best_repos)
