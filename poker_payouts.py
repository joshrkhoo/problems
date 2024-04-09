# """
# Algorithm poker payouts
# - determine how much each player needs to receive or pay another player

# Losers to payout 
# Winners to get paid

# Inputs:
# 1. Starting money
# 2. List of players and their current amount of money

# Output:
# Number of transactions
# N trasactions of the form:
#     - (player, amount)
#     - index pays player amount


# Starting money: 10
# 0. Jarred: 8.80
# 1. Raghav: 39.90
# 2. Jean: 12.90
# 3. Ling: 18.10
# 4. Khoo: 6.2
# 5. Josh: 0
# 6. Ezra: 0
# 7. Julian: 8.80
# 8. Ryan: 0
# 9. Allen: 5.30


# Starting money: 10
# 0. Jean: 25.9
# 1. Ling: 24.9
# 2. Josh: 39.2
# 3. Julian: 0
# 4. Allen: 0
# 5. Jarred: 0
# 6. Raghav: 0
# 7. Khoo: 0
# 8. Ezra: 0

# """
# from collections import deque
# from decimal import Decimal, ROUND_HALF_UP


# def poker_payouts(starting_money: Decimal, players: list)-> int:

#     """
#     queue of winners
#     list of losers


#     when do we stop paying a winner?
#         - when winner amount == starting money
    
#     when does a loser stop paying?
#         - when loser amount == starting money
    
    
    
                    
#     Get winner
#         Get loser
#             calculate payout
#             winner amount -= payout
#             loser amount += payout
#             if winner amount > starting money
#                 get next loser
#             if loser amount < starting money and winner amount == starting money
#                 get next winner

    
#     """

#     winners = deque()
#     losers = []
#     payouts = []


#     for player, amount in enumerate(players):
#         if amount > starting_money:
#             winners.append((player, Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
#         elif amount < starting_money:
#             losers.append((player, Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    
#     winners = sorted(winners, key=lambda x: x[1], reverse=False)
#     losers = sorted(losers, key=lambda x: x[1], reverse=False)

    
#     i = 0
#     # while winners still in queue (havent paid them out)
#     while winners:
#         winner, winner_amount = winners.pop()
#         if winner_amount == starting_money:
#             break

#         # while winnner still needs to be paid
#         while winner_amount > starting_money:
#             loser, loser_amount = losers[i]

#             if loser_amount == starting_money:
#                 i += 1

#             if loser_amount < starting_money:
#                 payout = min(winner_amount - starting_money, starting_money - loser_amount)
#                 payouts.append((loser, winner, payout))
#                 loser_amount += payout
#                 winner_amount -= payout

#                 losers[i] = (loser, loser_amount)

#                 if loser_amount == starting_money:
#                     i += 1


#     # print(winners)
#     # print(losers)
                    

#     return payouts, len(payouts)






# if __name__ == "__main__":
#     input1 = [10, [8.80, 39.90, 12.90, 18.10, 6.20, 0, 0, 8.80, 0, 5.30]]
#     input2 = [10, [25.9, 24.9, 39.2, 0, 0, 0, 0, 0, 0]]

#     data1 = poker_payouts(input1[0], input1[1])
#     payouts1, transactions1 = data1
#     data2 = poker_payouts(input2[0], input2[1])
#     payouts2, transactions2 = data2

#     print("Number of transactions:", transactions1)
#     for transaction in payouts1:
#         print(f"Player {transaction[0]} pays Player {transaction[1]} amount {transaction[2]}")


#     print("Number of transactions:", transactions2)
#     for transaction in payouts2:
#         print(f"Player {transaction[0]} pays Player {transaction[1]} amount {transaction[2]}")




from decimal import Decimal, ROUND_HALF_UP
from collections import deque

def poker_payouts(starting_money: Decimal, players: dict) -> None:
    """
    Algorithm to find the least number of transactions to pay out the players

    Currently, this is the most optimal solution I can think of
        - Sort of Greedy approach
    """

    winners = deque()
    losers = []
    payouts = []

    # Convert player amounts to Decimal with two decimal places
    for name, amount in players.items():
        if amount > starting_money:
            winners.append((name, Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
        elif amount < starting_money:
            losers.append((name, Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    
    # Sort winners and losers
    winners = sorted(winners, key=lambda x: x[1], reverse=False)
    losers = sorted(losers, key=lambda x: x[1], reverse=False)

    i = 0
    while winners:
        winner, winner_amount = winners.pop()
        if winner_amount == starting_money:
            break

        while winner_amount > starting_money:
            loser, loser_amount = losers[i]

            if loser_amount == starting_money:
                i += 1

            if loser_amount < starting_money:
                payout = min(winner_amount - starting_money, starting_money - loser_amount)
                payouts.append((loser, winner, payout))
                loser_amount += payout
                winner_amount -= payout
                losers[i] = (loser, loser_amount)

                if loser_amount == starting_money:
                    i += 1

    # Print number of transactions
    print("Number of transactions:", len(payouts))
    
    # Print each transaction
    for transaction in payouts:
        print(f"{transaction[0]} pays {transaction[1]} amount {transaction[2]}")

    print()

if __name__ == "__main__":
    input1 = {
        "Jarred": Decimal('8.80'),
        "Raghav": Decimal('39.90'),
        "Jean": Decimal('12.90'),
        "Ling": Decimal('18.10'),
        "Khoo": Decimal('6.2'),
        "Josh": Decimal('0'),
        "Ezra": Decimal('0'),
        "Julian": Decimal('8.80'),
        "Ryan": Decimal('0'),
        "Allen": Decimal('5.30')
    }
    input2 = {
        "Jean": Decimal('25.9'),
        "Ling": Decimal('24.9'),
        "Josh": Decimal('39.2'),
        "Julian": Decimal('0'),
        "Allen": Decimal('0'),
        "Jarred": Decimal('0'),
        "Raghav": Decimal('0'),
        "Khoo": Decimal('0'),
        "Ezra": Decimal('0')
    }

    poker_payouts(Decimal('10'), input1)

    poker_payouts(Decimal('10'), input2)