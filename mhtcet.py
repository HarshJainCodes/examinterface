question_set = [
    ['Q1', 'a', 'b', 'c', 'd', 'd'],
    ['Q2', 'a', 'b', 'c', 'd', 'c'],
    ['Q3', 'a', 'b', 'c', 'd', 'd'],
    ['Q4', 'a', 'b', 'c', 'd', 'a'],
]
response = input("Do you want to take test:")
if response == 'yes':
    gate = True
score = 0
q = 0
while gate:
    
    for x in question_set:
        print(x[0])
        print(x[1], x[2], x[3], x[4])
        ans = input("Your answer?")
        if ans == x[-1]:
            score += 4
    print(score)
    gate = False
    
