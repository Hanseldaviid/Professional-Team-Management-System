# Create class Player:
class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
        
# Create class Team:
class Team:
    def __init__(self):
        self.team_name = ""
        self.players = []
        
    # Name of the team:
    def name_team(self):
        self.team_name = input("Insert the name of your team: ")

    # Method add_player
    def add_player(self, player):
        self.players.append(player)
    
    # Method show full players:
    def show_roaster(self):
        print(f" = = \n ROASTER OF: {self.team_name.upper()} = = ")
        for s in self.players:
            print(f"Professional player: {s.name} | Position: {s.position} | Number: {s.number} \n")
        
    # Method total_players:
    def count_players(self):
        amount = len(self.players)
        print(f"Amount: {amount}")
       
        
# Create classes:
      
player1 = Player(" Lionel Messi ", " Striker ", " 10 \n      ")
player2 = Player(" Neymar Jr ", " Second Striker ", " 11 \n  ")
player3 = Player(" Pedri Rodriguez ", " Midfielder ", " 22 \n")
player4 = Player(" Virgil Van Dijk ", " Center Back ", " 4 \n")
player5 = Player(" Lamine Yamal ", " Striker ", " 10 \n      ") 


# Save class team to a variable:
my_team = Team() 

# Call function name of the team: 
my_team.name_team()

# Call the methods in my Team class:
my_team.add_player(player1)  
my_team.add_player(player2)  
my_team.add_player(player3)  
my_team.add_player(player4)
my_team.add_player(player5) 

# Show my players:
my_team.show_roaster()

# Amount of thing in the list:
my_team.count_players()

        
        
        
        
            
            
                
    
        