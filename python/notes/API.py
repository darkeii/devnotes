# How to connect to an API using python
# https://pokeapi.co/api/v2/

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)                # it is a response object.              like # 404 is reponse code for "Not found"
    print(response)                             # response codes grouped in 5 classes : 100-199 (Info responses)
                                                #                                       200-299 (Successful responses)          # this is what we need
                                                #                                       400-499 (Client error responses)
                                                #                                       500-599 (server error reponses)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code}")

pokemon_name = "arbok"
pokemon_info = get_pokemon_info(pokemon_name)           # stored all the dictionary data in a self defined variable.

if pokemon_info:
    print(f"name: {pokemon_info["name"]}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    print(f"weight: {pokemon_info["weight"]}")





