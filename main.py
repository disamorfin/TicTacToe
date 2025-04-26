from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGridLayout,QSpacerItem,QSizePolicy,QMessageBox,QSplashScreen,QProgressBar
from PyQt6.QtCore import QSize, Qt, QUrl,QTimer,QThread,pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap,QPainter
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
import sys, os, random,time
import json
from styles import statistic_label_style, button_style, progressbar_style, loading_label_style, settings_label_style,night_loading_label_style, night_button_style
from animated_toggle import AnimatedToggle

class CellButton(QPushButton):
    def __init__(self, row, col, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col
        self.setFixedSize(110, 110)
        self.setStyleSheet("font-size: 100px;"
                           "background:white;"
                           "color:red;"
                           "text-align: center;"
                           "border:none;"
                           )
class Worker(QThread):
    progress_changed = pyqtSignal(int)

    def run(self):
        i = 0
        while i != 25: 
            time.sleep(0.02)
            self.progress_changed.emit(i)
            i+=1
        while i != 35:
            time.sleep(0.09)
            self.progress_changed.emit(i)
            i+=1
        while i!= 50:
            time.sleep(0.02)
            self.progress_changed.emit(i)
            i+=1
        while i!= 60:
            time.sleep(0.15)
            self.progress_changed.emit(i)
            i+=1
        while i!= 95:
            time.sleep(0.03)
            self.progress_changed.emit(i)
            i+=1
        while i!=101:
            time.sleep(0.25)
            self.progress_changed.emit(i)
            i+=1
            
class MainMenu(QWidget):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle('Крестики нолики')

        current_dir = os.path.dirname(os.path.abspath(__file__))

        icon_path = os.path.join(current_dir, "img", "icons8-крестики-нолики-64.png")

        self.background_image_day_path = os.path.join(current_dir, "img", "TryLoadScreen.png")
        self.background_image_night_path = os.path.join(current_dir, "img","night.jpg")

        self.setWindowIcon(QIcon(icon_path))

        self.layout = QGridLayout()

        self.toggler = AnimatedToggle(bar_color=Qt.GlobalColor.yellow,handle_color=Qt.GlobalColor.darkYellow)
        self.play_button = QPushButton("Играть")
        self.statistic_button = QPushButton("Статистика")
        self.settings_button = QPushButton("Настройки")
        self.quit_button = QPushButton("Выйти")
        self.easylvl_button = QPushButton("Легкий")
        self.mediumlvl_button = QPushButton("Средний")
        self.hardlvl_button = QPushButton("Сложный")
        self.choose_lvl = QLabel("Выберите уровень")
        self.full_screen_button = QPushButton("Полноэкранный")
        self.window_screen_button = QPushButton("В окне")
        self.back_to_main_menu_button = QPushButton("Вернуться в меню")
        self.vs_bot_button = QPushButton("Один")
        self.vs_human_button = QPushButton("Вдвоем")
        self.daynightlabel = QLabel("День")
        self.replay_button = QPushButton("Начать заново")
        self.bot_statistic_button = QPushButton("Против бота")
        self.human_statistic_button = QPushButton("Против человека")
        self.null_statistic_button = QPushButton("Обнулить")
        self.null_statistic_button_human = QPushButton("Обнулить")
        self.graph_settings_button = QPushButton("Экран")
        self.game_settings_button = QPushButton("Игра")
        self.game_launch_button = QPushButton("Заставка ВКЛ")
        self.mod_label = QLabel("Уровень")
        self.win_label = QLabel("Победа")
        self.lose_label = QLabel("Поражение")
        self.draw_label = QLabel("Ничья")
        self.ez_mod_label = QLabel("Легкий")
        self.med_mod_label = QLabel("Средний")
        self.hard_mod_label = QLabel("Сложный")
        self.X_player_label = QLabel("Игрок X")
        self.O_player_label = QLabel("Игрок O")
        self.word_player_label = QLabel("Игроки")
        self.loading_label = QLabel("Добро")
        
        self.winning_combinations = [
            [2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26],
        
            [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [6, 11, 16, 21, 26],
        
            [2, 8, 14, 20, 26], [6, 10, 14, 18, 22]
        ]

        self.list_index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        self.med_index = 0
        self.index = 0
        self.def_counter = 0
        self.random_index = 0
        self.hard_index = 0
        self.X_combinations = []
        self.O_combinations = []
        self.trywinlist = []
        self.spacer = QWidget()
        self.spacer2 = QWidget()
        self.gamemod = "Nothing"
        self.current_symbol= "X"
        self.now_page = 'Main'
        self.fails = 0
        self.med_counter = 0
        self.dayornight = self.got_value("dayornight")
        self.game_launch = self.got_value("game_launch")
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.trackplay_button = QPushButton('▶')
        self.trackplay_button_feel = False
        self.bot = None

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setTextVisible(False)

        self.ez_win_statistic_value = self.got_value('const_ez_win')
        self.ez_lose_statistic_value = self.got_value('const_ez_lose')
        self.ez_draw_statistic_value = int(self.got_value('const_ez_draw'))
        self.med_win_statistic_value = self.got_value('const_med_win')
        self.med_lose_statistic_value = self.got_value('const_med_lose')
        self.med_draw_statistic_value = int(self.got_value('const_med_draw'))
        self.hard_win_statistic_value = self.got_value('const_hard_win')
        self.hard_lose_statistic_value = self.got_value('const_hard_lose')
        self.hard_draw_statistic_value = int(self.got_value('const_hard_draw'))

        self.X_statistic_value = int(self.got_value("const_vs_player_X"))
        self.O_statistic_value = int(self.got_value("const_vs_player_O"))
        self.Player_draw_statistic_value = int(self.got_value("const_vs_player_draw"))

        self.ez_win_statistic = QLabel()
        self.ez_win_statistic.setObjectName("WinLabel")
        self.ez_win_statistic.setText(str(self.ez_win_statistic_value))
        self.ez_lose_statistic = QLabel()
        self.ez_lose_statistic.setObjectName("LoseLabel")
        self.ez_lose_statistic.setText(str(self.ez_lose_statistic_value))
        self.ez_draw_statistic = QLabel()
        self.ez_draw_statistic.setObjectName("DrawLabel")
        self.ez_draw_statistic.setText(str(self.ez_draw_statistic_value))
        self.med_win_statistic = QLabel()
        self.med_win_statistic.setObjectName("WinLabel")
        self.med_win_statistic.setText(str(self.med_win_statistic_value))
        self.med_lose_statistic = QLabel()
        self.med_lose_statistic.setObjectName("LoseLabel")
        self.med_lose_statistic.setText(str(self.med_lose_statistic_value))
        self.med_draw_statistic = QLabel()
        self.med_draw_statistic.setObjectName("DrawLabel")
        self.med_draw_statistic.setText(str(self.med_draw_statistic_value))
        self.hard_win_statistic = QLabel()
        self.hard_win_statistic.setObjectName("WinLabel")
        self.hard_win_statistic.setText(str(self.hard_win_statistic_value))
        self.hard_lose_statistic = QLabel()    
        self.hard_lose_statistic.setObjectName("LoseLabel")
        self.hard_lose_statistic.setText(str(self.hard_lose_statistic_value))
        self.hard_draw_statistic = QLabel()
        self.hard_draw_statistic.setObjectName("DrawLabel")
        self.hard_draw_statistic.setText(str(self.hard_draw_statistic_value))
        self.X_player_statistic = QLabel()
        self.X_player_statistic.setObjectName("WinLabel")
        self.X_player_statistic.setText(str(self.X_statistic_value))
        self.O_player_statistic = QLabel()
        self.O_player_statistic.setObjectName("WinLabel")
        self.O_player_statistic.setText(str(self.O_statistic_value))
        self.draw_player_statistic = QLabel()
        self.draw_player_statistic.setObjectName("DrawPlayerLabel")
        self.draw_player_statistic.setText(str(self.Player_draw_statistic_value))
        self.draw_player_statistic2 = QLabel()
        self.draw_player_statistic2.setObjectName("DrawPlayerLabel")
        self.draw_player_statistic2.setText(str(self.Player_draw_statistic_value))

        self.replay_button.setObjectName("ReplayButton")
        self.back_to_main_menu_button.setObjectName("MenuButton")
        self.trackplay_button.setObjectName("TrackButton")
        self.null_statistic_button.setObjectName("NullButton")
        self.null_statistic_button_human.setObjectName("NullButton")
        self.graph_settings_button.setObjectName("SettingsButton")
        self.game_settings_button.setObjectName("SettingsButton")
        self.full_screen_button.setObjectName("SettingsUseButton")
        self.window_screen_button.setObjectName("SettingsUseButton")
        self.game_launch_button.setObjectName("SettingsUseButton")

        if self.game_launch == 1:
            self.layout.addWidget(self.spacer, 0, 0)
            self.layout.addWidget(self.loading_label, 0, 1)
            self.layout.addWidget(self.progress_bar, 4, 1)
            self.layout.addWidget(self.spacer, 0, 3)
            self.layout.addWidget(self.spacer, 5, 3)
            self.layout.addWidget(self.spacer, 4, 3)
            self.start_task()
        else:
            self.layout.removeWidget(self.progress_bar)
            self.progress_bar.hide()
            self.layout.removeWidget(self.loading_label)
            self.loading_label.hide()

            self.layout.addWidget(self.spacer, 0, 0)
            self.layout.addWidget(self.play_button, 1, 2)
            self.layout.addWidget(self.statistic_button, 2, 2)
            self.layout.addWidget(self.settings_button, 3, 2)
            self.layout.addWidget(self.quit_button, 4, 2)
            self.layout.addWidget(self.spacer, 0, 3)
            self.layout.addWidget(self.spacer, 5, 3)
            self.layout.addWidget(self.spacer, 4, 3)

        self.cells = []

        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.resize(screen_width, screen_height)

        if self.dayornight == 0:

            self.progress_bar.setStyleSheet(progressbar_style)
            self.play_button.setStyleSheet(button_style)
            self.statistic_button.setStyleSheet(button_style)
            self.settings_button.setStyleSheet(button_style)
            self.quit_button.setStyleSheet(button_style)
            self.easylvl_button.setStyleSheet(button_style)
            self.mediumlvl_button.setStyleSheet(button_style)
            self.hardlvl_button.setStyleSheet(button_style)
            self.full_screen_button.setStyleSheet(button_style)
            self.window_screen_button.setStyleSheet(button_style)
            self.back_to_main_menu_button.setStyleSheet(button_style)
            self.vs_bot_button.setStyleSheet(button_style)
            self.vs_human_button.setStyleSheet(button_style)
            self.replay_button.setStyleSheet(button_style)
            self.trackplay_button.setStyleSheet(button_style)
            self.human_statistic_button.setStyleSheet(button_style)
            self.bot_statistic_button.setStyleSheet(button_style)
            self.mod_label.setStyleSheet(statistic_label_style)
            self.ez_mod_label.setStyleSheet(statistic_label_style)
            self.med_mod_label.setStyleSheet(statistic_label_style)
            self.hard_mod_label.setStyleSheet(statistic_label_style)
            self.win_label.setStyleSheet(statistic_label_style)
            self.lose_label.setStyleSheet(statistic_label_style)
            self.draw_label.setStyleSheet(statistic_label_style)
            self.ez_win_statistic.setStyleSheet(statistic_label_style)
            self.ez_lose_statistic.setStyleSheet(statistic_label_style)
            self.ez_draw_statistic.setStyleSheet(statistic_label_style)
            self.med_win_statistic.setStyleSheet(statistic_label_style)
            self.med_lose_statistic.setStyleSheet(statistic_label_style)
            self.med_draw_statistic.setStyleSheet(statistic_label_style)
            self.hard_win_statistic.setStyleSheet(statistic_label_style)
            self.hard_lose_statistic.setStyleSheet(statistic_label_style)
            self.hard_draw_statistic.setStyleSheet(statistic_label_style)
            self.null_statistic_button.setStyleSheet(button_style)
            self.X_player_label.setStyleSheet(statistic_label_style)
            self.word_player_label.setStyleSheet(statistic_label_style)
            self.O_player_label.setStyleSheet(statistic_label_style)
            self.X_player_statistic.setStyleSheet(statistic_label_style)
            self.O_player_statistic.setStyleSheet(statistic_label_style)
            self.draw_player_statistic.setStyleSheet(statistic_label_style)
            self.draw_player_statistic2.setStyleSheet(statistic_label_style)
            self.null_statistic_button_human.setStyleSheet(button_style)
            self.loading_label.setStyleSheet(loading_label_style)
            self.graph_settings_button.setStyleSheet(button_style)
            self.game_settings_button.setStyleSheet(button_style)
            self.game_launch_button.setStyleSheet(button_style)
            self.daynightlabel.setStyleSheet(settings_label_style)

        if self.dayornight == 1:

            self.progress_bar.setStyleSheet(progressbar_style)
            self.play_button.setStyleSheet(night_button_style)
            self.statistic_button.setStyleSheet(night_button_style)
            self.settings_button.setStyleSheet(night_button_style)
            self.quit_button.setStyleSheet(night_button_style)
            self.easylvl_button.setStyleSheet(night_button_style)
            self.mediumlvl_button.setStyleSheet(night_button_style)
            self.hardlvl_button.setStyleSheet(night_button_style)
            self.full_screen_button.setStyleSheet(night_button_style)
            self.window_screen_button.setStyleSheet(night_button_style)
            self.back_to_main_menu_button.setStyleSheet(night_button_style)
            self.vs_bot_button.setStyleSheet(night_button_style)
            self.vs_human_button.setStyleSheet(night_button_style)
            self.replay_button.setStyleSheet(night_button_style)
            self.trackplay_button.setStyleSheet(night_button_style)
            self.human_statistic_button.setStyleSheet(night_button_style)
            self.bot_statistic_button.setStyleSheet(night_button_style)
            self.mod_label.setStyleSheet(statistic_label_style)
            self.ez_mod_label.setStyleSheet(statistic_label_style)
            self.med_mod_label.setStyleSheet(statistic_label_style)
            self.hard_mod_label.setStyleSheet(statistic_label_style)
            self.win_label.setStyleSheet(statistic_label_style)
            self.lose_label.setStyleSheet(statistic_label_style)
            self.draw_label.setStyleSheet(statistic_label_style)
            self.ez_win_statistic.setStyleSheet(statistic_label_style)
            self.ez_lose_statistic.setStyleSheet(statistic_label_style)
            self.ez_draw_statistic.setStyleSheet(statistic_label_style)
            self.med_win_statistic.setStyleSheet(statistic_label_style)
            self.med_lose_statistic.setStyleSheet(statistic_label_style)
            self.med_draw_statistic.setStyleSheet(statistic_label_style)
            self.hard_win_statistic.setStyleSheet(statistic_label_style)
            self.hard_lose_statistic.setStyleSheet(statistic_label_style)
            self.hard_draw_statistic.setStyleSheet(statistic_label_style)
            self.null_statistic_button.setStyleSheet(night_button_style)
            self.X_player_label.setStyleSheet(statistic_label_style)
            self.word_player_label.setStyleSheet(statistic_label_style)
            self.O_player_label.setStyleSheet(statistic_label_style)
            self.X_player_statistic.setStyleSheet(statistic_label_style)
            self.O_player_statistic.setStyleSheet(statistic_label_style)
            self.draw_player_statistic.setStyleSheet(statistic_label_style)
            self.draw_player_statistic2.setStyleSheet(statistic_label_style)
            self.null_statistic_button_human.setStyleSheet(night_button_style)
            self.loading_label.setStyleSheet(night_loading_label_style)
            self.graph_settings_button.setStyleSheet(night_button_style)
            self.game_settings_button.setStyleSheet(night_button_style)
            self.game_launch_button.setStyleSheet(night_button_style)
            self.daynightlabel.setStyleSheet(settings_label_style)    


        self.mod_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.draw_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.win_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lose_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ez_mod_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.med_mod_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hard_mod_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ez_win_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ez_lose_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ez_draw_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.med_win_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.med_lose_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.med_draw_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hard_win_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hard_lose_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hard_draw_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.X_player_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.draw_player_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.O_player_statistic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.draw_player_statistic2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.X_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.O_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.daynightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.play_button.clicked.connect(self.play_button_clicked)
        self.statistic_button.clicked.connect(self.statistic_button_clicked)
        self.settings_button.clicked.connect(self.settings_button_clicked)
        self.quit_button.clicked.connect(app.quit)
        self.full_screen_button.clicked.connect(self.full_screen_button_clicked)
        self.window_screen_button.clicked.connect(self.window_screen_button_clicked)
        self.back_to_main_menu_button.clicked.connect(self.back_to_main_menu_button_clicked)
        self.vs_bot_button.clicked.connect(self.play_button_ii_clicked)
        self.vs_human_button.clicked.connect(self.vs_human_button_clicked)
        self.replay_button.clicked.connect(self.replay_button_clicked)
        self.easylvl_button.clicked.connect(self.easylvl_button_clicked)
        self.mediumlvl_button.clicked.connect(self.mediumlvl_button_clicked)
        self.bot_statistic_button.clicked.connect(self.bot_statistic_button_clicked)
        self.human_statistic_button.clicked.connect(self.human_statistic_button_clicked)
        self.graph_settings_button.clicked.connect(self.graph_settings_button_clicked)
        self.game_settings_button.clicked.connect(self.game_settings_button_clicked)
        self.game_launch_button.clicked.connect(self.game_launch_button_clicked)
        self.setLayout(self.layout)
        self.media_player.setSource(QUrl.fromLocalFile("mp3\Lonely(minus).mp3"))
        self.trackplay_button.clicked.connect(self.trackplay_button_clicked)
        self.null_statistic_button.clicked.connect(self.null_statistic_button_clicked)
        self.null_statistic_button_human.clicked.connect(self.null_statistic_button_human_clicked)
        self.initialize_ai()
        self.hardlvl_button.clicked.connect(self.hardlvl_button_clicked)
        self.toggler.clicked.connect(self.toggler_clicked)

        if self.dayornight == 0: 
            self.background_image = QPixmap(self.background_image_day_path)
        elif self.dayornight == 1:
            self.background_image = QPixmap(self.background_image_night_path)

    def start_task(self):
        self.worker = Worker() 
        self.worker.progress_changed.connect(self.update_progress)
        self.worker.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        if value == 30:
            self.loading_label.setText("Добро пожаловать")
        if value == 60:
            self.loading_label.setText("Добро пожаловать в игру!")
        if value == 100:
            self.layout.removeWidget(self.progress_bar)
            self.progress_bar.hide()
            self.layout.removeWidget(self.loading_label)
            self.loading_label.hide()
            self.layout.addWidget(self.spacer, 0, 0)
            self.layout.addWidget(self.play_button, 1, 2)
            self.layout.addWidget(self.statistic_button, 2, 2)
            self.layout.addWidget(self.settings_button, 3, 2)
            self.layout.addWidget(self.quit_button, 4, 2)
            self.layout.addWidget(self.spacer, 0, 3)
            self.layout.addWidget(self.spacer, 5, 3)
            self.layout.addWidget(self.spacer, 4, 3)

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.background_image.isNull(): 
            painter.drawPixmap(self.rect(), self.background_image)

    def initialize_ai(self):
        from defs_ai import MedClass 
        self.bot = MedClass()

    def make_med_ai_move(self):
        if self.bot:
            self.bot.make_med_ai_move()
        else:
            print('Err')
    
    def make_ez_ai_move(self):
        if self.bot:
            self.bot.make_ez_ai_move()
        else:
            print('Err')

    def got_value (self,name):
        with open('data.json') as f:
            data = json.load(f)
            value = data[name]
            return(value)

    def load_data(self,filename='data.json'):
        with open(filename, 'r') as file:
            return json.load(file)

    def save_data(self,data, filename='data.json'):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    
    def increase_variable (self, variable_name, increment, filename='data.json'):
        data = self.load_data(filename)
       
        if variable_name in data:
            data[variable_name] += increment
       
        self.save_data(data, filename)

        return data[variable_name]
    
    def play_button_clicked(self):
        
        self.now_page = 'Play'

        self.layout.removeWidget(self.spacer)
        self.spacer.hide()
        self.layout.removeWidget(self.play_button)
        self.play_button.hide()
        self.layout.removeWidget(self.statistic_button)
        self.statistic_button.hide()
        self.layout.removeWidget(self.settings_button)
        self.settings_button.hide()
        self.layout.removeWidget(self.quit_button)
        self.quit_button.hide()
        self.layout.removeWidget(self.trackplay_button)
        self.trackplay_button.hide()

        self.layout.addWidget(self.back_to_main_menu_button, 0, 0)
        self.layout.addWidget(self.vs_bot_button, 2, 2)
        self.layout.addWidget(self.vs_human_button, 3, 2)
        self.layout.addWidget(self.spacer, 4, 2)
        self.layout.addWidget(self.spacer, 4, 3)
        self.layout.addWidget(self.spacer2, 1, 3)

        self.vs_bot_button.show()
        self.vs_human_button.show()
        self.back_to_main_menu_button.show()
        self.spacer.show()
        self.spacer2.show()

    def play_button_ii_clicked(self):
        self.now_page = 'Play_ii'

        self.layout.removeWidget(self.spacer)
        self.layout.removeWidget(self.vs_bot_button)
        self.vs_bot_button.hide()
        self.layout.removeWidget(self.vs_human_button)
        self.vs_human_button.hide()
  
        self.layout.addWidget(self.back_to_main_menu_button, 0, 0)
        self.layout.addWidget(self.easylvl_button, 2, 3)
        self.layout.addWidget(self.mediumlvl_button, 3, 3)
        self.layout.addWidget(self.hardlvl_button, 4, 3)
        self.layout.addWidget(self.spacer, 5, 4)

        self.back_to_main_menu_button.show()
        self.easylvl_button.show()
        self.mediumlvl_button.show()
        self.hardlvl_button.show()
        self.spacer.show()

    def statistic_button_clicked(self):

        self.ez_win_statistic_value = self.got_value('const_ez_win')
        self.ez_lose_statistic_value = self.got_value('const_ez_lose')
        self.ez_draw_statistic_value = int(self.got_value('const_ez_draw'))
        self.med_win_statistic_value = self.got_value('const_med_win')
        self.med_lose_statistic_value = self.got_value('const_med_lose')
        self.med_draw_statistic_value = int(self.got_value('const_med_draw'))
        self.hard_win_statistic_value = self.got_value('const_hard_win')
        self.hard_lose_statistic_value = self.got_value('const_hard_lose')
        self.hard_draw_statistic_value = int(self.got_value('const_hard_draw'))
        self.X_statistic_value = self.got_value("const_vs_player_X")
        self.O_statistic_value = self.got_value("const_vs_player_O")
        self.Player_draw_statistic_value = int(self.got_value("const_vs_player_draw"))

        self.ez_win_statistic.setText(str(self.ez_win_statistic_value))
        self.ez_lose_statistic.setText(str(self.ez_lose_statistic_value))
        self.ez_draw_statistic.setText(str(self.ez_draw_statistic_value))
        self.med_win_statistic.setText(str(self.med_win_statistic_value))
        self.med_lose_statistic.setText(str(self.med_lose_statistic_value))
        self.med_draw_statistic.setText(str(self.med_draw_statistic_value))
        self.hard_win_statistic.setText(str(self.hard_win_statistic_value))
        self.hard_lose_statistic.setText(str(self.hard_lose_statistic_value))
        self.hard_draw_statistic.setText(str(self.hard_draw_statistic_value))
        self.X_player_statistic.setText(str(self.X_statistic_value))
        self.O_player_statistic.setText(str(self.O_statistic_value))
        self.draw_player_statistic.setText(str(self.Player_draw_statistic_value))
        self.draw_player_statistic2.setText(str(self.Player_draw_statistic_value))

        self.now_page = 'Statistic'

        self.layout.removeWidget(self.spacer)
        self.layout.removeWidget(self.spacer2)

        self.layout.removeWidget(self.play_button)
        self.play_button.hide()
        self.layout.removeWidget(self.statistic_button)
        self.statistic_button.hide()
        self.layout.removeWidget(self.settings_button)
        self.settings_button.hide()
        self.layout.removeWidget(self.quit_button)
        self.quit_button.hide()

        self.layout.addWidget(self.back_to_main_menu_button, 0, 0)
        self.layout.addWidget(self.human_statistic_button, 2, 2)
        self.layout.addWidget(self.bot_statistic_button, 3, 2)
        self.layout.addWidget(self.spacer, 4, 3)
        self.layout.addWidget(self.spacer2, 1, 3)

        self.back_to_main_menu_button.show()
        self.human_statistic_button.show()
        self.bot_statistic_button.show()
        self.spacer2.show()

    def game_launch_button_clicked(self):
        self.game_launch = self.got_value("game_launch")
        if self.game_launch == 1:
            self.game_launch = 0
            self.increase_variable("game_launch" , -1)
            self.game_launch_button.setText("Заставка ВЫКЛ")
        elif self.game_launch == 0:
            self.game_launch = 1
            self.increase_variable("game_launch" , 1)
            self.game_launch_button.setText("Заставка ВКЛ")

    def sound_settings_button_clicked(self):
        pass

    def game_settings_button_clicked(self):

        self.dayornight = self.got_value("dayornight")

        if self.game_launch == 1:
            self.game_launch_button.setText("Заставка ВКЛ")
        elif self.game_launch == 0:
            self.game_launch_button.setText("Заставка ВЫКЛ")   

        self.layout.removeWidget(self.full_screen_button)
        self.full_screen_button.hide()
        self.layout.removeWidget(self.window_screen_button)
        self.window_screen_button.hide()

        if self.dayornight == 1:

            self.toggler.setChecked(True)
            self.layout.addWidget(self.toggler, 3, 5)
            
            self.daynightlabel.setText("Ночь")
            self.daynightlabel.setStyleSheet('''font-size:70px;
                                                color: white;
                                                ''')
        elif self.dayornight == 0:

            self.toggler.setChecked(False)
            self.layout.addWidget(self.toggler, 3, 5)

            self.daynightlabel.setText("День")
            self.daynightlabel.setStyleSheet('''font-size:70px;
                                                color: black;
                                             
                                                ''')

        self.layout.addWidget(self.game_launch_button, 4, 4, 1, 2)
        self.layout.addWidget(self.daynightlabel, 3, 4)

        self.layout.addWidget(self.spacer2, 2, 0)
        self.layout.addWidget(self.spacer, 5, 0)

        self.game_launch_button.show()
        self.spacer.show()
        self.spacer2.show()
        self.toggler.show()
        self.daynightlabel.show()

    def toggler_clicked(self):

        self.dayornight = self.got_value("dayornight")
        if self.dayornight == 0:

            self.background_image = QPixmap(self.background_image_night_path)

            self.increase_variable("dayornight", 1)
            self.daynightlabel.setText("Ночь")
            self.daynightlabel.setStyleSheet('''font-size:70px;
                                                color: white;''')

            self.play_button.setStyleSheet(night_button_style)
            self.statistic_button.setStyleSheet(night_button_style)
            self.settings_button.setStyleSheet(night_button_style)
            self.quit_button.setStyleSheet(night_button_style)
            self.easylvl_button.setStyleSheet(night_button_style)
            self.mediumlvl_button.setStyleSheet(night_button_style)
            self.hardlvl_button.setStyleSheet(night_button_style)
            self.full_screen_button.setStyleSheet(night_button_style)
            self.window_screen_button.setStyleSheet(night_button_style)
            self.back_to_main_menu_button.setStyleSheet(night_button_style)
            self.vs_bot_button.setStyleSheet(night_button_style)
            self.vs_human_button.setStyleSheet(night_button_style)
            self.replay_button.setStyleSheet(night_button_style)
            self.trackplay_button.setStyleSheet(night_button_style)
            self.human_statistic_button.setStyleSheet(night_button_style)
            self.bot_statistic_button.setStyleSheet(night_button_style)
            self.graph_settings_button.setStyleSheet(night_button_style)
            self.game_settings_button.setStyleSheet(night_button_style)
            self.game_launch_button.setStyleSheet(night_button_style)
            self.null_statistic_button.setStyleSheet(night_button_style)
            
        elif self.dayornight == 1:

            self.background_image = QPixmap(self.background_image_day_path)

            self.increase_variable("dayornight", -1)
            self.daynightlabel.setText("День")
            self.daynightlabel.setStyleSheet('''font-size:70px;
                                                color: black;''')
            self.play_button.setStyleSheet(button_style)
            self.statistic_button.setStyleSheet(button_style)
            self.settings_button.setStyleSheet(button_style)
            self.quit_button.setStyleSheet(button_style)
            self.easylvl_button.setStyleSheet(button_style)
            self.mediumlvl_button.setStyleSheet(button_style)
            self.hardlvl_button.setStyleSheet(button_style)
            self.full_screen_button.setStyleSheet(button_style)
            self.window_screen_button.setStyleSheet(button_style)
            self.back_to_main_menu_button.setStyleSheet(button_style)
            self.vs_bot_button.setStyleSheet(button_style)
            self.vs_human_button.setStyleSheet(button_style)
            self.replay_button.setStyleSheet(button_style)
            self.trackplay_button.setStyleSheet(button_style)
            self.human_statistic_button.setStyleSheet(button_style)
            self.bot_statistic_button.setStyleSheet(button_style)
            self.graph_settings_button.setStyleSheet(button_style)
            self.game_settings_button.setStyleSheet(button_style)
            self.game_launch_button.setStyleSheet(button_style)
            self.null_statistic_button.setStyleSheet(button_style)

        self.update()

    def settings_button_clicked(self):

        self.now_page = 'Settings'
        self.layout.removeWidget(self.play_button)
        self.play_button.hide()
        self.layout.removeWidget(self.statistic_button)
        self.statistic_button.hide()
        self.layout.removeWidget(self.settings_button)
        self.settings_button.hide()
        self.layout.removeWidget(self.quit_button)
        self.quit_button.hide()
        self.layout.removeWidget(self.spacer)
        self.layout.removeWidget(self.spacer2)
        
        self.layout.addWidget(self.back_to_main_menu_button, 0, 0)
        self.layout.addWidget(self.graph_settings_button, 1, 0, 1 ,2)
        self.layout.addWidget(self.game_settings_button, 1, 4, 1 ,2)
        self.layout.addWidget(self.spacer, 5, 0)

        self.back_to_main_menu_button.show()
        self.graph_settings_button.show()
        self.game_settings_button.show()
        self.spacer.show()

    def graph_settings_button_clicked(self):
        
        self.layout.removeWidget(self.game_launch_button)
        self.game_launch_button.hide()
        self.layout.removeWidget(self.toggler)
        self.toggler.hide()
        self.layout.removeWidget(self.daynightlabel)
        self.daynightlabel.hide()

        self.layout.addWidget(self.full_screen_button, 3, 0, 1, 2)
        self.layout.addWidget(self.window_screen_button, 4, 0, 1, 2)
        self.layout.addWidget(self.spacer2, 2, 0)
        self.layout.addWidget(self.spacer, 5, 0)
        
        self.window_screen_button.show()
        self.full_screen_button.show()
        self.spacer2.show()

    def full_screen_button_clicked(self):
        menu_window.showFullScreen()

    def window_screen_button_clicked(self):
        menu_window.showNormal()

    def back_to_main_menu_button_clicked(self):

        if self.now_page == 'Play_ii':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.easylvl_button)
            self.easylvl_button.hide()
            self.layout.removeWidget(self.mediumlvl_button)
            self.mediumlvl_button.hide()
            self.layout.removeWidget(self.hardlvl_button)
            self.hardlvl_button.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()

        if self.now_page == 'Settings':
            
            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.game_settings_button)
            self.game_settings_button.hide()
            self.layout.removeWidget(self.graph_settings_button)
            self.graph_settings_button.hide()
            self.layout.removeWidget(self.full_screen_button)
            self.full_screen_button.hide()
            self.layout.removeWidget(self.window_screen_button)
            self.window_screen_button.hide()
            self.layout.removeWidget(self.game_launch_button)
            self.game_launch_button.hide()
            self.layout.removeWidget(self.toggler)
            self.toggler.hide()
            self.layout.removeWidget(self.daynightlabel)
            self.daynightlabel.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Play':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.vs_bot_button)
            self.vs_bot_button.hide()
            self.layout.removeWidget(self.vs_human_button)
            self.vs_human_button.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Vs_human':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.O_combinations = []
            self.X_combinations = []
            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.replay_button)
            self.replay_button.hide()

            for row in self.cells:
                for self.cell in row:
                    if self.cell.isVisible():
                        self.layout.removeWidget(self.cell)
                        self.cell.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Easy_lvl':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.list_index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
            self.O_combinations = []
            self.X_combinations = []
            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.replay_button)
            self.replay_button.hide()

            for row in self.cells:
                for self.cell in row:
                    if self.cell.isVisible():
                        self.layout.removeWidget(self.cell)
                        self.cell.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Medium_lvl':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.list_index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
            self.med_index = 0
            self.O_combinations = []
            self.X_combinations = []
            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.replay_button)
            self.replay_button.hide()

            for row in self.cells:
                for self.cell in row:
                    if self.cell.isVisible():
                        self.layout.removeWidget(self.cell)
                        self.cell.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Hard_lvl':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.winning_combinations = [[2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26],
        
            [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [6, 11, 16, 21, 26],
        
            [2, 8, 14, 20, 26], [6, 10, 14, 18, 22]]

            self.list_index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
            self.hard_index = 0
            self.O_combinations = []
            self.X_combinations = []
            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.replay_button)
            self.replay_button.hide()

            for row in self.cells:
                for self.cell in row:
                    if self.cell.isVisible():
                        self.layout.removeWidget(self.cell)
                        self.cell.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Statistic':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.bot_statistic_button)
            self.bot_statistic_button.hide()
            self.layout.removeWidget(self.human_statistic_button)
            self.human_statistic_button.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

        if self.now_page == 'Statistic_Bot':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.null_statistic_button.setEnabled(True)
            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.mod_label)
            self.mod_label.hide()
            self.layout.removeWidget(self.win_label)
            self.win_label.hide()
            self.layout.removeWidget(self.lose_label)
            self.lose_label.hide()
            self.layout.removeWidget(self.draw_label)
            self.draw_label.hide()
            self.layout.removeWidget(self.ez_mod_label)
            self.ez_mod_label.hide()
            self.layout.removeWidget(self.med_mod_label)
            self.med_mod_label.hide()
            self.layout.removeWidget(self.hard_mod_label)
            self.hard_mod_label.hide()
            self.layout.removeWidget(self.ez_win_statistic)
            self.ez_win_statistic.hide()
            self.layout.removeWidget(self.ez_lose_statistic)
            self.ez_lose_statistic.hide()
            self.layout.removeWidget(self.ez_draw_statistic)
            self.ez_draw_statistic.hide()
            self.layout.removeWidget(self.med_win_statistic)
            self.med_win_statistic.hide()
            self.layout.removeWidget(self.med_lose_statistic)
            self.med_lose_statistic.hide()
            self.layout.removeWidget(self.med_draw_statistic)
            self.med_draw_statistic.hide()
            self.layout.removeWidget(self.hard_win_statistic)
            self.hard_win_statistic.hide()
            self.layout.removeWidget(self.hard_lose_statistic)
            self.hard_lose_statistic.hide()
            self.layout.removeWidget(self.hard_draw_statistic)
            self.hard_draw_statistic.hide()
            self.layout.removeWidget(self.null_statistic_button)
            self.null_statistic_button.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()
        
        if self.now_page == 'Statistic_Human':

            self.layout.removeWidget(self.spacer)
            self.spacer.hide()
            self.layout.removeWidget(self.spacer2)
            self.spacer2.hide()

            self.null_statistic_button_human.setEnabled(True)
            self.layout.removeWidget(self.back_to_main_menu_button)
            self.back_to_main_menu_button.hide()
            self.layout.removeWidget(self.word_player_label)
            self.word_player_label.hide()
            self.layout.removeWidget(self.win_label)
            self.win_label.hide()
            self.layout.removeWidget(self.lose_label)
            self.lose_label.hide()
            self.layout.removeWidget(self.draw_label)
            self.draw_label.hide()
            self.layout.removeWidget(self.X_player_label)
            self.X_player_label.hide()
            self.layout.removeWidget(self.O_player_label)
            self.O_player_label.hide()
            self.layout.removeWidget(self.null_statistic_button)
            self.null_statistic_button.hide()
            self.layout.removeWidget(self.O_player_statistic)
            self.O_player_statistic.hide()
            self.layout.removeWidget(self.X_player_statistic)
            self.X_player_statistic.hide()
            self.layout.removeWidget(self.draw_player_statistic)
            self.draw_player_statistic.hide()
            self.layout.removeWidget(self.draw_player_statistic2)
            self.draw_player_statistic2.hide()
            self.layout.removeWidget(self.null_statistic_button_human)
            self.null_statistic_button_human.hide()

            self.play_button.show()
            self.settings_button.show()
            self.statistic_button.show()
            self.quit_button.show()
            self.spacer.show()

    def vs_human_button_clicked(self):
        self.now_page = 'Vs_human'
        self.gamemod = 'humanmod'
    
        self.layout.removeWidget(self.vs_bot_button)
        self.vs_bot_button.hide()
        self.layout.removeWidget(self.vs_human_button)
        self.vs_human_button.hide()
        self.layout.removeWidget(self.trackplay_button)
        self.trackplay_button.hide()
        row = 1
        col = 1
        self.current_symbol = 'X'
        for row in range(1, 6):
            cell_row = []  
            for col in range(1, 6):
                cell_button = CellButton(row, col)
                cell_button.clicked.connect(self.cell_clicked)
                self.layout.addWidget(cell_button, row, col)
                cell_row.append(cell_button)
            self.cells.append(cell_row)

        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 0, 1)
        self.layout.addWidget(self.spacer, 0, 7)
        self.layout.addWidget(self.replay_button, 7, 0)
        self.replay_button.show()

    def cell_clicked(self):

        self.button = self.sender()
        index = self.layout.indexOf(self.button)

        if self.gamemod == "humanmod":
            if self.current_symbol == "X":
                self.button.setText("X")
                index = self.layout.indexOf(self.button)
                self.X_combinations.append(index)
                self.button.setEnabled(False)
                self.current_symbol = "O"
                winner = self.check_winner()
                if winner == 'X':
                    self.message_dialog("Игрок X победил. Хотите начать заново?")
                
                winner = self.check_winner()
                if winner == "draw":
                    self.message_dialog("Ничья. Хотите начать заново?")

            elif self.current_symbol == "O":
                
                self.button.setText("O")
                index = self.layout.indexOf(self.button)
                self.O_combinations.append(index)
                self.button.setEnabled(False)

                self.current_symbol = "X"

                self.button.setStyleSheet("font-size: 100px;"
                                    "background:white;"
                                    "color:blue;"
                                    "text-align: center;"
                                    "border:none"
                                    )
                winner = self.check_winner()
                if winner == 'O':
                    self.message_dialog("Игрок O победил. Хотите начать заново?")

                winner = self.check_winner()
                if winner == "draw":
                    self.message_dialog("Ничья. Хотите начать заново?")
            
        if self.gamemod == "easygamemod":
            if self.current_symbol == "X":
                self.button.setText("X")
                index = self.layout.indexOf(self.button)
                self.X_combinations.append(index)
                self.button.setEnabled(False)
                self.current_symbol = "O"
                self.list_index.remove(index)
            winner = self.check_winner()
            if winner == "X":
                    self.message_dialog("Игрок X победил. Хотите начать заново?")
            if len(self.X_combinations) != 13 and winner!="X":
                self.bot.make_ez_ai_move(self.current_symbol, self.X_combinations, self.list_index, self.layout, self.index, self.O_combinations, self.random_index)
                self.current_symbol = 'X'
                winner = self.check_winner()
                
            if winner == 'O':
                    self.message_dialog("Игрок O победил. Хотите начать заново?")

            if winner == "draw":
                self.message_dialog("Ничья. Хотите начать заново?")

            winner = self.check_winner()
            if winner == "X":
                    self.message_dialog("Игрок X победил. Хотите начать заново?")

        if self.gamemod == "mediumgamemod":
            if self.current_symbol == "X":
                self.button.setText("X")
                self.index = self.layout.indexOf(self.button)
                self.X_combinations.append(self.index)
                self.button.setEnabled(False)
                self.current_symbol = "O"
                self.list_index.remove(self.index)
            winner = self.check_winner()
            if winner == "X":
                self.message_dialog("Игрок X победил. Хотите начать заново?")
            if len(self.X_combinations) != 13 and winner!="X":
                self.bot.make_med_ai_move(self.current_symbol, self.X_combinations, self.list_index, self.layout, self.med_index, self.index, self.O_combinations, self.def_counter)
                self.current_symbol = 'X'
                self.def_counter = 1
                winner = self.check_winner()
                if winner == 'O':
                    self.message_dialog("Игрок O победил. Хотите начать заново?")

            winner = self.check_winner()
            if winner == "draw":
                self.message_dialog("Ничья. Хотите начать заново?")

            winner = self.check_winner()
            if winner == "X":
                    self.message_dialog("Игрок X победил. Хотите начать заново?")
        
        if self.gamemod == "hardgamemod":
            if self.current_symbol == "X":
                self.button.setText("X")
                self.index = self.layout.indexOf(self.button)
                self.X_combinations.append(self.index)
                self.button.setEnabled(False)
                self.current_symbol = "O"
                self.list_index.remove(self.index)
            winner = self.check_winner()
            if winner == "X":
                self.message_dialog("Игрок X победил. Хотите начать заново?")
            if len(self.X_combinations) != 13 and winner!="X":
                self.bot.make_hard_ai_move(self.X_combinations, self.list_index, self.layout, self.index, self.O_combinations, self.hard_index, self.winning_combinations, self.trywinlist)
                self.current_symbol = 'X'
                winner = self.check_winner()
                if winner == 'O':
                    self.message_dialog("Игрок O победил. Хотите начать заново?")

            winner = self.check_winner()
            if winner == "draw":
                self.message_dialog("Ничья. Хотите начать заново?")

            winner = self.check_winner()
            if winner == "X":
                    self.message_dialog("Игрок X победил. Хотите начать заново?")
            
    def easylvl_button_clicked(self):
        self.gamemod = 'easygamemod'
        self.now_page = 'Easy_lvl'
        self.layout.removeWidget(self.trackplay_button)
        self.trackplay_button.hide()
        self.layout.removeWidget(self.easylvl_button)
        self.easylvl_button.hide()
        self.layout.removeWidget(self.mediumlvl_button)
        self.mediumlvl_button.hide()
        self.layout.removeWidget(self.hardlvl_button)
        self.hardlvl_button.hide()

        row = 1
        col = 1
        self.current_symbol = 'X'

        for row in range(1, 6):
            cell_row = []  
            for col in range(1, 6):
                cell_button = CellButton(row, col)
                cell_button.clicked.connect(self.cell_clicked)
                self.layout.addWidget(cell_button, row, col)
                cell_row.append(cell_button)
            self.cells.append(cell_row)

        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 0, 1)
        self.layout.addWidget(self.spacer, 0, 7)
        self.layout.addWidget(self.replay_button, 7, 0)
        self.replay_button.show()

    def mediumlvl_button_clicked(self):
        self.gamemod = 'mediumgamemod'
        self.now_page = 'Medium_lvl'
        self.layout.removeWidget(self.trackplay_button)
        self.trackplay_button.hide()
        self.layout.removeWidget(self.easylvl_button)
        self.easylvl_button.hide()
        self.layout.removeWidget(self.mediumlvl_button)
        self.mediumlvl_button.hide()
        self.layout.removeWidget(self.hardlvl_button)
        self.hardlvl_button.hide()

        row = 1
        col = 1
        self.current_symbol = 'X'
        self.def_counter = 0

        for row in range(1, 6):
            cell_row = []  
            for col in range(1, 6):
                cell_button = CellButton(row, col)
                cell_button.clicked.connect(self.cell_clicked)
                self.layout.addWidget(cell_button, row, col)
                cell_row.append(cell_button)
            self.cells.append(cell_row)

        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 0, 1)
        self.layout.addWidget(self.spacer, 0, 7)
        self.layout.addWidget(self.replay_button, 7, 0)
        self.replay_button.show()

    def hardlvl_button_clicked(self):
        self.gamemod = 'hardgamemod'
        self.now_page = 'Hard_lvl'
        self.layout.removeWidget(self.trackplay_button)
        self.trackplay_button.hide()
        self.layout.removeWidget(self.easylvl_button)
        self.easylvl_button.hide()
        self.layout.removeWidget(self.mediumlvl_button)
        self.mediumlvl_button.hide()
        self.layout.removeWidget(self.hardlvl_button)
        self.hardlvl_button.hide()

        row = 1
        col = 1
        self.current_symbol = 'X'

        for row in range(1, 6):
            cell_row = []  
            for col in range(1, 6):
                cell_button = CellButton(row, col)
                cell_button.clicked.connect(self.cell_clicked)
                self.layout.addWidget(cell_button, row, col)
                cell_row.append(cell_button)
            self.cells.append(cell_row)

        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 0, 1)
        self.layout.addWidget(self.spacer, 0, 7)
        self.layout.addWidget(self.replay_button, 7, 0)
        self.replay_button.show()

    def replay_button_clicked(self):

        self.winning_combinations = [
            [2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26],
        
            [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [6, 11, 16, 21, 26],
        
            [2, 8, 14, 20, 26], [6, 10, 14, 18, 22]
        ]
        self.O_combinations = []
        self.X_combinations = []
        self.current_symbol = "X"
        self.def_counter = 0
        self.med_counter = 0

        for row in self.cells:
                for self.cell in row:
                    if self.cell.isVisible():
                        self.layout.removeWidget(self.cell)
                        self.cell.hide()

        self.layout.removeWidget(self.replay_button)

        for row in range(1, 6):
            cell_row = []
            for col in range(1, 6):
                cell_button = CellButton(row, col)
                cell_button.clicked.connect(self.cell_clicked)
                self.layout.addWidget(cell_button, row, col)
                cell_row.append(cell_button)
            self.cells.append(cell_row)

        self.layout.addWidget(self.replay_button, 7, 0)
        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 0, 1)
        self.layout.addWidget(self.spacer, 0, 7)
        self.list_index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

            
    
    def message_dialog(self, message):

        message_box = QMessageBox(self)
        message_box.setWindowTitle("Игра окончена")
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        ret = message_box.exec()

        if ret == QMessageBox.StandardButton.Yes:
            self.replay_button_clicked()
        else:
            self.back_to_main_menu_button_clicked()

    def check_winner(self):

        winning_combinations = [
            [2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26],
        
            [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [6, 11, 16, 21, 26],
        
            [2, 8, 14, 20, 26], [6, 10, 14, 18, 22]
        ]

        if self.gamemod == "easygamemod":
            for combo in winning_combinations:
                if all(index in self.X_combinations for index in combo):
                    self.increase_variable('const_ez_win',1)
                    self.ez_win_statistic.setText(str(self.ez_win_statistic_value))
                    return "X"
                if all(index in self.O_combinations for index in combo):
                    self.increase_variable('const_ez_lose',1)
                    self.ez_lose_statistic.setText(str(self.ez_lose_statistic_value))
                    return "O"
            if len(self.O_combinations) + len(self.X_combinations) == 25:
                self.increase_variable('const_ez_draw', 0.5)
                self.ez_draw_statistic.setText(str(self.ez_draw_statistic_value))
                return "draw"
            
        if self.gamemod == "humanmod":

            for combo in winning_combinations:
                if all(index in self.X_combinations for index in combo):
                    self.increase_variable('const_vs_player_X', 1)
                    return "X"  
                if all(index in self.O_combinations for index in combo):
                    self.increase_variable('const_vs_player_O', 1)
                    return "O"
            if len(self.O_combinations) + len(self.X_combinations) == 25:
                self.increase_variable('const_vs_player_draw', 0.5)
                return "draw"
            
        if self.gamemod == "mediumgamemod":
            for combo in winning_combinations:
                if all(index in self.X_combinations for index in combo):
                    self.increase_variable('const_med_win', 1)
                    self.med_win_statistic.setText(str(self.med_win_statistic_value))
                    return "X"
                if all(index in self.O_combinations for index in combo):
                    self.increase_variable('const_med_lose', 1)
                    self.med_lose_statistic.setText(str(self.med_lose_statistic_value))
                    return "O"
            if len(self.O_combinations) + len(self.X_combinations) == 25:
                self.increase_variable('const_med_draw', 0.5)
                self.med_draw_statistic.setText(str(self.med_draw_statistic_value))
                return "draw"
            
        if self.gamemod == "hardgamemod":
            for combo in winning_combinations:
                if all(index in self.X_combinations for index in combo):
                    self.increase_variable('const_hard_win', 1)
                    self.hard_win_statistic.setText(str(self.hard_win_statistic_value))
                    return "X"
                if all(index in self.O_combinations for index in combo):
                    self.increase_variable('const_hard_lose', 1)
                    self.hard_lose_statistic.setText(str(self.hard_lose_statistic_value))
                    return "O"
            if len(self.O_combinations) + len(self.X_combinations) == 25:
                self.increase_variable('const_hard_draw', 0.5)
                self.med_draw_statistic.setText(str(self.hard_draw_statistic_value))
                return "draw"

    def trackplay_button_clicked(self):
        if self.trackplay_button_feel == False: 
            self.media_player.play()
            self.trackplay_button.setText('▐▐')
            self.trackplay_button_feel = True
            self.trackplay_button.setStyleSheet(
            '''
            background: transparent; 
            border: none;       
            color: black;
            font-size: 40px;
            text-align: center''')
        else:
            self.trackplay_button_feel = False
            self.media_player.stop()
            self.trackplay_button.setText ('▶')
            self.trackplay_button.setStyleSheet('''
            background: transparent;
            border: none;
            color: black;
            font-size: 90px;
            text-align: center''')
    
    def bot_statistic_button_clicked(self):

        self.now_page = 'Statistic_Bot'
        self.layout.removeWidget(self.human_statistic_button)
        self.human_statistic_button.hide()
        self.layout.removeWidget(self.bot_statistic_button)
        self.bot_statistic_button.hide()

        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 5, 1)
        self.layout.addWidget(self.spacer, 1, 5)
        self.layout.addWidget(self.mod_label, 1, 1)
        self.mod_label.show()
        self.layout.addWidget(self.ez_mod_label, 2, 1)
        self.ez_mod_label.show()
        self.layout.addWidget(self.med_mod_label, 3 ,1)
        self.med_mod_label.show()
        self.layout.addWidget(self.hard_mod_label, 4, 1)
        self.hard_mod_label.show()
        self.layout.addWidget(self.win_label  ,1, 2)
        self.win_label.show()
        self.layout.addWidget(self.lose_label ,1, 3)
        self.lose_label.show()
        self.layout.addWidget(self.draw_label, 1, 4)
        self.draw_label.show()
        self.layout.addWidget(self.ez_win_statistic , 2, 2)
        self.ez_win_statistic.show()
        self.layout.addWidget(self.ez_lose_statistic , 2, 3)
        self.ez_lose_statistic.show()
        self.layout.addWidget(self.ez_draw_statistic , 2, 4)
        self.ez_draw_statistic.show()
        self.layout.addWidget(self.med_win_statistic , 3, 2)
        self.med_win_statistic.show()
        self.layout.addWidget(self.med_lose_statistic , 3, 3)
        self.med_lose_statistic.show()
        self.layout.addWidget(self.med_draw_statistic , 3, 4)
        self.med_draw_statistic.show()
        self.layout.addWidget(self.hard_win_statistic , 4, 2)
        self.hard_win_statistic.show()
        self.layout.addWidget(self.hard_lose_statistic , 4, 3)
        self.hard_lose_statistic.show()
        self.layout.addWidget(self.hard_draw_statistic , 4, 4)
        self.hard_draw_statistic.show()
        self.layout.addWidget(self.null_statistic_button, 5, 0)
        self.null_statistic_button.show()

    def human_statistic_button_clicked(self):

        self.now_page = 'Statistic_Human'
        self.layout.removeWidget(self.human_statistic_button)
        self.human_statistic_button.hide()
        self.layout.removeWidget(self.bot_statistic_button)
        self.bot_statistic_button.hide()

        self.layout.addWidget(self.spacer, 0, 0)
        self.layout.addWidget(self.spacer, 5, 1)
        self.layout.addWidget(self.spacer, 1, 4)
        self.layout.addWidget(self.word_player_label, 1, 1)
        self.word_player_label.show()
        self.layout.addWidget(self.X_player_label, 2, 1)
        self.X_player_label.show()
        self.layout.addWidget(self.O_player_label, 3 ,1)
        self.O_player_label.show()
        self.layout.addWidget(self.win_label, 1, 2)
        self.win_label.show()
        self.layout.addWidget(self.draw_label, 1, 3)
        self.draw_label.show()
        self.layout.addWidget(self.X_player_statistic, 2, 2)
        self.X_player_statistic.show()
        self.layout.addWidget(self.draw_player_statistic, 2, 3)
        self.draw_player_statistic.show()
        self.layout.addWidget(self.draw_player_statistic2, 3, 3)
        self.draw_player_statistic2.show()
        self.layout.addWidget(self.O_player_statistic, 3, 2)
        self.O_player_statistic.show()
        self.layout.addWidget(self.null_statistic_button_human, 5, 0)
        self.null_statistic_button_human.show()

    def null_statistic_button_clicked(self):
        
        self.increase_variable("const_ez_win", -(self.ez_win_statistic_value))
        self.increase_variable("const_ez_lose", -(self.ez_lose_statistic_value))
        self.increase_variable("const_ez_draw", -(self.ez_draw_statistic_value))
        self.increase_variable("const_med_win", -(self.med_win_statistic_value))
        self.increase_variable("const_med_lose", -(self.med_lose_statistic_value))
        self.increase_variable("const_med_draw", -(self.med_draw_statistic_value))
        self.increase_variable("const_hard_win", -(self.hard_win_statistic_value))
        self.increase_variable("const_hard_lose", -(self.hard_lose_statistic_value))
        self.increase_variable("const_hard_draw", -(self.hard_draw_statistic_value))

        self.ez_win_statistic_value = self.got_value('const_ez_win')
        self.ez_lose_statistic_value = self.got_value('const_ez_lose')
        self.ez_draw_statistic_value = int(self.got_value('const_ez_draw'))
        self.med_win_statistic_value = self.got_value('const_med_win')
        self.med_lose_statistic_value = self.got_value('const_med_lose')
        self.med_draw_statistic_value = int(self.got_value('const_med_draw'))
        self.hard_win_statistic_value = self.got_value('const_hard_win')
        self.hard_lose_statistic_value = self.got_value('const_hard_lose')
        self.hard_draw_statistic_value = int(self.got_value('const_hard_draw'))

        self.ez_win_statistic.setText(str(self.ez_win_statistic_value))
        self.ez_lose_statistic.setText(str(self.ez_lose_statistic_value))
        self.ez_draw_statistic.setText(str(self.ez_draw_statistic_value))
        self.med_win_statistic.setText(str(self.med_win_statistic_value))
        self.med_lose_statistic.setText(str(self.med_lose_statistic_value))
        self.med_draw_statistic.setText(str(self.med_draw_statistic_value))
        self.hard_win_statistic.setText(str(self.hard_win_statistic_value))
        self.hard_lose_statistic.setText(str(self.hard_lose_statistic_value))
        self.hard_draw_statistic.setText(str(self.hard_draw_statistic_value))

        self.null_statistic_button.setEnabled(False)
            
    def null_statistic_button_human_clicked(self):
       
        self.increase_variable("const_vs_player_X", -(self.X_statistic_value))
        self.increase_variable("const_vs_player_O", -(self.O_statistic_value))
        self.increase_variable("const_vs_player_draw", -(self.Player_draw_statistic_value))

        self.X_statistic_value = self.got_value('const_vs_player_X')
        self.O_statistic_value = self.got_value('const_vs_player_O')
        self.Player_draw_statistic_value = int(self.got_value('const_vs_player_draw'))

        self.X_player_statistic.setText(str(self.X_statistic_value))
        self.O_player_statistic.setText(str(self.O_statistic_value))
        self.draw_player_statistic.setText(str(self.Player_draw_statistic_value))
        self.draw_player_statistic2.setText(str(self.Player_draw_statistic_value))

        self.null_statistic_button_human.setEnabled(False)

app = QApplication(sys.argv)
menu_window = MainMenu()
menu_window.show()
sys.exit(app.exec())