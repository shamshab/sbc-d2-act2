from random import choice

p1 = input("Fold/Unfold: ")

c2 = choice(["Fold", "Unfold"])
c3 = choice(["Fold", "Unfold"])


print(f"Player 1: {p1}")
print(f"Com 2: {c2}")
print(f"Com 3: {c3}")


if (p1 == "Fold" and c2 == "Unfold" and c3 == "Unfold") or (p1 == "Unfold" and c2 == "Fold" and c3 == "Fold"):
    print("Player 1 Win!")
elif (p1 == "Unfold" and c2 == "Fold" and c3 == "Unfold") or (p1 == "Fold" and c2 == "Unfold" and c3 == "Fold"):
    print("Com 2 Win!")
elif (p1 == "Unfold" and c2 == "Unfold" and c3 == "Fold") or (p1 == "Fold" and c2 == "Fold" and c3 == "Unfold"):
    print("Comp 3 Win!")
else:
    print("No one wins!")
