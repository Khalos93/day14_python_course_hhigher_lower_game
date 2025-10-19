from data import datas
from logic import higher_or_lower
name = 'name'
follower_count = 'follower_count'
while True:
    print("Welcome to Higher vs Lower!\nThe scope of the game is guessing between 2 people who has more follower"
          " between them ")
    score: int = 0
    first_data = None
    datas_copy = datas[:]
    higher_or_lower(datas_copy, first_data, name, follower_count, score)


