def untreated_crimes(n, events):
    untreated = 0
    available_officers = 0

    for event in events:
        if event == -1:  # A crime occurs
            if available_officers > 0:
                available_officers -= 1  # Use one officer to investigate
            else:
                untreated += 1  # No officers available, crime goes untreated
        else:
            available_officers += event  # Recruit officers

    return untreated

# Input
n = int(input())
events = list(map(int, input().split()))

# Output
print(untreated_crimes(n, events))
