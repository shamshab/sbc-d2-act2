from random import randint

p1 = (input("Fold/Unfold:"))
c2 = randint(1,2)
c3 = randint(1,2) 

print("Player 1:", p1)

print("Computer 2:")
if c2 == 1:
    print("Fold")
else:
    print("Unfold")

print("Computer 3:")
if c3 == 1:
    print("Fold")
else:
    print("Unfold")

c2_choose = "Fold" if c2 == 1 else "Unfold"
c3_choose = "Fold" if c3 == 1 else "Unfold"

if (p1 == "Fold" and c2_choose == "Unfold" and c3_choose == "Unfold") or (p1 == "Unfold" and c2_choose == "Fold" and c3_choose == "Fold"):
    print("Player 1 Win!")

elif (p1 == "Unfold" and c2_choose == "Fold" and c3_choose == "Unfold") or (p1 == "Fold" and c2_choose == "Unfold" and c3_choose == "Fold"):
    print("Computer 2 Win!")

elif (p1 == "Unfold" and c2_choose == "Unfold" and c3_choose == "Fold") or (p1 == "Fold" and c2_choose == "Fold" and c3_choose == "Unfold"):
    print("Computer 3 Win!")

else:
    print("No one wins!")