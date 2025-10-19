from data import datas
import random
name = 'name'
follower_count = 'follower_count'
while True:
    print("Welcome to Higher vs Lower!\nThe scope of the game is guessing between 2 people who has more follower"
          " between them ")
    index: int = 0
    score: int = 0
    while True:
        first_data = datas[index]
        random_index = random.randint(0, len(datas) - 1)
        if random_index == index:
            random_index = random.randint(0, len(datas) - 1)

        second_data = datas[random_index]
        print(first_data[name])
        print("VS")
        print(second_data[name])
        user_guess = input('A or B:').lower()

        if user_guess == 'a':
            if first_data[follower_count] > second_data[follower_count]:
                score += 1
                print(f"Congrats you won! Your score is: {score}")
                index = datas.index(first_data)
            else:
                print("Oh no, I am afraid you are wrong..!\nBetter luck next time!")
                print('\n' * 2)
                break
        else:
            if second_data[follower_count] > first_data[follower_count]:
                score += 1
                print(f"Congrats you won! Your score is: {score}")
                index = datas.index(second_data)
            else:
                print("Oh no, I am afraid you are wrong..!\nBetter luck next time!")
                print('\n' * 2)
                break

# to remove names already appeared
# otherwise there is a big risk for the same name to repeat itself.
# but everytime the first_data changed we should re-arrange the array data as per original.
