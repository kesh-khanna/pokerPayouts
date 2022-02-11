# compares Hand Equity, Pot Odds and number of outs

# calculates the relationship between the total pot size and bet that you must call to see the next card

def pot_odds(size, call_amount):
    return round((call_amount) / (size + call_amount) * 100, 2)

# rule of 2 & 4
# count the number of outs we have
# multiply the outs by 2 on the flop
# multiply by 2 on turn
# multipy by 4 on flop and opponent is all in

def two_four(odds, outs):
    equity = outs * 2
    if equity >= round(odds):
        return "Call"
    else:
        return "Fold"


def decision_adv(pot_odds_pct, num_outs, river=False):
    if river == True:
        hand_equity = (num_outs / 48) * 100
    else:
        hand_equity = (num_outs / 49) * 100

    print('Hand Equity: {}%'.format(round(hand_equity, 3)))
    print('Pot Odds: {}%'.format(pot_odds_pct))
    print('#####################')

    if hand_equity >= pot_odds_pct:
        print('Call')
    else:
        print('Fold')



