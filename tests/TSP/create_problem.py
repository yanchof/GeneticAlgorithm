import random


if __name__ == "__main__":
    # create city
    city_num = 5
    for i in range(city_num):
        x = random.random() * 100
        y = random.random() * 100
        print(x, y)
