# how to connect to an API using python

import requests


base_url = 'https://pokeapi.co/api/v2/'


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    res = requests.get(url)

    if res.status_code == 200:
        pokemon_data = res.json()
        # print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to retrieved data {res.status_code}")


pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f'name : {pokemon_info["name"].capitalize()}')
    print(f'id : {pokemon_info["id"]}')
    print(f'Height : {pokemon_info["height"]}')
    print(f'Weight : {pokemon_info["weight"]}')
