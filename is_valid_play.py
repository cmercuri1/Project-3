def is_valid_play(play, curr_trick, hand):
    '''Function that Looks at a card and determines if that is a valid option
    for a play'''
    #Check if card is actually in hand
    if play not in hand:
        return False
    else:
        #Check if player is lead, meaning any card is valid
        if !curr_trick:
            return True
        #Check if card is of same suit as lead
        else:
            if play[1] == curr_trick[0][1]:
                return True
            #if not, check if any other cards in hand are of same suit
            else:
                for card in hand:
                    if card[1] == curr_trick[0][1]:
                        return False
                #If no other cards are of same suit    
                return True                    
