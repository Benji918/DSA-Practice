# Calculate Average temperature
temp = []
print('How many day\'s temperature?')

while True:
    counter = len(temp) + 1
    user_input = input(f'Day {counter} high temp ')

    if user_input.lower() == 'done':
        break

    temp.append(int(user_input))

avg_temp = sum(temp)/len(temp)
print(f'Average = {avg_temp}')

max_day_temp_value = max(temp)
days_above_avg_temp = [v for v in temp if v > avg_temp]
print(f'{len(days_above_avg_temp)} days(s) is above average')




