# given players and their total buy in and ending chips calculates who should pay who what amount

class Player:
    name = ""
    buy_in = 0
    final_chips = 0
    diff = 0

    def __init__(self, buy, name, final):
        self.buy_in = buy
        self.final_chips = final
        self.diff = buy - final
        self.name = name

    def add_on(self, amount):
        self.buy_in += amount
        self.diff = self.buy_in - self.final_chips

    def set_final_chips(self, final):
        self.final_chips = final
        self.diff = self.buy_in - self.final_chips


class Transaction:
    """	Class representing a transaction (un remboursement) between two people
    """

    def __init__(self, payer, amount, receiver):
        self.payer = payer
        self.amount = amount
        self.receiver = receiver

    def __str__(self):
        return "{} pays {} cad to {}".format(self.payer, round(self.amount, 2), self.receiver)


class Game:
    players = []
    # list of players in the negative [name, amount_owed]
    negative = []
    # list of player in the positive [name, amount_to_be_paid]
    positive = []

    # players that are even are omitted

    def __init__(self, players):
        self.players = players
        for player in players:
            # if player made money
            if player.diff > 0:
                p = [player.name, player.diff]
                self.positive.append(p)

            # if they lost money
            if player.diff < 0:
                p = [player.name, -player.diff]
                self.negative.append(p)

    def calculate_payments(self):
        # sort to try and reduce the number of payments
        self.negative.sort(key=lambda x: x[1])
        self.positive.sort(key=lambda x: x[1])

        # done with two pointers
        payments = []
        # receiver
        i = 0
        # payer
        j = 0

        # make sure we don't go past the end of a list
        while i < len(self.negative) and j < len(self.positive):
            current_receive = self.negative[i]
            current_payer = self.positive[j]

            payer = current_payer[0]
            receiver = current_receive[0]
            owed = current_receive[1]
            to_pay = current_payer[1]

            if owed > to_pay:
                payments.append(Transaction(payer, to_pay, receiver))

                # want to set to_pay balance to 0, subtract the difference from owed, and increment the payer
                current_receive[1] -= current_payer[1]
                current_payer[1] = 0
                j += 1
                continue
            elif owed == to_pay:
                payments.append(Transaction(payer, to_pay, receiver))

                # want to set to_pay balance to 0, subtract the difference from owed, and increment the payer
                current_receive[1] = 0
                current_payer[1] = 0
                i += 1
                j += 1

            else:
                payments.append(Transaction(payer, owed, receiver))

                # pay as much as possible to the current receiver update values then increment the receiver
                current_payer[1] -= current_receive[1]
                current_receive[1] = 0
                i += 1

        return payments


if __name__ == "__main__":
    Jonah = Player(25, "Jonah", 15)
    Kesh = Player(25, "Kesh", 30)
    Younes = Player(25, "Younes", 10)
    Samir = Player(25, "Samir", 60)
    Josh = Player(50, "Josh", 35)

    new_game = Game([Jonah, Kesh, Younes, Samir, Josh])
    transaction = new_game.calculate_payments()
    for t in transaction:
        print(t)
