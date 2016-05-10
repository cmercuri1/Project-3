from collections import defaultdict as dd

def score_phase(bids, tricks, deck_top, player_data=None, 
                suppress_player_data=True):
    ''' Function that determines the scores for each player for a particular
    Phase '''
    
    score = [0, 0, 0, 0]

    curr = 0
    curr_win = 0

    trump_suit = deck_top[1]

    winning_tricks = dd(int)

    bid_list = []
    trick_list = []
    count = 0

    #Convert trick tuple into list so that it is iterable
    for trick in tricks:
        trick_list.append([])
        for card in trick:
            trick_list[count].append(card)
        count += 1

    for trick in trick_list:
        curr_suit = trick[0][1]
        high_value = trick[0][0]
        high_value = true_value(high_value)
        for card in trick[1:]:
            if (curr == 3):
                curr = 0
            else:
                curr += 1

            suit = card[1]
            value = card[0]
            value = true_value(value)

            if (suit == curr_suit):
                if (value > high_value):
                    high_value = value
                    curr_win = curr
            elif (suit == trump_suit):
                if (curr_suit != trump_suit):
                    curr_suit = trump_suit
                    high_value = value
                    curr_win = curr
        winning_tricks[curr_win] += 1

    #Calculate scores for each player by first checking if they met their bid
    #and then adding their victories
    for player in range(0, 4):
        if (bids[player] == winning_tricks[player]):
            score[player] += 10
        score[player] += winning_tricks[player]

    return score[0], score[1], score[2], score[3]    

''' Helper function that sets card values for 10 (seen as 0), and the non
numerical value cards to numberical values to make comparisons easiers '''
def true_value(value):
    if (value == '0'):
        value = 10
    elif (value == 'J'):
        value = 11
    elif (value == 'Q'):
        value = 12
    elif (value == 'K'):
        value = 13
    elif (value == 'A'):
        value = 14
    else:
        value = int(value)
    return value
