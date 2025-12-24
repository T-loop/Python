nested_list = [[x, x + 1] for x in range(100)]

for pair in nested_list:
    for item in pair:
        print(f" {pair} and -> {item}")
