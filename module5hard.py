import time
import datetime

class User:
    def __init__(self, nickname, password, year):
        self.nickname = nickname
        self.password = password
        self.age = int(datetime.datetime.now().year) - int(year)

class Video:
    def __init__(self, title, duration, time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

    def register(self, x):
        if not self.users:
            already_exists = False
        else:
            for i in self.users:
                if x.nickname == i.nickname:
                    already_exists = True
                else:
                    already_exists = False
        if already_exists:
            print("Пользователь уже существует")
        else:
            self.users.append(x)
            self.current_user = x

    def add_video(self, *args):
        for video in args:
            self.videos.append(video)

    def watch_video(self, name):
        in_videos = False
        for video in self.videos:
            if name in video.title and self.current_user and video.adult_mode == False:
                print(f'Старт видео {name}')
                for i in range(video.duration):
                    video.time_now += 1
                    print(video.time_now)
                    time.sleep(1)
                print("Конец видео")
                in_videos = True
            elif video.adult_mode:
                for_adults = True
                in_videos = True
            elif name in video.title:
                in_videos = True
            else:
                continue

        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif not in_videos:
            print("Фильм не найден")
        elif self.current_user.age < 18 and for_adults == True:
            print("Вам нет 18 лет, покиньте страницу")

    def get_videos(self, x):
        x = str(x).lower()
        video_list = []
        for video in self.videos:
            if x in str(video.title).lower():
                video_list.append(video.title)
            else:
                continue
        print(video_list)

    def log_out(self):
        self.current_user = None

    def log_in(self, login, password):
        for i in self.users:
            if login == i.nickname:
                user_exists = True
            else:
                user_exists = False
        if user_exists:
            if hash(i.password) == hash(password):
                print(f'Вход осуществлен, добро пожаловать, {login}')
            else:
                print("Пароли не совпадают")
        else:
            print("Пользователь не найден")


V1 = Video('Как правильно спать', 10, 0, True)
V2 = Video('Властелин колец', 8, 0)
V3 = Video('Один дома', 6, 0, True)
Ut = UrTube()
Ut.add_video(V1, V2, V3)
Ut.watch_video('Один дома')
Ut.get_videos("властелин")
User1 = User("Monster", "123qwerty", 1994)
User2 = User("Starr", "123qwerty", 2010)
User3 = User("Starr", "123qwerty", 2010)
Ut.register(User1)
Ut.register(User2)
Ut.register(User3)
Ut.log_in("Oldboy", "1qwerty")
Ut.log_in("Starr", "123qwerty")
Ut.watch_video('Один дома')