n, c = map(int, input().split())
cards = input().split()

def find_max_power(curr_n: int,curr_power: int, cards: list[str]) -> int:
    curr_attack = curr_n*curr_power

    for i in range(c):
        if cards[i] == 'T':
            cards[i] = '*'
            result = find_max_power(curr_n, curr_power+1, cards)
            cards[i] = 'T'

            curr_attack = max(curr_attack, result)
        elif cards[i] == 'R':
            cards[i] = '*'
            result = find_max_power(curr_n, curr_power+(curr_n//2), cards)
            cards[i] = 'R'

            curr_attack = max(curr_attack, result)
        elif cards[i] == 'S':
            cards[i] = '*'
            result = find_max_power(curr_n-1, curr_power+(curr_power//2), cards)
            cards[i] = 'S'

            curr_attack = max(curr_attack, result)

    return curr_attack

print(find_max_power(n,1,cards))
        

            
    