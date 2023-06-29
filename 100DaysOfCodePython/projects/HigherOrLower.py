import random
logo = """

 _   _ _       _                    
| | | (_)     | |                   
| |_| |_  __ _| |__   ___ _ __      
|  _  | |/ _` | '_ \ / _ \ '__|     
| | | | | (_| | | | |  __/ |        
\_| |_/_|\__, |_| |_|\___|_|        
          __/ |                     
         |___/                      
     ___  _ __                      
    / _ \| '__|                     
   | (_) | |                        
    \___/|_|                        
       _                            
      | |                           
      | |     _____      _____ _ __ 
      | |    / _ \ \ /\ / / _ \ '__|
      | |___| (_) \ V  V /  __/ |   
      \_____/\___/ \_/\_/ \___|_|   
                                                                        
"""
influencers = {
    "Cristiano Ronaldo":439000000,
    "Lionel Messi":449000000,
    "Selena Gomez":406000000,
    "Kylie Jenner":384000000,
    "Dwayne Johnson":372000000,
    "Ariana Grande":363000000,
    "Kim Kardashian":350000000,
    "Beyoncé":303000000,
    "Khloé Kardashian":301000000,
    "Justin Bieber":284000000,
}

def set_opponent():
    random_influencer = random.choice(list(influencers.keys()))
    return random_influencer

def check_answer(a,b,aws):
    pass
    

def game():
    print(logo)
    a = print(set_opponent())
    print('OR')
    b = print(set_opponent())
    aws = input('Who has more followers? Type "A" or "B"')
    check_answer(a,b,aws)

game()


