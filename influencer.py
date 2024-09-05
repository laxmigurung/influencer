"""
Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication. 
Write a Python script that makes a request to your selected API, using the appropriate endpoint and parameters to retrieve data. 
Save the response data to a variable, and handle it as JSON to work with nested structures. 
Extract a specific item from the nested dictionary in the response, and print a statement that meaningfully displays this information. 
Have fun exploring the data you retrieve!
"""

import requests

URL = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-posts"

querystring = {"linkedin_url":"https://www.linkedin.com/in/williamhgates/","type":"posts"}

headers = {
	"x-rapidapi-key": "31a5a664b6mshf5194e9db5bced2p14db50jsn7f71ff4a40c1",
	"x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
}

def get_data():
    response = requests.get(URL, headers=headers, params=querystring)
    return response.json()["data"]

# ['images', 'num_appreciations', 'num_comments', 'num_empathy', 'num_interests', 'num_likes', 'num_praises', 'num_reposts', 
# 'post_url', 'posted', 'poster_linkedin_url', 'reshared', 'text', 'time', 'urn', 'video']

# goal is to collect the profile of those who meets the conditions to be called as INFLUENCER.
def transform_data(data):
    popular_profiles = []
    for item in data:
        if item["num_comments"] > 500 and item["num_appreciations"] > 100 and item["num_reposts"] > 10:
            popular_profiles.append(item["poster_linkedin_url"])
    return popular_profiles



data = get_data()
influencer = transform_data(data)
