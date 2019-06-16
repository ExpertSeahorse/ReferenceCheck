import json
movie = {}
movie["title"] = "Matrix"
movie["director"] = "The Wachowski Brothers"
movie["composer"] = None
movie["actors"] = ["Keanu Reeves", "Laurence Fishburñ", "Carrie-Anne Moss", "Hugo Weaving", "Gloria Foster"]
movie["is awesome"] = True
movie["budget"] = 63000000

with open("Matrix_stats.txt", "w", encoding="utf-8") as file:
    json.dump(movie, file, ensure_ascii=False)
