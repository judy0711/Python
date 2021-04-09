letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: value
    for key,value
    in zip(letters, points)
}
letter_to_points[" "] = 0
print(letter_to_points)

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter,0)
    return point_total

# testing for the code with BROWNIE
brownie_points = score_word("BROWNIE")
print(brownie_points) 

player_to_words = {
    "player1" : ["BLUE", "TENNIS", "EXIT"],
    "wordNerd":["EARTH", "EYES", "MACHINE"],
    "LEXI CON": ["ERASER", "BELLY", "HUSKY"],
    "PROF READER":["ZAP", "COMA", "PERIOD"]
    
}

player_to_points = {}

#update points total any time a word is played

def update_points_total():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

print(player_to_points)

#add inputed name into the player_to_words dictionary

x = input("What is your name?")
y = input("What word can your form?")

def play_word(player, word):
    player_to_words[player].append(word)
    update_points_total()




if x == "player1" in player_to_words:
    play_word("player1", y)
elif x == "wordNerd" in player_to_words:
    play_word("wordNerd", y)
elif x == "LEXI CON" in player_to_words:
    play_word("LEXI CON", y)
elif x == "PROF READER" in player_to_words:
    play_word("PROF READER", y)
else:
    player_to_words.update({x:y})
    update_points_total()

   
print(player_to_words)
print(player_to_points)

