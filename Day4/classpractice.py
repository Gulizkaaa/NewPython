movies = [
    {'name': 'The Shawshank Redemption', 
    'year of release': 'October, 1994', 
    'director': 'Frank Darabount', 
    'main actors': '["Morgan Freeman", "Tim Robbins"]'},  
    {'name': 'Forrest Gump', 
    'year of release': 'July, 1994', 
    'director': 'Robert Zemeckis', 
    'main actors': '[Tom Hanks, Robin Wright]'} ]


#print(movies[0]["director"], movies[1]["director"])

# for movie in movies: #iterating inside of a list ----> goes through the dictinoary
#     print("---------------------")
#     for info in movie.items(): # second loop is iterating inside of a dictionary 
#     #-------> goes through keys and values
#         print(info)

for movie in movies:
    print("Movie name is:", movie["name"], "Movie year of release is:", movie["year of release"])