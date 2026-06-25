import random
import time


class Allplayers:
    def __init__(self,players):
        self.players = players
    def add_user(self,user):
        self.players.append(user)
    def del_user(self,user):
        self.players.remove(user)
    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

class Player:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def main():
    allplayers = Allplayers([])
    allcards = []
    authorized = False
    while True:
        while not authorized:
            ans = input("Что вы хотите сделать?\n1.Регистрация\n2.Вход\n")
            if ans == '1':
                name = input('Введите имя:')
                player = allplayers.get_player(name)
                if player:
                    print('Такое имя уже существует.')
                else:
                    password = input('Введите пароль:')
                    if len(password) > 5:
                        player = Player(name,password)
                        allplayers.add_user(player)
                    else:
                        print("Пароль не может быть короче 5 символов!")
            elif ans == '2':
                name = input('Введите имя:')
                player = allplayers.get_player(name)
                if player:
                    password = input('Введите пароль:')
                    if password == player.password:
                         print("Вы успешно зашли в систему!")
                         authorized = True
                    else:
                        print("Неправильный пароль")
                else:
                    print("Неправильно введено имя/Не зарегестрировались")
            else:
                print('Неправильно ввели действие!')

        ans = input("Что вы хотите сделать?\n1.Добавить карточку\n2.Викторина\n")
        if ans == '1':
            question = input("Введите вопрос")
            answer = input("Введите ответ")
            card = Card(question,answer)
            allcards.append(card)
        elif ans == '2':
            if allcards:
                correct_answers = 0
                try:
                    questionnum = int(input("Сколько вопросов вы хотите?"))
                except ValueError:
                    print("Введите корректное число")
                else:
                    if questionnum == 0:
                        print("Больше вопросов")
                    elif questionnum > len(allcards):
                        print("Вы не можете ответить на количество вопросов больше которого у вас есть")
                    else:
                        quizcards = allcards.copy()
                        for i in range(questionnum):
                            start = time.time()
                            question = random.choice(quizcards)
                            print(question.question)
                            user_answer = input("Введите ответ: ")
                            end = time.time()
                            answertime = end - start
                            if answertime > 30:
                                print("Вы неуспели ответить на вопрос!")
                            else:
                                if user_answer.lower() == question.answer.lower():
                                    print("Вы ответили правильно!")
                                    correct_answers += 1
                                else:
                                    print("Неправильно, правильный ответ:", question.answer)
                            quizcards.remove(question)
                        print(f"Итоги Викторины:\nПравильные ответы: {correct_answers}")

            else:
                print("Нету ни одной карточки!")
        else:
            print("Неправильно ввели действие")

main()