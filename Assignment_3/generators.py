def my_gen():
    n = 1

    yield n

    n += 1
    yield n

    n += 1
    yield n


for i in my_gen():
    print(i)

