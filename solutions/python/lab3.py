


score = input("Enter your grade: ")
# score = int(input("Enter your grade: "))
if score.isdigit():
    score = int(score)
else:
    score = 0

result = ''

if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'F'

if score >= 100:
    result += '+'
elif score < 60:
    result = result
elif score % 10 > 5:
    result += '+'
elif score % 10 < 5:
    result += '-'

print(result)