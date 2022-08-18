# Микела́нджело Буонарро́ти 1475
# Леона́рдо да Ви́нчи 1452
# Винсе́нт Ви́ллем ван Гог 1853 г
# Сальвадо́р Дали́ 1904
# Пабло Пикассо 1881
while True:
    correctCount = 0
    incorrectCount = 0
    print('Викторина, назовите год рождения следующих художников:')
    mikel = input('Микела́нджело Буонарро́ти: ')
    if mikel == '1475':
        correctCount += 1
    else:
        incorrectCount += 1
    leo = input('Леона́рдо да Ви́нчи: ')
    if leo == '1452':
        correctCount += 1
    else:
        incorrectCount += 1
    vinset = input('Винсе́нт Ви́ллем ван Гог: ')
    if vinset == '1853':
        correctCount += 1
    else:
        incorrectCount += 1
    dali = input('Сальвадо́р Дали́: ')
    if dali == '1904':
        correctCount += 1
    else:
        incorrectCount += 1
    pablo = input('Пабло Пикассо: ')
    if pablo == '1881':
        correctCount += 1
    else:
        incorrectCount += 1
    print('Количество верных ответов:', correctCount)
    print('Количество неверных ответов:', incorrectCount)
    print('Процент правильных ответов:', correctCount*100/5)
    print('Процент неправильных ответов:', incorrectCount*100/5)
    answer = input('Начнем сначала?')
    if answer == 'нет':
        break