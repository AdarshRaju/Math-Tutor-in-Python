print('Math Tutor')

import random, string, timeit

x = 12
def tutor():
    print(x)
    no_of_questions = int(input("Enter no. of questions:"))
    highest_digit = int(input("Enter how many digits you need:"))
    
    score = 0
    array1 = []
    array2 = []
    for i in range(no_of_questions):
        numa = (random.randrange(0, 10**highest_digit))
        numb = (random.randrange(0, 10**highest_digit))
        oper = random.choice(['+', '-', '*', '/'])

        if oper == '+':
            correct = int(numa) + int(numb)
        if oper == '-':
            correct = int(numa) - int(numb)
        if oper == '*':
            correct = int(numa) * int(numb)
        if oper == '/':
            numb = random.randrange(1, 10**highest_digit)
            correct = int(numa) / int(numb)
                    
            
        question = str(numa) + oper + str(numb)
    
        answer = input(f'{question}?')
       
        if int(answer) == correct:
            score += 1
        print(numa, numb)
        array1.append(question)
        array2.append(answer)
        table = dict(zip(array1, array2))
    
    print(f'Your score is {score}/{no_of_questions}')
    print(f'Percentage correct is {score*100/no_of_questions}')
    print(f'The record of questions and answers are: {table}')
    print('Thanks for playing!')
    return (1)
  
print(f'The total time is {timeit.timeit(\'tutor()\', globals=globals(), number =1)}')        
