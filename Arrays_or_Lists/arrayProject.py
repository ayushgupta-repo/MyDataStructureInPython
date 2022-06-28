# Taking input and calculating average
days = int(input('How many day\'s temperature? '))

days_temperature = []

for i in range(days):
    temperature = int(input('Day {}\'s high temp: '.format(i+1)))
    days_temperature.append(temperature)

sum = 0

for temp in days_temperature:
    sum += temp

average = sum/len(days_temperature)

print('Average =', average)

count = 0

for temp in days_temperature:
    if temp > average:
        count += 1

print('{} days(s) above average'.format(count))