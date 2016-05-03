from collections import defaultdict as dd

def score_phase(bids, tricks, deck_top):
    ''' Function that determines the scores for each player for a particular
    Phase '''
    score_0 = 0
    score_1 = 0
    score_2 = 0
    score_3 = 0

    curr_lead = 0
    curr_win = 0

    trump_suit = deck_top[1]

    winning_tricks = dd(int)
    
    for trick in tricks:
        curr_suit = trick[0][1]
        high_value = trick[0][0]
        for card in trick[1:]:
            suit = card[1]
            value = card[0]
            if (suit == curr_suit):
            

    return score_0, score_1, score_2, score_3    
