def bid(hand, player_no, phase_no, deck_top, reshuffled=False, player_data=None,
        suppress_player_data=True):
    bid = 0

    if (phase_no == 4) or (phase_no == 16):
        return 1
    elif (phase_no == 8) or (phase_no == 12):
        return 2
    
