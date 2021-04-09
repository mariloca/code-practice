import requests

#Make an API call and store the response.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status Code:", r.status_code) #code 200 indicates a successful response

#Store API response in a variable
response_dict=r.json() #json() converts information to a dict
print("Total repositories: ", response_dict['total_count'])

#Explore information about the repositories
repo_dicts=response_dict['items']
print("Repositories returned:", len(repo_dicts))

#Examine the first repositories
repo_dict=repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#	print(key)

print("\nSelected information about first respository:")
for repo_dict in repo_dicts:
	print("\nName:", repo_dict['name'])
	print("Owner:", repo_dict['owner']['login'])
	print("Stars:", repo_dict['stargazers_count'])
	print("Repository:", repo_dict['html_url'])
	print("Description:", repo_dict['description'])


#Process results.
#print(response_dict.keys())