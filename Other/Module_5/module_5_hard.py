import time

class User:
    """
    Класс пользователя c атрибутами:
        nickname(имя пользователя, строка), password(принимает строку, хранит хэш-число), age(возраст, число)
    """
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash((nickname, password))
        self.age = age

    def __str__(self):
        return 'Имя: ' + self.nickname + ', Возраст: ' + str(self.age)

    def __eq__(self, other):
        return self.password == other.password

class Video:
    """
    Класс видеоролика с атрибутами:
        title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки),
        adult_mode(ограничение по возрасту, bool, False по умолчанию)
    """
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        msg = f'Заголовок: {self.title}, Продолжительность: {str(self.duration)}, Рейтинг 18+: '
        msg += 'Да' if self.adult_mode else 'Нет'
        return msg

    def __eq__(self, other):
        return self.title == other.title    # для "одинаковости" двух видеороликов достаточно совпадения их названий

class UrTube:
    """
    Класс платформы видеороликов.
        Атрибуты:
            users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, объект User)
        Методы:
            log_in(меняет current_user), register(добавляет пользователя в users), log_out, add(добавляет видео в
            videos), get_videos(поиск видео по названию, вывод перечня), watch_video(просмотр ролика)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, item):
        return any(list(item == self.videos[i] for i in self.videos))

    # endings of ordinal numbers - словарь окончаний порядковых числительных
    EON_dict = {'символ': ['ов', '', 'а', 'а', 'а', 'ов', 'ов', 'ов', 'ов', 'ов'],
                'совпадени': ['й', 'е', 'я', 'я', 'я', 'й', 'й', 'й', 'й', 'й']}

    def register(self, nickname: str, password: str, age: int):
        if any(map(lambda user: user.nickname == nickname, self.users)):
            print(f"Пользователь {nickname} уже существует!")
        else:                                           # создать нового пользователя, если nickname не найден
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)             # автоматический вход зарегистрированного пользователя

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        # список результата проверки имени и пароля во всех self.users (совпадение одновременно и имени и пароля):
        check_users = list(map(lambda user: (user.nickname == nickname) and
                                            (user.password == hash((nickname, password))), self.users))
        if any(check_users):
            self.current_user = self.users[check_users.index(True)] # вытащить User-а по индексу элемента со значением
                                # True в списке check_users
        else:       # если же имя и/или пароль не совпадают
            print('Пользователь с таким именем/паролем не найден')

    def add(self, *args: Video):
        for video in args:
            if not (video in self.videos):
                self.videos.append(video)

    def get_videos(self, *search_str: str):
        count = 0
        if search_str:        # аргумент присутствует
            print(f'В результате поиска строки "{search_str[0]}" найдено:')
            search_str = search_str[0].lower()
            for video in self.videos:
                if search_str in video.title.lower():
                    count += 1
                    print(count, '-', video)
            print(f'    Итого {count} совпадени{UrTube.EON_dict.get('совпадени')[int(str(count)[-1:])]}')
        else:
            print('Список имеющихся видео:')
            for i in range(len(self.videos)):
                print(i + 1 , '-', self.videos[i])


    def watch_video(self, search_str: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if search_str == video.title:
                if self.current_user.age < 18 and video.adult_mode:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                print(f'Воспроизведение видео "{search_str}":')
                for i in range(video.time_now, video.duration + 1):
                    print(i, end=' ')
                    time.sleep(1)
                print('Конец видео')
                video.time_now = 0
                break
        else:
            print(f'Видео с названием "{search_str}" не найдено')


if __name__ == '__main__':

    # Проверка вывода описания класса UrTube
    print(UrTube.__doc__)

    # Проверка на тестовых данных, манипуляции с передачей аргументов
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 7, 3)      # тут пауза на 3й секунде
    v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)
    v3 = Video('Растения против зомби или Чужие против Хищника?', duration=150)

    # Добавление видео
    ur.add(v1, v2, v1, v3)  # одинаковое видео V1 не добавится

    # Проверка поиска
    ur.get_videos('лучший')
    ur.get_videos('ПрО')

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.watch_video('Лучший язык программирования 2024 года')        # с третьей секунды
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Манипуляции с аккаунтами
    print('Попытка регистрации нового пользователя, чьё имя уже есть в системе:')
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print('  текущий пользователь  ', ur.current_user)
    ur.log_out()
    print('Выход из аккаунта:\n  текущий пользователь  ', ur.current_user)
    print('Вход под другим логином (с неправильным паролем):')
    ur.log_in('urban_pythonist', 'iScX4vAgF')
    print('  текущий пользователь  ', ur.current_user)
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    print('Теперь тот же User, но с правильным паролем:\n  текущий пользователь  ', ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # Проверка вывода полного списка видео (3 шт.) при запросе "пустого поиска"
    ur.get_videos()

    # Проверка вывода полного списка пользователей
    print('Список всех пользователей:', *ur.users, sep='\n')

