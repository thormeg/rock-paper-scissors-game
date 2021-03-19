"""ASCII art for Rock Paper Scissors"""
# flake8: noqa
options = """
    Please make your choice:
        [R]ock
        [P]aper
        [S]cissors
"""

# ASCII Text 'Univers' font at https://www.coolgenerator.com/ascii-text-generator
welcome = r'''
I8,        8        ,8I            88                                                              88  
`8b       d8b       d8'            88                                                              88  
 "8,     ,8"8,     ,8"             88                                                              88  
  Y8     8P Y8     8P   ,adPPYba,  88   ,adPPYba,   ,adPPYba,   88,dPYba,,adPYba,    ,adPPYba,     88  
  `8b   d8' `8b   d8'  a8P_____88  88  a8"     ""  a8"     "8a  88P'   "88"    "8a  a8P_____88     88  
   `8a a8'   `8a a8'   8PP"""""""  88  8b          8b       d8  88      88      88  8PP"""""""     ""  
    `8a8'     `8a8'    "8b,   ,aa  88  "8a,   ,aa  "8a,   ,a8"  88      88      88  "8b,   ,aa     aa  
     `8'       `8'      `"Ybbd8"'  88   `"Ybbd8"'   `"YbbdP"'   88      88      88   `"Ybbd8"'     88  
'''

the_end = r'''
888888888888  88                          88888888888                        88     88                 
     88       88                          88                                 88     88                 
     88       88                          88                                 88     88                 
     88       88,dPPYba,    ,adPPYba,     88aaaaa      8b,dPPYba,    ,adPPYb,88     88                 
     88       88P'    "8a  a8P_____88     88"""""      88P'   `"8a  a8"    `Y88     88                 
     88       88       88  8PP"""""""     88           88       88  8b       88     ""                 
     88       88       88  "8b,   ,aa     88           88       88  "8a,   ,d88     aa                 
     88       88       88   `"Ybbd8"'     88888888888  88       88   `"8bbdP"Y8     88       
'''

scissors = """
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
"""
paper = """
            _____..
____..--'''' ._ __.'
              "-..__
            '"--..__";
____        '--...__"";
    `-..__ '"---..._;"
          ''''----
"""

rock = """
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""

win = r'''
8b        d8                           I8,        8        ,8I  88                  88                 
 Y8,    ,8P                            `8b       d8b       d8'  ""                  88                 
  Y8,  ,8P                              "8,     ,8"8,     ,8"                       88                 
   "8aa8"  ,adPPYba,   88       88       Y8     8P Y8     8P    88  8b,dPPYba,      88                 
    `88'  a8"     "8a  88       88       `8b   d8' `8b   d8'    88  88P'   `"8a     88                 
     88   8b       d8  88       88        `8a a8'   `8a a8'     88  88       88     ""                 
     88   "8a,   ,a8"  "8a,   ,a88         `8a8'     `8a8'      88  88       88     aa                 
     88    `"YbbdP"'    `"YbbdP'Y8          `8'       `8'       88  88       88     88   
'''

lose = r'''
8b        d8                           88                                                 88           
 Y8,    ,8P                            88                                                 88           
  Y8,  ,8P                             88                                                 88           
   "8aa8"  ,adPPYba,   88       88     88           ,adPPYba,   ,adPPYba,   ,adPPYba,     88           
    `88'  a8"     "8a  88       88     88          a8"     "8a  I8[    ""  a8P_____88     88           
     88   8b       d8  88       88     88          8b       d8   `"Y8ba,   8PP"""""""     ""           
     88   "8a,   ,a8"  "8a,   ,a88     88          "8a,   ,a8"  aa    ]8I  "8b,   ,aa     aa           
     88    `"YbbdP"'       Draw!       88888888888  `"YbbdP"'   `"YbbdP"'   `"Ybbd8"'     88  
'''

draw = r'''
88888888ba,                                                   88  
88      `"8b                                                  88  
88        `8b                                                 88  
88         88  8b,dPPYba,  ,adPPYYba,  8b      db      d8     88  
88         88  88P'   "Y8  ""     `Y8  `8b    d88b    d8'     88  
88         8P  88          ,adPPPPP88   `8b  d8'`8b  d8'      ""  
88      .a8P   88          88,    ,88    `8bd8'  `8bd8'       aa  
88888888Y"'    88          `"8bbdP"Y8      YP      YP         88  
                                                                  
'''
