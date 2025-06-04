import random

class MedClass:
        
    def make_med_ai_move(self, current_symbol, X_combinations, list_index, layout, med_index, index, O_combinations, def_counter):
        self.fails = 0
        self.current_symbol = current_symbol
        self.X_combinations = X_combinations
        self.list_index = list_index
        self.layout = layout
        self.O_combinations = O_combinations
        
        # First move logic
        if def_counter == 0:
            self.med_index = 2 if 14 in X_combinations else 14
        else:
            # Define possible moves based on position
            if index in [3, 4, 5, 7, 12, 17, 23, 24, 25]:
                directions = [1, -1, 5, -5]  # horizontal and vertical
            elif index in [11, 16, 21]:
                directions = [5, -5, 1]  # mainly vertical
            elif index in [8, 9, 10, 13, 14, 15, 18, 19, 20]:
                directions = [1, -1, 5, -5, 6, -6, 4, -4]  # all directions
            elif index == 2:
                directions = [1, 5, 6]  # specific corner
            elif index == 6:
                directions = [5, -1, 4]  # specific corner
            elif index == 22:
                directions = [1, -5, -4]  # specific corner
            elif index == 26:
                directions = [-1, -5, -6]  # specific corner
            else:
                directions = []
            
            # Try to find an available move in preferred directions
            for direction in directions:
                target = index + direction
                if target in list_index:
                    self.med_index = target
                    break
            else:
                # If no preferred move found, choose randomly
                self.med_index = random.choice(list_index)
        
        # Make the move
        self.list_index.remove(self.med_index)
        button = self.layout.itemAt(self.med_index).widget()
        button.setText("O")
        self.current_symbol = "X"
        self.O_combinations.append(self.med_index)
        button.setEnabled(False)
        button.setStyleSheet(
            "font-size: 100px;"
            "background:white;"
            "color:blue;"
            "text-align: center;"
            "border:none;"
        )
                
    def make_ez_ai_move(self, current_symbol, X_combinations, list_index, layout, index, O_combinations, random_index):

        self.current_symbol = current_symbol
        self.X_combinations = X_combinations
        self.list_index = list_index
        self.layout = layout
        self.index = index
        self.O_combinations = O_combinations
        self.random_index = random_index

        for i in range(2, 27):
            self.random_index = random.choice(self.list_index)
            button = self.layout.itemAt(self.random_index).widget()
            if self.layout.indexOf(button) == self.random_index:
                self.button = button
                self.list_index.remove(self.random_index)
                break

        if self.button:
            self.button.setText("O")
            self.current_symbol = "X"
            self.O_combinations.append(self.random_index)
            self.button.setEnabled(False)

            self.button.setStyleSheet("font-size: 100px;"
                                  "background:white;"
                                  "color:blue;"
                                  "text-align: center;"
                                  "border:none;"
                                  )
    
    def make_hard_ai_move(self, X_combinations, list_index, layout, index, O_combinations, hard_index, winning_combinations, trywinlist):

        self.winning_combinations = winning_combinations
        self.X_combinations = X_combinations
        self.index = index
        self.trywinlist = trywinlist
        self.O_combinations = O_combinations
        self.list_index = list_index
        self.layout = layout
        self.hard_index = hard_index

        listoflist=[]
        thebiggest=0
        counter = 0
        playercard = True
        gotvalue = 0

        for w in self.winning_combinations:
            gotnew=len(set(self.X_combinations)&set(w))
            if thebiggest<=gotnew:
                thebiggest = gotnew
        for w in self.winning_combinations:
            gotnew=len(set(self.X_combinations)&set(w))
            if thebiggest==gotnew:
                thebiggest = gotnew
                neededlist = w
                counter+=1
                listoflist.append(neededlist)
        if len(listoflist)>1:
            hardlist = listoflist[random.randint(0, counter-1)]
        elif len(listoflist) == 1:
            hardlist = listoflist[0]
        elif len(listoflist) == 0:
            thebiggest = 0
            playercard = False
            for list in self.trywinlist:
                if len(set(list)&set(O_combinations))>thebiggest:
                    thebiggest = len(set(list)&set(O_combinations))
            for list in self.trywinlist:
                if len(set(self.O_combinations)&set(list))==thebiggest and len(self.trywinlist)!=0:
                    for i in list:
                        if i not in self.X_combinations and i not in self.O_combinations:
                            self.hard_index = i
                            gotvalue = 1
                            break
                            
            if gotvalue == 0:
                for i in self.list_index:
                    if i not in self.X_combinations and i not in self.O_combinations:
                        self.hard_index = i
                        
        if playercard == True:                
            for i in range(5):
                if hardlist[i] not in self.X_combinations and hardlist[i] not in self.O_combinations:
                    self.hard_index = hardlist[i]
                    break
            for list in self.winning_combinations:
                for el in list:
                    if el == self.hard_index:
                        self.winning_combinations.remove(list)
                        self.trywinlist.append(list)
                        
        if self.hard_index == 0:
            for i in self.list_index:
                    if i not in self.X_combinations and i not in self.O_combinations:
                        self.hard_index = i

        self.button = self.layout.itemAt(self.hard_index).widget() 
        self.button.setText("O")
        self.current_symbol = "X"
        self.O_combinations.append(self.hard_index)
        self.button.setEnabled(False)

        self.button.setStyleSheet("font-size: 100px;"
                                                "background:white;"
                                                "color:blue;"
                                                "text-align: center;"
                                                "border:none;"
                                                )