# Использование %:
team1_num = 5
print('В команде Мастера кода участников: %s ! ' % team1_num)

team2_num = 6
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print()

# Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
team1_time = 18015.2
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
print()

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'победа команды Волшебники Данных!'
else:
    result = 'ничья!'
challenge_result = result
print(f'Результат битвы: {challenge_result}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
