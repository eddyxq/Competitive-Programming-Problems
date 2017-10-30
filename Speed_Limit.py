num_pairs = 1

while num_pairs != -1:
    num_pairs = int(input())


    total_time = 0
    total_distance = 0
    for x in range(num_pairs):
        speed, time = input().split()
        speed = int(speed)
        time = int(time)
        time_elapsed = time - total_time
        total_time += time_elapsed
        distance = time_elapsed * speed
        total_distance += distance
    if num_pairs != -1:
        print(str(total_distance) + " miles")