class Animals():
  '''Описание класса животное '''
  def __init__(self, animal, name, weight):
    self.animal = animal
    self.name = name
    self.weight = weight



class Goat(Animals):
    def __init__(self, animal, name, weight):
        super().__init__(animal, name, weight)
    def  goat_say(self):
        print(f'Коза {goat.name} говорит: Мее-ееее')
    def feed_goat(self):
        print(f'Коза {goat.name} жует травку')
    def goat_manage(self):
        print(f'Козу {goat.name} нужно подоить')



class Chicken(Animals):
    def __init__(self, animal, name, weight):
        super().__init__(animal, name, weight)
    def  chicken_say(self):
        print(f'Курица {chicken.name} говорит: КуКаРеку')
    def feed_chicken(self):
        print(f'Курица {chicken.name} щиплет зернышки')
    def chicken_manage(self):
        print(f'У курицы {chicken.name} нужно собрать яйца')



class Sheep(Animals):
    def __init__(self, animal, name, weight):
        super().__init__(animal, name, weight)
    def  sheep_say(self):
        print(f'Овца {sheep.name} говорит: Меееее')
    def feed_sheep(self):
        print(f'Овца {sheep.name} жует травку')
    def sheep_manage(self):
        print(f'Овцу {sheep.name} нужно подстрич')


class Cow(Animals):
    def __init__(self, animal, name, weight):
        super().__init__(animal, name, weight)
    def  cow_say(self):
        print(f'Корова {cow.name} говорит: Мууу')
    def feed_cow(self):
        print(f'Корова {cow.name} жует травку')
    def cow_manage(self):
        print(f'Корову {cow.name} нужно подоить')


class Goose(Animals):
    def __init__(self, animal, name, weight):
        super().__init__(animal, name, weight)
    def  goose_say(self):
        print(f'Гусь {goose.name} говорит: Га-Га-Га')
    def feed_goose(self):
        print(f'Гусь {goose.name} щиплет травку')
    def goose_manage(self):
        print(f'У гуся {goose.name} нужно собрать яйца')


class Duck(Animals):
    def __init__(self, animal, name, weight):
        super().__init__(animal, name, weight)
    def  duck_say(self):
        print(f'Утка {duck.name} говорит: Кря-Кря')
    def feed_duck(self):
        print(f'Утка {duck.name} щиплет травку')
    def duck_manage(self):
        print(f'У утки {duck.name} нужно собрать яйца')




goose_gray = Goose('Гусь', 'Борис', 5)
goose_white = Goose('Гусь',  'Иван', 7)
duck = Duck('Утка', 'Кряква', 7)
goat_roga = Goat('Коза', 'Рога', 15)
goat = Goat('Коза', 'Копыта', 20)
chicken = Chicken('Курица', 'Ко-Ко', 3)
chicken_kukareku = Chicken('Курица', 'Кукареку', 5)
sheep_borashek = Sheep('Овца', 'Барашек', 20)
sheep = Sheep('Овца', 'Кудрявый', 25)
cow = Cow('Корова', 'Манька', 50)




# Общий веc животных
total_weight = sum([goose_gray.weight,goose_white.weight,cow.weight,
                    sheep_borashek.weight,sheep.weight,
                    chicken.weight,chicken_kukareku.weight,
                    goat_roga.weight,goat.weight,duck.weight])


animals = [goose_gray.__dict__, goose_white.__dict__, cow.__dict__, sheep.__dict__, sheep_borashek.__dict__, chicken_kukareku.__dict__,
           chicken.__dict__, goat_roga.__dict__, goat.__dict__, duck.__dict__]

animals_weight = 0
animals_weight_max = 0
for animal in animals:
    animals_weight += animal['weight']
    if animals_weight_max < animal['weight']:
        animals_weight_max = animal['weight']
    else:
        animals_weight_max = animals_weight_max
for animal in animals:
    for k, v in animal.items():
        if v == animals_weight_max:
            big_animal = animal['name']

print(f"Общий вес животных - {animals_weight} кг.\nИмя самого тяжелого животного - {big_animal}")



