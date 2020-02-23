import random
guessT = 0
print("Желаешь заработать??Как тебя зовут?")
name = input("Введите имя: ")
num = random.randint(0,20)
 
print("Привет {} ,тогда давай начнём) Угадай число" .format(name))
while guessT < 6:
    print("Как ты думаешь,какое?")
    guessnum = input()
    guessnum = int(guessnum)
    guessT = guessT+1

    if guessnum < num:
        print("Загаданое число больше чем твоё( ")
    if guessnum > num:
        print("Загаданое число меньше чем твоё( ")
    if guessnum == num:
        break

if guessnum == num:
    guessT = str(guessT)
    print("Ты угадал!Поздравляю тебя,ты выиграл мешок картошки))")
if guessnum != num:
    num = str(num)
    print("Ты не угадал, та и попытки закончились ,с тебя милион долларов(( ")
