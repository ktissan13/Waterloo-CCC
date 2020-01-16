# CCC 04 J3 - Smile with Similes
# Tissan Kugathas
# ICS4U0
# January 25 2020

adj = []
nouns = []

n = int(input())
m = int(input())

if 1 <= n <= 5:
    if 1 <= m <= 5:
        for index in range(n):
            adj.append(input())
        for index in range(m):
            nouns.append(input())

        for adject in adj:
            for noun in nouns:
                final = adject + ' as ' + noun
                print(final)
