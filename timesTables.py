from random import choice

def tables(num1,num2):
    tableslist = [num1*num2 for num2 in range(1,num2+1)]
    return tableslist

def times_table_quiz_random(num1,num2):
    list = tables(num1,num2)
    score = 0 
    for i in range(1,num2+1):
        correct_choice = choice(list)
        list.remove(correct_choice)
        question = input("what is "+str(num1)+" times "+ str(correct_choice/num1)+": ").strip()
        if question == str(correct_choice):
            score+=1
        else:
            print("incorrect")
    return score 
print(times_table_quiz_random(15,12))