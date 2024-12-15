import requests
import pandas as pd
import matplotlib.pyplot as plt


#1. pobieranie danych z publicznego API
url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"

response_users = requests.get(url_users)
response_posts = requests.get(url_posts)
response_comments = requests.get(url_comments)

#print(response_users)
#print(response_users.json())
#print(response_users.status_code)

if response_users.status_code == 200 and response_posts.status_code == 200 and response_comments.status_code == 200:
    data_users = response_users = response_users.json()
    data_posts = response_posts = response_posts.json()
    data_comments = response_comments.json()
else:
    raise Exception("Nie udało się pobrać danych")

#tworzenie dataframes
df_users = pd.DataFrame(data_users)
df_posts = pd.DataFrame(data_posts)
df_comments = pd.DataFrame(data_comments)

#print(df_users.to_string())


posts_per_user = df_posts.groupby('userId', as_index=False)['id'].count()
posts_per_user.rename(columns={'id': 'posts_count'}, inplace=True)
print(posts_per_user)