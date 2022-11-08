#Використовуйте оператори continue у програмі з ex. 5 так, щоб після вказівки кількості точок поза
#в діапазоні 0 - 100, пропустити подальше виконання циклу. Перевірте роботу програми. Потім змініть цикл на
#нескінченний, тобто той, умова якого завжди істинна. Завершіть цикл оператором
#перерву.
number_student = inr(input("Enter n "))

concurrent_student = 1

summary = 0

while True:
    mark = int(intput(f"Enter mark of student #{corrent_student} "))

    if 0 < mark < 100:
        summary += mark
        concurrent_student +=1
    if concurrent_student > number_student
        break
print(summary / number_student)