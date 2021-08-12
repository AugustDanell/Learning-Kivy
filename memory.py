class card:
    def __init__(self, type):
        self.type = type

        switch = {
            "duck" : "memory_assets/duck.png",
            "dog"  : "memory_assets/dog.png",
            "cat"  : "memory_assets/cat.png",
            "horse": "memory_assets/horse.png",
            "elephant": "memory_assets/elephant.png",
        }
        try:
            self.link = switch[type]

        except KeyError:
            print(type, "is not a valid type, there is no such memory card!")

    def __eq__(self, other):
        if(self.type == other.type):
            return True
        return False

if __name__ == "__main__":
    amount_of_cards = 5
    #text_game().run()
