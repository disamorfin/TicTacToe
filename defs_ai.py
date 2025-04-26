import random

class MedClass:
        
    def make_med_ai_move(self, current_symbol, X_combinations,list_index, layout, med_index, index, O_combinations, def_counter):
                 
            self.fails = 0
            self.index = index
            self.list_index = list_index
            self.current_symbol = current_symbol
            self.X_combinations = X_combinations
            self.layout = layout
            self.med_index = med_index
            self.O_combinations = O_combinations
            self.def_counter = def_counter

            if self.def_counter == 0 and 14 not in X_combinations:
                self.med_index = 14
                self.button = self.layout.itemAt(self.med_index).widget()
                self.button.setText("O")
                self.current_symbol = "X"
                self.O_combinations.append(self.med_index)
                self.button.setEnabled(False)
                self.button.setStyleSheet("font-size: 100px;"
                                            "background:white;"
                                            "color:blue;"
                                            "text-align: center;"
                                            "border:none;"
                                            )
                self.list_index.remove(self.med_index)
            
            elif self.def_counter == 0 and 14 in X_combinations:
                
                self.med_index = 2
                self.button = self.layout.itemAt(self.med_index).widget() 
                self.button.setText("O")
                self.current_symbol = "X"
                self.O_combinations.append(self.med_index)
                self.button.setEnabled(False)
                self.button.setStyleSheet("font-size: 100px;"
                                            "background:white;"
                                            "color:blue;"
                                            "text-align: center;"
                                            "border:none;"
                                            )
                self.list_index.remove(self.med_index)

            else:    
                if self.index == 3 or self.index == 4 or self.index == 5:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index + 1 == i:
                                    self.med_index = self.index + 1
                                    break
                                elif self.index + 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index + 5

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index + 5 == i:
                                    self.med_index = self.index + 5
                                    break

                                elif self.index + 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.med_index+1 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.med_index+1 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index - 1 == i:
                                    self.med_index = self.index - 1
                                    break
                                elif self.index - 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.index+1 !=i:
                                                self.med_index = self.index + 5
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index+5 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)

                if self.index == 11 or self.index == 16 or self.index == 21:
                        self.med_index = random.randint(1,3)

                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index - 1 == i:
                                    self.med_index = self.index - 1
                                    break
                                elif self.index - 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index + 5 == i:
                                    self.med_index = self.index + 5
                                    break
                                elif self.index + 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index - 5 == i:
                                    self.med_index = self.index - 5
                                    break
                                
                                elif self.index - 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.index+5 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)

                if self.index == 7 or self.index == 12 or self.index == 17:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index + 1 == i:
                                    self.med_index = self.index + 1
                                    break

                                elif self.index + 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index+5 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index + 5 == i:
                                    self.med_index = self.index + 5
                                    break

                                elif self.index + 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.med_index+1 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index - 5 == i:
                                    self.med_index = self.index - 5
                                    break
                                elif self.index - 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.index+1 != i:
                                                self.med_index = self.index + 5
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index+5 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)

                if self.index == 23 or self.index == 24 or self.index == 25:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index): 
                                if self.index + 1 == i:
                                    self.med_index = self.index + 1
                                    break

                                elif self.index + 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index - 5 == i:
                                    self.med_index = self.index - 5
                                    break
                                elif self.index - 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index + 1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.med_index+1 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break

                                            else:
                                                self.fails+=1

                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index - 1 == i:
                                    self.med_index = self.index - 1
                                    break
                                elif self.index - 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.index+5 !=i:
                                                self.med_index = self.index - 1
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    elif self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)

                if self.index == 8 or self.index == 9 or self.index == 10 or self.index == 13 or self.index == 14 or self.index == 15 or self.index == 18 or self.index == 19 or self.index == 20:
                        self.med_index = random.randint(1,4)

                        if self.med_index == 1:
                            for i in (self.list_index):
                                if self.index + 1 == i:
                                    self.med_index = self.index + 1
                                    break
                                else:
                                    pass

                                if self.index + 1 != i:
                                    self.med_index = random.randint(1,3)
                                    if self.med_index == 1:

                                        for i in (self.list_index):
                                            if self.index + 5 == i:
                                                self.med_index = self.index + 5
                                                break
                                            elif self.index + 5 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index-1 == i:
                                                            self.med_index = self.index-1
                                                            break
                                                        elif self.med_index-1 !=i:
                                                            self.med_index = self.index - 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index - 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)


                                    if self.med_index == 2:

                                        for i in (self.list_index):
                                            if self.index + 5 == i:
                                                self.med_index = self.index + 5
                                                break
                                            elif self.index + 5 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index-1 == i:
                                                            self.med_index = self.index-1
                                                            break
                                                        elif self.med_index-1 !=i:
                                                            self.med_index = self.index - 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index - 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1
                                            
                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)
                                                

                                    if self.med_index == 3:

                                        for i in (self.list_index):
                                            if self.index - 1 == i:
                                                self.med_index = self.index - 1
                                                break
                                            elif self.index - 1 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.index+5 == i:
                                                            self.med_index = self.index+5
                                                            break
                                                        elif self.index+5 !=i:
                                                            self.med_index = self.index - 5
                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index + 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)

                        if self.med_index == 2:
                            for i in (self.list_index):
                                if self.index + 5 == i:
                                    self.med_index = self.index + 5
                                    break
                                else:
                                    pass

                                if self.index + 1 != i:
                                    self.med_index = random.randint(1,3)
                                    if self.med_index == 1:

                                        for i in (self.list_index):
                                            if self.index + 1 == i:
                                                self.med_index = self.index + 1
                                                break
                                            elif self.index + 1 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index-1 == i: 
                                                            self.med_index = self.index - 1
                                                            break
                                                        elif self.med_index-1 !=i:
                                                            self.med_index = self.index - 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1
                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index - 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)


                                    if self.med_index == 2:

                                        for i in (self.list_index):
                                            if self.index - 1 == i:
                                                self.med_index = self.index - 1
                                                break
                                            elif self.index - 1 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index+1 == i:
                                                            self.med_index = self.index+1
                                                            break
                                                        elif self.med_index+1 !=i:
                                                            self.med_index = self.index - 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index + 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1
                                            
                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)
                                                

                                    if self.med_index == 3:

                                        for i in (self.list_index):
                                            if self.index - 5 == i:
                                                self.med_index = self.index - 5
                                                break
                                            elif self.index - 5 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.index+1 == i:
                                                            self.med_index = self.index+1
                                                            break
                                                        elif self.index+1 !=i:
                                                            self.med_index = self.index - 1
                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-1 == i:
                                                            self.med_index = self.index-1
                                                            break
                                                        elif self.med_index-1 !=i:
                                                            self.med_index = self.index + 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)

                        if self.med_index == 3:
                            for i in (self.list_index):
                                if self.index - 1 == i:
                                    self.med_index = self.index - 1
                                    break
                                else:
                                    pass

                                if self.index - 1 != i:
                                    self.med_index = random.randint(1,3)
                                    if self.med_index == 1:

                                        for i in (self.list_index):
                                            if self.index + 1 == i:
                                                self.med_index = self.index + 1
                                                break
                                            elif self.index + 1 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index+5 == i:
                                                            self.med_index = self.index+5
                                                            break
                                                        elif self.med_index+5 !=i:
                                                            self.med_index = self.index - 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index + 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1
                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)


                                    if self.med_index == 2:

                                        for i in (self.list_index):
                                            if self.index + 5 == i:
                                                self.med_index = self.index + 5
                                                break
                                            elif self.index + 5 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index+1 == i:
                                                            self.med_index = self.index+1
                                                            break
                                                        elif self.med_index+1 !=i:
                                                            self.med_index = self.index - 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-5 == i:
                                                            self.med_index = self.index-5
                                                            break
                                                        elif self.med_index-5 !=i:
                                                            self.med_index = self.index + 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1
                                            
                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)
                                                

                                    if self.med_index == 3:

                                        for i in (self.list_index):
                                            if self.index - 5 == i:
                                                self.med_index = self.index - 5
                                                break
                                            elif self.index - 5 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.index+1 == i:
                                                            self.med_index = self.index+1
                                                            break
                                                        elif self.index+1 !=i:
                                                            self.med_index = self.index + 5
                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index+5 == i:
                                                            self.med_index = self.index+5
                                                            break
                                                        elif self.med_index+5 !=i:
                                                            self.med_index = self.index + 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)

                        if self.med_index == 4:
                            for i in (self.list_index):
                                if self.index - 5 == i:
                                    self.med_index = self.index - 5
                                    break
                                else:
                                    pass

                                if self.index - 5 != i:
                                    self.med_index = random.randint(1,3)
                                    if self.med_index == 1:

                                        for i in (self.list_index):
                                            if self.index + 1 == i:
                                                self.med_index = self.index + 1
                                                break
                                            elif self.index + 1 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index+5 == i:
                                                            self.med_index = self.index+5
                                                            break
                                                        elif self.med_index+5 !=i:
                                                            self.med_index = self.index - 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-1 == i:
                                                            self.med_index = self.index-1
                                                            break
                                                        elif self.med_index-1 !=i:
                                                            self.med_index = self.index + 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)


                                    if self.med_index == 2:

                                        for i in (self.list_index):
                                            if self.index + 5 == i:
                                                self.med_index = self.index + 5
                                                break
                                            elif self.index + 5 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.med_index+1 == i:
                                                            self.med_index = self.index+1
                                                            break
                                                        elif self.med_index+1 !=i:
                                                            self.med_index = self.index - 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index-1 == i:
                                                            self.med_index = self.index-1
                                                            break
                                                        elif self.med_index-1 !=i:
                                                            self.med_index = self.index + 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1
                                            
                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)
                                                

                                    if self.med_index == 3:

                                        for i in (self.list_index):
                                            if self.index - 1 == i:
                                                self.med_index = self.index - 1
                                                break
                                            elif self.index - 1 != i:
                                                self.med_index = random.randint(1,2)
                                                if self.med_index == 1:
                                                    for i in (self.list_index):
                                                        if self.index+1 == i:
                                                            self.med_index = self.index+1
                                                            break
                                                        elif self.index+1 !=i:
                                                            self.med_index = self.index + 5

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                                elif self.med_index == 2:
                                                    for i in (self.list_index):
                                                        if self.med_index+5 == i:
                                                            self.med_index = self.index+5
                                                            break
                                                        elif self.med_index+5 !=i:
                                                            self.med_index = self.index + 1

                                                    for i in (self.list_index):
                                                        if self.med_index == i:
                                                            self.med_index = self.med_index
                                                            self.fails = 0
                                                            break
                                                        else:
                                                            self.fails+=1

                                        if self.fails == 0:
                                            self.med_index = self.med_index
                                        else:
                                            self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)
                            
                if self.index == 2:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index + 1 == i:
                                    self.med_index = self.index + 1
                                    break

                                elif self.index + 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index + 6

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+6 == i:
                                                self.med_index = self.index+6
                                                break
                                            elif self.med_index+6 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index + 5 == i:
                                    self.med_index = self.index + 5
                                    break

                                elif self.index + 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.med_index+1 !=i:
                                                self.med_index = self.index + 6

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+6 == i:
                                                self.med_index = self.index+6
                                                break
                                            elif self.med_index+6 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index + 6 == i:
                                    self.med_index = self.index + 6
                                    break
                                elif self.index + 6 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.index+1 !=i:
                                                self.med_index = self.index + 5
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index+5 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)
                    
                if self.index == 6:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index + 5 == i:
                                    self.med_index = self.index + 5
                                    break
                                elif self.index + 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index + 4

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+4 == i:
                                                self.med_index = self.index+4
                                                break
                                            elif self.med_index+4 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index - 1 == i:
                                    self.med_index = self.index - 1
                                    break
                                elif self.index - 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.med_index+5 !=i:
                                                self.med_index = self.index + 4

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index+4 == i:
                                                self.med_index = self.index+4
                                                break
                                            elif self.med_index+4 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index + 4 == i:
                                    self.med_index = self.index + 4
                                    break
                                elif self.index + 4 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+5 == i:
                                                self.med_index = self.index+5
                                                break
                                            elif self.index+5 !=i:
                                                self.med_index = self.index - 1
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index + 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)
                    
                if self.index == 22:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index + 1 == i:
                                    self.med_index = self.index + 1
                                    break
                                elif self.index + 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 != i:
                                                self.med_index = self.index - 4

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-4 == i:
                                                self.med_index = self.index-4
                                                break
                                            elif self.med_index-4 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index - 5 == i:
                                    self.med_index = self.index - 5
                                    break
                                elif self.index - 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.med_index+1 !=i:
                                                self.med_index = self.index - 4

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-4 == i:
                                                self.med_index = self.index-4
                                                break
                                            elif self.med_index-4 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index - 4 == i:
                                    self.med_index = self.index - 4
                                    break
                                elif self.index - 4 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index+1 == i:
                                                self.med_index = self.index+1
                                                break
                                            elif self.index+1 !=i:
                                                self.med_index = self.index - 5
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index + 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)
                    
                if self.index == 26:
                        self.med_index = random.randint(1,3)
                        if self.med_index == 1:

                            for i in (self.list_index):
                                if self.index - 1 == i:
                                    self.med_index = self.index - 1
                                    break
                                elif self.index - 1 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 != i:
                                                self.med_index = self.index - 6

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-6 == i:
                                                self.med_index = self.index-6
                                                break
                                            elif self.med_index-6 !=i:
                                                self.med_index = self.index - 5

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)


                        if self.med_index == 2:

                            for i in (self.list_index):
                                if self.index - 5 == i:
                                    self.med_index = self.index - 5
                                    break
                                elif self.index - 5 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.med_index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.med_index-1 !=i:
                                                self.med_index = self.index - 6

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1

                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-6 == i:
                                                self.med_index = self.index-6
                                                break
                                            elif self.med_index-6 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)
                                                

                        if self.med_index == 3:

                            for i in (self.list_index):
                                if self.index - 6 == i:
                                    self.med_index = self.index - 6
                                    break
                                elif self.index - 6 != i:
                                    self.med_index = random.randint(1,2)
                                    if self.med_index == 1:
                                        for i in (self.list_index):
                                            if self.index-1 == i:
                                                self.med_index = self.index-1
                                                break
                                            elif self.index-1 !=i:
                                                self.med_index = self.index - 5
                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                                                
                                    if self.med_index == 2:
                                        for i in (self.list_index):
                                            if self.med_index-5 == i:
                                                self.med_index = self.index-5
                                                break
                                            elif self.med_index-5 !=i:
                                                self.med_index = self.index - 1

                                        for i in (self.list_index):
                                            if self.med_index == i:
                                                self.med_index = self.med_index
                                                self.fails = 0
                                                break
                                            else:
                                                self.fails+=1
                            if self.fails == 0:
                                self.med_index = self.med_index
                            else:
                                self.med_index = random.choice(self.list_index)

                        self.list_index.remove(self.med_index)

                self.button = self.layout.itemAt(self.med_index).widget() 
                self.button.setText("O")
                self.current_symbol = "X"
                self.O_combinations.append(self.med_index)
                self.button.setEnabled(False)

                self.button.setStyleSheet("font-size: 100px;"
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