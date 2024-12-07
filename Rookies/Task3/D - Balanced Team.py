def max_balanced_team(n, skills):
    skills.sort()
    left = 0
    max_team_size = 0
    for right in range(n):
        while skills[right] - skills[left] > 5:
            left += 1
        max_team_size = max(max_team_size, right - left + 1)
    return max_team_size

n = int(input())
skills = list(map(int, input().split()))
print(max_balanced_team(n, skills))
