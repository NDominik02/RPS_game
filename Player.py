class Player:
    def __init__(self, name, health, hand):
        self.name = name
        self.health = health
        self.hand = hand

    def __eq__(self, other):
        return self.hand == other.hand
    
    def __lt__(self, other):
        
        if self.hand == other.hand:
            return False
        
        if self.hand == "rock":
            return other.hand == "paper"
        
        if self.hand == "paper":
            return other.hand == "scissors"
        
        if self.hand == "scissors":
            return other.hand == "rock"
        
        return False
    
    def __gt__(self, other):
        
        if self.hand == other.hand:
            return False 
        
        if self.hand == "rock":
            return other.hand == "scissors"
        
        if self.hand == "paper":
            return other.hand == "rock"
        
        if self.hand == "scissors":
            return other.hand == "paper"
        
        return False