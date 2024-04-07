size = int(input())
times = input()

ordered_times = times.split()
ordered_times = [int(x) for x in ordered_times]
ordered_times = sorted(ordered_times)
waiting_per_person = []

for i in range(size):
        getsum = sum(ordered_times[:i+1]) 
        waiting_per_person.append(getsum)

total = sum(waiting_per_person)
print(total)