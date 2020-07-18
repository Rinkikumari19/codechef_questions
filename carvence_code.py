
T = int(input())
for i in range(T):
    car_no = int(input())
    cars = input()
    cars = cars.split()
    print(cars)
    count = cars[0]
    max = 1
    for index_of_cars in range(len(cars)-1):
        if count >= cars[index_of_cars+1]:   
            max = max + 1
            count = cars[index_of_cars+1]
    print(max)

# carvence