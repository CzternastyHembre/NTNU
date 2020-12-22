def new_deck():
    shades = ['s', 'h', 'd', 'c']
    nums = [i for i in range(2,15)]
    deck = []
    for shade in shades:
        for number in nums:
            deck.append((number, shade))
    return deck


import random
def shuffle(deck):
    random.shuffle(deck)
    return deck

deck = new_deck()


def check_value(play):

    if play[0][0] == play[1][0] == play[2][0]:
        return 5

    straight = True
    for i in range(len(play)-1):
        if not(play[i][0] + 1 == play[i+1][0]):
            straight = False
            break
    if straight:
        return 4
    if play[0][0] == play[1][0] or play[1][0] == play[2][0] or play[2][0] == play[0][0]:
        return 2
    return 1

def check_suits(play):
    for i in range(len(play)-1):
        if not(play[i][1] == play[i+1][1]):
            return 1
    return 3


def evaluate_play(play):
    suits = check_suits(play)
    value = check_value(play)
    if value + suits == 7:
        return 6
    if value > suits:
        return value
    return suits


"""def computer_play(hand):
    besthand = 0
    newhand = []
    for i in range(len(hand)-2):
        if evaluate_play(hand[i:i+3]) >= besthand:
            besthand = evaluate_play(hand[i:i+3])
            newhand = hand[i:i+3]
    for card in newhand:
        del hand[hand.index(card)]
    return newhand"""

def computer_play(hand):
    besthand = 0
    newhand = []
    for i in range(len(hand)):
        for j in range(1, len(hand)):
            for k in range(2, len(hand)):
                if j != i and j != k and i != k:
                    if evaluate_play([(hand[i]),(hand[j]),(hand[k])]) >= besthand:
                        besthand = evaluate_play([(hand[i]),(hand[j]),(hand[k])])
                        newhand = [(hand[i]),(hand[j]),(hand[k])]
    for card in newhand:
        del hand[hand.index(card)]
    return newhand


def human_play(hand):
    card_str = convert_card_to_string(hand)
    legal = False
    while not legal:
        legal = True
        choice = input('Dine kort på hånden er' + card_str + '. Velg kort: ')
        choice = choice.split(' ')
        try:
            for i in range(len(choice)):
                choice[i] = int(choice[i])
                choice[i] -= 1
        except:
            print('Feil antall kort. Prøv på nytt!')
            continue
        for i in range(len(choice)-1):
            if (hand[choice[i]] == hand[choice[i+1]]) or not(0 <= choice[i] <= 4) or not(0 <= choice[i+1] <= 4) or len(choice) != 3:
                print('Feil antall kort. Prøv på nytt!')
                legal = False
                break
    new_hand = []
    for el in choice:
        new_hand.append(hand[el])
    for el in choice[::-1]:
        del hand[el]
    return new_hand


def convert_card_to_string(hand):
    values = [i for i in range(2,11)]
    values += ['J', 'Q', 'K', 'A']
    card_str = ''
    for card in hand:
        card_str += ' ' + str(values[card[0]-2]) + card[1]
    return card_str


def update_winner(won_cards, winner_play, loser_play, war_cards):
    won_cards += winner_play
    won_cards += loser_play
    won_cards += war_cards
    del war_cards[::]


hand = [(3,'s'),(11,'s'),(4,'a'),(4,'d'),(4,'s')]
#new_hand = human_play(hand)
#print(new_hand)
#print(hand)
c_won = [(14, 'c'), (14, 's'), (14, 'd'), (10, 's'), (4, 's'), (3, 'h')]
c_play =  [(11, 'd'), (10, 'd'), (9, 'd')]
h_play =  [(7,'c'), (9, 'c'), (4, 'c')]
war_cards =  [(2, 'h'), (12, 'c'), (8, 'c'), (13, 'c'), (12, 'h'), (6, 'c')]
update_winner(c_won, c_play, h_play, war_cards)

def main():
    i = 0
    deck = new_deck()
    war_cards = []
    c_won = []
    h_won = []

    while len(deck) >= 10:

        shuffle(deck)
        i += 1
        hand1 = deck[:5]
        #     del deck[:5]

        hand2 = deck[5:10]
        #      del deck[5:10]


        print('Runde', i, end='. ')
        human = human_play(hand1)
        comp = computer_play(hand2)
        #        deck += hand1
        #       deck += hand2 Usikker på om jeg skulle legge tilbake de kortene som ikke blir brukt

        human_score = evaluate_play(human)
        comp_score = evaluate_play(comp)
        scores = ['', 'ingenting', 'par', 'flush', 'straight', 'tre like', 'straight flush']
        winner_play = None
        looser_play = None
        print('Du spilte ' + convert_card_to_string(human) +  '. Datamaskinen spilt ' + convert_card_to_string(comp))
        if comp_score > human_score:
            print('Det er', scores[human_score], 'mot ' + str(scores[comp_score]) + '. Datamskinen vant runden!')
            update_winner(c_won, comp, human, war_cards)

        elif human_score > comp_score:
            print('Det er', scores[human_score], 'mot ' + str(scores[comp_score]) + '. Du vant runden!')
            update_winner(h_won, human, comp, war_cards)

        else:
            print('Det er', scores[human_score], 'mot ' + str(scores[comp_score]) + '. Ingen vant runden.')
            print('Det ligger', len(war_cards), 'på bordet')

        print()
        if len(h_won) > 52/2 or len(c_won) > 52/2:
            break

    print('Du vant ' + str(len(h_won)) + '. Datamaskinen vant', len(c_won),'kort')
    if len(h_won) > len(c_won):
        print('Du vant sammenlagt')
    else:
        print('Datamaskinen van sammelagt')
main()
