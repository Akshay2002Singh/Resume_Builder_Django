import requests
import json
username="Akshay2002Singh"
apistring=f"https://api.github.com/users/{username}/repos"
headers={"Authorization":"Bearer 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"}
jsonresponse=requests.get(apistring,headers=headers).json()
best_repos=dict()
all_repos=list()
c=1
for repos in jsonresponse:
     if repos["fork"]==False and repos["name"]!=username:
         all_repos.append({
        "name": repos["name"]})
         repo_name=repos["name"]
         if repos["description"]!=None:
                    best_repos.update({
                        f"{c}":
                        {
                        "name":repos["name"],
                        "description":repos["description"],
                        }
                    }
                    )
                    c+=1
if len(best_repos)<6:
    for i in range(0,len(all_repos)):
        repo_dict=all_repos[i]
        repo_name=repo_dict["name"]
        repo_url=f"https://api.github.com/repos/akshay2002singh/{repo_name}/contributors"
        repojson=requests.get(repo_url,headers=headers).json()
        all_repos[i].update({
            "commits":repojson[0]["contributions"]
        })
    all_repos.sort(key=lambda r:r["commits"],reverse=True)
    all_repos=all_repos[:6]
    print(all_repos)
    for j in range(0,len(all_repos)):
        repo_name=all_repos[j]["name"]
        languages_used=list()
        languagejson=requests.get(f"https://api.github.com/repos/{username}/{repo_name}/languages",headers=headers).json()
        for key in languagejson:
               languages_used.append(key)
        all_repos[j].update({
            "languages_used":languages_used
            })
    print(all_repos)


 
