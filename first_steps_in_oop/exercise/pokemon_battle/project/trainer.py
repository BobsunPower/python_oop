# from first_steps_in_oop.exercise.pokemon_battle.project.pokemon import Pokemon
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name, self.pokemons = name, []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        return f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemons)}
- {' '.join([p.pokemon_details() for p in self.pokemons])}"""
