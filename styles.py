button_style = """
            QPushButton {
                background-color: rgba(255, 255, 255, 150);
                color:#000;
                font-size: 80px;
                padding: 10px; 
                border: none; 
                border-radius: 60px;
                margin-bottom: 30px;
                border: 2px solid rgba(0, 150, 255, 200);
            }

            QPushButton#MenuButton{
            background: transparent; 
            border: none;       
            color: black;
            font-size: 40px;
            text-align: left;
            }

            QPushButton#MenuButton:hover {
                color: gray;
            }

            QPushButton#ReplayButton:hover {
                color: gray;
            }
            
            QPushButton#ReplayButton {
            background: transparent; 
            border: none;       
            color: black;
            font-size: 50px;
            text-align: center;
            }

            QPushButton:hover {
                color: gray;
                font-size:77px;
            }

            QPushButton#Cell{
            background: black; 
            border: none;   
            color: black;
            font-size: 40px;
            max-width: 50px;
            max-heigth: 50px;
            }

            QPushButton#TrackButton{
            background: transparent; 
            border: none;       
            color: black;
            font-size: 90px;
            text-align: center;
            }
            QPushButton#TrackButton:hover{
            color:gray
            }

            QPushButton#NullButton{
            background: transparent; 
            border: none;       
            color: black;
            font-size: 40px;
            text-align: left;
            }
            QPushButton#NullButton:hover{
            color:gray
            }
            
            QPushButton#SettingsButton{

            background-color: rgba(255, 255, 255, 150);
            border: 1px;
            border-radius: 5px;       
            color: black;
            font-size: 40px;
            }
            QPushButton#SettingsButton:hover{
            color:gray
            }
            
            QPushButton#SettingsUseButton{
            background-color: rgba(255, 255, 255, 150);
            border: 2px;
            border-radius:10px;       
            color: black;
            margin-top:0px;
            margin-botom:40px;
            }
        """

statistic_label_style = '''
            QLabel {
                color: black;
                font-size: 40px;
                padding: 40px; 
                margin-bottom: 0px;
                margin-left: 0px;
                border
                text-align: center;
                border: 2px solid black; 
                border-radius: 5px;
                background-color:white;
}
            QLabel#WinLabel {
                color: green;
                font-size: 40px;
                padding: 40px; 
                margin-bottom: 0px;
                margin-left: 0px;
                border
                text-align: center;
                border: 2px solid black; 
                border-radius: 5px;
            }
            QLabel#LoseLabel{
            color: red;
                font-size: 40px;
                padding: 40px; 
                margin-bottom: 0px;
                margin-left: 0px;
                border
                text-align: center;
                border: 2px solid black; 
                border-radius: 5px;
            }

            QLabel#DrawLabel{
            color: gray;
                font-size: 40px;
                padding: 40px; 
                margin-bottom: 0px;
                margin-left: 0px;
                border
                text-align: center;
                border: 2px solid black; 
                border-radius: 5px;
            }

            QLabel#DrawPlayerLabel{
                color: gray;
                font-size: 40px;
                padding: 40px; 
                margin-bottom: 0px;
                margin-left: 0px;
                border
                text-align: center;
                border: 2px solid black; 
                border-radius: 5px;
            }
'''
progressbar_style = '''
QProgressBar{

    border:1px solid #5c5c5c;
    border-radius: 12px;
    background: #e0e0e0;  
}
    QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1E90FF, stop:1 #6A5ACD);
    border-radius: 12px; 
}
'''
loading_label_style = '''
    QLabel{
    font-size: 70px;
    font-weight: bold;
    color: #003153;
    background-color: transparent;
    padding: 10px;
    margin-bottom: 10px;
}
'''

settings_label_style = '''
QLabel{
    font-size:70px;
    font-weight: bold;
    color: Black;
}
'''

night_button_style = """

            QPushButton {
                background-color:none;
                color:white;
                font-size: 80px;
                padding: 10px;  
                border-radius: 60px;
                margin-bottom: 30px;
                border:1px solid white;
            }

            QPushButton#MenuButton{
            background: transparent; 
            border: none;       
            color: white;
            font-size: 40px;
            text-align: left;
            }

            QPushButton#MenuButton:hover {
                color: gray;
            }

            QPushButton#ReplayButton:hover {
                color: gray;
            }
            
            QPushButton#ReplayButton {
            background: transparent; 
            border: none;       
            color: white;
            font-size: 50px;
            text-align: center;
            }

            QPushButton:hover {
                color: gray;
                font-size:77px;
            }

            QPushButton#Cell{
            background: black; 
            border: none;   
            color: black;
            font-size: 40px;
            max-width: 50px;
            max-heigth: 50px;
            }

            QPushButton#TrackButton{
            background: transparent; 
            border: none;       
            color: white;
            font-size: 90px;
            text-align: center;
            }
            QPushButton#TrackButton:hover{
            color:gray
            }

            QPushButton#NullButton{
            background: transparent; 
            border: none;       
            color: white;
            font-size: 40px;
            text-align: left;
            }
            QPushButton#NullButton:hover{
            color:gray
            }
            
            QPushButton#SettingsButton{
            border:1px solid white;
            border-radius: 5px;       
            color: white;
            font-size: 40px;
            }
            QPushButton#SettingsButton:hover{
            color:gray
            }
            
            QPushButton#SettingsUseButton{
            border:1px solid white;
            border-radius:10px;    
            color: white;
            margin-top:0px;
            margin-botom:40px;
            }
        """

night_loading_label_style = '''
    QLabel{
    font-size: 70px;
    font-weight: bold;
    color: #d8bfd8;
    background-color: transparent;
    padding: 10px;
}
'''