plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)


plays.insert(0, "Romeo & Juliet")
print(plays)

plays.insert(10, "A Midsummer Night's Dream")
print(plays)




# Coding Exercise 24

def factors(numbers):
    all_factors = []
    for number in range(1, 65):
        if numbers % number == 0:
            all_factors.append(number)
    return all_factors
print(factors(64))