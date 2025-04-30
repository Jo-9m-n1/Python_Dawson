class Menu:
    def __init__(self):
        self.options = []
    def addOption(self, option: str) -> None:
        self.options.append(option)
    def getInput(self):
        for i in range(len(self.options)):
            print(f'{i+1}: {self.options[i]}')
        Done = True
        while Done == True: 
            try:
                choice = int(input('Enter your choice: '))
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            if 1 <= choice <= len(self.options):
                Done = False
            return str(choice) 
        
M = Menu()
M.addOption('Drink')
M.addOption('Side dish')
M.addOption('Main dish')
M.addOption('Dessert')
M.addOption('Quit')
print(M.getInput())