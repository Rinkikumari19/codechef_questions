T = int(input())
for i in range(T):
    Class_Id = input()
    if Class_Id == 'B' or Class_Id == 'b':
        print("BattleShip")
    elif Class_Id == 'C' or Class_Id == 'c':
        print("Cruiser")
    elif Class_Id == 'D' or Class_Id == 'd':
        print("Destroyer")
    else:
        print("Frigate")