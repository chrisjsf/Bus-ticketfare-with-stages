import math

distances = [10, 15, 5, 20, 15, 13, 15, 10]
stages = [0, 3, 5, 7, 8]

def distance_between_stages(src, dest):
    total = 0
    for i in range(src, dest):
        total += distances[i]
    return total
def calculate_fare(distance):
    if distance <= 2:
        return 20
    else:
        return 20 + (distance - 2) * 5
passengers = int(input("No. of passengers: "))
source = int(input("Source stop number: "))
destination = int(input("Destination stop number: "))
prev_stage = max([f for f in stages if f <= source])
next_stage = min([f for f in stages if f >= destination])
distance = distance_between_stages(prev_stage, next_stage)
fare = calculate_fare(distance)
total_fare = math.ceil(fare * passengers)
print(f"Ticket fare: Rs {total_fare}")
