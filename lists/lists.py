# Calculate Average temperature
temp = [] # O(1)
print('How many day\'s temperature?')# O(1)

while True: # O(n)
    counter = len(temp) + 1 # O(1)
    user_input = input(f'Day {counter} high temp ') # O(1)

    if user_input.lower() == 'done': # O(1)
        break

    temp.append(int(user_input)) # 0(1)

avg_temp = sum(temp)/len(temp)  # O(1)
print(f'Average = {avg_temp}')  # O(1)

max_day_temp_value = max(temp)   # O(1)
days_above_avg_temp = [v for v in temp if v > avg_temp]  # O(n)
print(f'{len(days_above_avg_temp)} days(s) is above average')  # 0{1)


def missing_number(arr, n):
    sum_of_n = n*(n+1)//2
    sum_of_array = sum(arr)
    return sum_of_n - sum_of_array


print(missing_number([1, 2, 3, 4, 6], 6))






