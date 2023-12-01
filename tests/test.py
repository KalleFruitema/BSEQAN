one_three = 0.07699957015737373/2
print(f"one_three\n{one_three}\n")

one_three__two = (0.468022646257077 + 0.436090225563909) / 2
print(f"one_three__two\n{one_three__two}\n")

one_three__four = (0.500523113476899 + 0.433936999100669) / 2
print(f"one_three__four\n{one_three__four}\n")

one_three__five = (0.705009991980958 + 0.674316263061227) / 2
print(f"one_three__five\n{one_three__five}\n")

print("===========================================")

two_four = 0.113662795098674 /2
print(f"two_four\n{two_four}\n")

two_four__five = (0.664764947512551 + 0.629058086962014) / 2
print(f"two_four__five\n{two_four__five}\n")

two_four__one_three = (one_three__two + one_three__four) / 2
print(f"two_four__one_three\n{two_four__one_three}\n")

print("===========================================")

two_four__one_three_div = two_four__one_three / 2
print(f"two_four__one_three_div\n{two_four__one_three_div}\n")

for_one_three = two_four__one_three_div - one_three
print(f"for one_three\n{for_one_three}\n")

for_two_four = two_four__one_three_div - two_four
print(f"for two_four\n{for_two_four}\n")

all_five = (0.689663127521092 + 0.646911517237282) / 2
print(f"all_five\n{all_five}\n")

print("===========================================")

all_five_for_all = all_five / 2 - two_four__one_three_div
print(f"all_five_for_all\n{all_five_for_all}\n")

all_five_for_five = all_five / 2
print(f"all_five_for_five\n{all_five_for_five}\n")