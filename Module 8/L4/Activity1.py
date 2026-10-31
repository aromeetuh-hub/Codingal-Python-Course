class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score


cricket = Cricket("Rohit", 85)
print("=== Sports Scoreboard ===\n")
cricket.__score = 90
print(f"get_score")