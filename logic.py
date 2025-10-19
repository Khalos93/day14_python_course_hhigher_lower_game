import random
from util import get_valid_user_input, ValidOptions


def higher_or_lower(datas_copy, first_data, name, follower_count, score ):
    while True:
        if len(datas_copy) < 2:
            print("No more data left to compare!")
            break

        index: int = random.randint(0, len(datas_copy) - 1)
        if not first_data:
            first_data = datas_copy.pop(index)

        random_index = random.randint(0, len(datas_copy) - 1)
        second_data = datas_copy.pop(random_index)
        print(first_data[name])
        print("VS")
        print(second_data[name])
        user_guess = get_valid_user_input("Type 'A' for the top option or 'S' for the bottom one:", ValidOptions)

        if (
                (user_guess == 'a' and first_data[follower_count] > second_data[follower_count] or
                 user_guess == 's' and second_data[follower_count] > first_data[follower_count])
        ):

            score += 1
            print(f"Congrats you won! Your score is: {score}")

            if user_guess == 's':
                first_data = second_data
                datas_copy = [item for item in datas_copy if item != second_data and item != first_data]

        else:
            print(f"Oh no, I am afraid you are wrong..!\n{first_data[name]} has {first_data[follower_count]} followers"
                  f" while {second_data[name]} has {second_data[follower_count]}\nBetter luck next time!")
            print('\n' * 2)
            break
