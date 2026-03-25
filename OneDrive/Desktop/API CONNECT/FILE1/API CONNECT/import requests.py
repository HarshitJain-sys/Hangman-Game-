import requests
base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url) #response is a object

    if response.status_code==200:
        #print("Data Retrieved")
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive the data {response.status_code} ")
pokemon_name="bulbasaur"
pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name :{pokemon_info["name"].capitalize()}")
    print(f"ID :{pokemon_info["id"]}")
    print(f"Height :{pokemon_info["height"]}")
    print(f"Weight:{pokemon_info["weight"]}")


