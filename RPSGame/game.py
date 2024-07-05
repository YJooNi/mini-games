import random
import menu

# list of playing cards

set = ["rock", "paper", "scissors"]

def icon(choice):
    match choice:
        case "rock":
            return "🪨"
        case "scissors":
            return "✂️"
        case "paper":
            return "📄"

# object for players

class Player:
  def __init__(self, cards, points):
    self.cards = cards
    self.points = points

# function for dealing cards and displaying cards

def deal_cards():
  list = []
  for x in range(3):
    list.insert(x, random.choice(set))
  return list

#   #   #   #   #
def display_cards(player, ai):

    print("AI's hand:")
    for card in ai.cards:
        print("[Hidden]", end=" ")
    menu.nextLine()

    menu.nextLine()

    print("Your hand:")
    for card in player.cards:
        print(card, end=" ")
    menu.nextLine()

# function for printing and handing points

def ai_win(ai):
    menu.nextLine()
    print("AI wins!", "AI gets 1 point 🎖 !")
    ai.points += 1

def player_win(player):
    menu.nextLine()
    print("You win!", "You get 1 point 🎖 !")
    player.points += 1
    
def tie():
    print("Round ends in a tie. No point given!")

#   #   #   #   #
def result(player, ai):
    menu.nextLine()
    print("===== Points =====")
    print("AI:", ai.points, "     ", "You:", player.points)

    if player.points > ai.points:
        menu.nextLine()
        print("You win the game! What a champ!")
    elif player.points < ai.points:
        menu.nextLine()
        print("AI wins the game! Better luck next time!")
    elif player.points == ai.points:
        menu.nextLine()
        print("What a game! It's a tie! You're no better than an AI!")

# function for game rounds

def round(player, ai, choice):

    menu.nextLine()
    player.cards.remove(choice)
    print("You have played", choice, icon(choice))

    ai_choice = random.choice(ai.cards)
    ai.cards.remove(ai_choice)
    print("AI has played", ai_choice, icon(ai_choice))

    match choice:
        #   #   #   #   #
        case "rock":
            if ai_choice == "rock":
                tie()
            elif ai_choice == "paper":
                ai_win(ai)
            elif ai_choice == "scissors":
                player_win(player)
        #   #   #   #   #
        case "paper":
            if ai_choice == "paper":
                tie()
            elif ai_choice == "scissors":
                ai_win(ai)
            elif ai_choice == "rock":
                player_win(player)
        #   #   #   #   #
        case "scissors":
            if ai_choice == "scissors":
                tie()
            elif ai_choice == "rock":
                ai_win(ai)
            elif ai_choice == "paper":
                player_win(player)


# ==========================================================================
# main function for starting the game 

def game_start(run):
    menu.nextLine()
    print("===== GAME START =====")
    player = Player(deal_cards(), 0)
    ai = Player(deal_cards(), 0)

    # the game runs while cards are in play
    while player.cards:

        # displays total cards
        menu.nextLine()
        display_cards(player, ai)
        menu.nextLine()

        #   #   #   #   #
        print("===== Points =====")
        print("AI:", ai.points, "     ", "You:", player.points)
        menu.nextLine()

        #   #   #   #   #
        choice = input("Which card would you like to use? ")
        if choice in player.cards:
            match choice:
                case "rock":
                    round(player, ai, choice)
                case "paper":
                    round(player, ai, choice)
                case "scissors":
                    round(player, ai, choice)
                case _:
                    print("Please type in a choice of cards you have!")
        else:
           print("You do not have", choice, "in your hand")

    # are the rounds end and no one has any cards and prints result
    result(player, ai)

    # after the game ends, the game asks to play again or leave
    while run:
        menu.nextLine()
        print("Have what it takes to play again?")
        menu.nextLine()
        menu.create_menu(menu.list_game_menu)
        #   #   #   #   #
        selection = input("Select an option:")
        match selection:
            case "1" :
                game_start(run)
                break
            case "2":
                print("Thank You For Playing!")
                run = False
                break 
            case _:
                print(selection, "is not an option!")

    # returns true or false
    return run