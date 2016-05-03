from collections import defaultdict as dd

def score_phase(bids, tricks, deck_top):
    ''' Function that determines the scores for each player for a particular
    Phase '''
    
    score = (0, 0, 0, 0)

    curr = 0
    curr_win = 0

    trump_suit = deck_top[1]

    winning_tricks = dd(int)
    
    for trick in tricks:
        curr_suit = trick[0][1]
        high_value = trick[0][0]
        high_value = true_value[high_value]
        for card in trick[1:]:
            if (curr == 3):
                curr = 0
            else:
                curr += 1

            suit = card[1]
            value = card[0]
            value = true_value(value)

            if (suit == curr_suit):
                if (isdigit(high_value)):
                    if (value > high_value):
                        high_value = value
                        curr_win = curr
            elif (suit == trump_suit):
                if (curr_suit != trump_suit):
                    curr_suit = trump_suit
                    high_value = value
                    curr_win = curr
        winning_tricks[curr_win] += 1

    for player in range(0, 4):
        if (bids(player) == winning_tricks[player]):
            score[player] += 10
        score[player] += winning_tricks[player]

    return score_0, score_1, score_2, score_3    

''' Helper function that sets card values for 10 (seen as 0), and the non
numerical value cards to numberical values to make comparisons easiers '''
def true_value(value):
    if (value == 0):
        value = 10
    elif (value == 'J'):
        value = 11
    elif (value == 'Q'):
        value = 12
    elif (value == 'K'):
        value = 13
    elif (value == 'A'):
        value = 14
    return value
