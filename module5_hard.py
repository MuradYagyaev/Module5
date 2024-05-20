from hashlib import sha256
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = sha256(password.encode('utf-8')).hexdigest()
        self.age = age

    def __eq__(self, other):
        return self.nickname == other

    def password_ok(self, passw):
        return self.password == sha256(passw.encode('utf-8')).hexdigest()

    def __str__(self):
        return 'Текущий пользователь {}'.format(self.nickname)

    def __del__(self):
        pass


class Video:
    def __init__(self, title, duration, adult=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.title, self.duration, self.time_now, self.adult_mode)

    def __contains__(self, item):
        return self.title.lower().__contains__(item.lower())

    def video_watch(self):
        while self.time_now < self.duration:
            sleep(1)
            self.time_now += 1
            print(self.time_now, end=' ')
        print('Конец видео')


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, passw):
        for user in self.users:
            if user == login and user.password_ok(passw):
                self.current_user = user
                return
        print('Неверный пароль или логин')

    def register(self, name, passw, age_):
        for user in self.users:
            if user == name:
                print(f'Пользователь {name} уже существует!')
                return
        self.users.append(User(name, passw, age_))

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        self.videos.extend(video)

    def get_videos(self, find_string):
        titles = []
        for video in self.videos:
            if find_string in video:
                titles.append(video.title)
        return titles

    def watch_video(self, title_):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            for video in self.videos:
                if video.title == title_:
                    if not video.adult_mode or self.current_user.age > 18:
                        video.video_watch()
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
            # print('Нет такого видео!')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 3, True)
v3 = Video('Как программировать на пайтон?', 6)

# Добавление видео
ur.add(v1, v2)
ur.add(v3)

# Проверка поиска видео
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Регистрация пользователей
ur.register('pupkin', 'qwerty1', 15)
ur.register('bobrikov', 'qwerty2', 25)
# попытка регистрации пользователя с существующим никнеймом
ur.register('pupkin', 'qwerty3', 35)

# Проверка авторизации пользователя
ur.log_in('pupkin', 'qwerty1')
# попытка авторизации с неверным паролем
ur.log_in('bobrikov', 'qwerty1')
# выход
ur.log_out()

# Проверка воспроизведения видео и возрастное ограничение
# Попытка просмотра видео неавторизованным пользователем
ur.watch_video('Для чего девушкам парень программист?')
# Авторизация и попытка просмотра видео несовершеннолетним
ur.log_in('pupkin', 'qwerty1')
ur.watch_video('Для чего девушкам парень программист?')
# Просмотр несовершеннолетним разрешенного контента
ur.watch_video('Лучший язык программирования 2024 года')
# Аавторизация совершеннолетнего и просмотр видео
ur.log_in('bobrikov', 'qwerty2')
ur.watch_video('Для чего девушкам парень программист?')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print(ur.current_user)
