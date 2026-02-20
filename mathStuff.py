def get_success_rate(answers,correct_answers):
    return (correct_answers/answers) * 100 # returns the raw percentage


def get_area_of_sqaure(x,y):
    return x*y

def get_area_of_circle(radius):
    return 3.1459 * radius**2

def get_circumfrence_of_circle_d(diameter):
    return diameter*3.1459

def get_circumfrence_of_circle_r(radius):
    return radius*2 * 3.1459

print(get_success_rate(12,4))
print(get_area_of_circle(3))
print(get_area_of_sqaure(3,4))
print(get_circumfrence_of_circle_d(7))
print(get_circumfrence_of_circle_r(3.5))
