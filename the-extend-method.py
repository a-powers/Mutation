mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)

extra_mountains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)


#Not mutated; simply combining two or other lists
steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks
print(my_meal)

steaks += more_steaks
print(steaks)