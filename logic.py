from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.hp = randint(20,40)
        self.dmg = randint(5,7)

        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        if enemy.hp > self.dmg:
            enemy.hp -= self.dmg
            return f"Аттака на покемона, здоровье {enemy.hp}"
        else:
            enemy.hp = 0
            return "Враг повержен"
        
    def info(self):
        return f"""У твоего покемона следующие характеристики:
        -{self.hp} ед. здоровья
        -{self.dmg} ед. урона"""


    # Метод для получения картинки покемона через API
    def get_img(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data['sprites']['front_default'])
            else:
                return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
