cards = {}
for i in range(6):
    card = input()
    if card == "Jack":
        cards[i] = 11
    elif card == "Queen":
        cards[i] = 12
    elif card == "King":
        cards[i] = 13
    elif card == "Ace":
        cards[i] = 14
    else:
        cards[i] = int(card)
print(sum(cards.values()) / len(cards))
