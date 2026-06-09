import random

def guess_the_number():  
    secret_number = random.randint(1, 100)  
    print("Слід розгадати число, від 1 до 100")
    for attempt in range(1, 6):
        try:
            user_guess = int(input(f"Спроба номер {attempt}/5. Введи своє число: "))
        except ValueError:
            print("Потрібно ввести ціле число.")
            continue
        if user_guess == secret_number:
            print("Ви вгадали правильне число")
            return 
        elif user_guess > secret_number:
            print("Правильне число є менше ніж вказане")
        else:
            print("Правильне число є більше ніж вказане")
    print(f"У вас закінчилися спроби. Правильне число {secret_number}")

guess_the_number()