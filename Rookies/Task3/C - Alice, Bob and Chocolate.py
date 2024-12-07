def chocolates_game(n, times):
   
    alice = 0  
    bob = n - 1  
    alice_time = 0 
    bob_time = 0  
    alice_bars = 0  
    bob_bars = 0  

    while alice <= bob:
        if alice_time <= bob_time:
            alice_time += times[alice]
            alice += 1
            alice_bars += 1
        else:
            bob_time += times[bob]
            bob -= 1
            bob_bars += 1

    return alice_bars, bob_bars

n = int(input("Enter the number of chocolate bars: "))
times = list(map(int, input("Enter the time for each bar: ").split()))

alice_bars, bob_bars = chocolates_game(n, times)
print(f"Alice: {alice_bars}, Bob: {bob_bars}")
