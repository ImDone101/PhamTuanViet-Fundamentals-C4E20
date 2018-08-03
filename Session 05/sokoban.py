map = {
    "size_x" : 5,
    "size_y" : 5
}

player = {
    "x" : 3,
    "y" : 4
}
boxes = [
    {"x":1, "y":1},
    {"x":2, "y":2},
    {"x":3, "y":3}
]
destination = [
    {"x":2, "y":1},
    {"x":3, "y":2},
    {"x":4, "y":3}
]
play = True
while play:

#print map

    for y in range(map['size_y']):
        for x in range(map['size_x']):
            player_day = False
            if y == player['y'] and x == player['x']:
                player_day = True
            box_day = False
            for box in boxes:
                if y == box['y'] and x == box['x']:
                    box_day = True
            destination_day = False
            for dichDen in destination:
                if y == dichDen['y'] and x == dichDen['x']:
                    destination_day = True
            if player_day:
                print("P", end = " ")
            elif box_day:
                print("B", end = " ")
            elif destination_day:
                print("D", end = " ")
            else:
                print("-", end = ' ')
            
        print()
    #end print
    
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win:
        print("Thang")
        break

    move = input("Nhap nuoc di: ").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "A":
        dx = -1        
    elif move == "S":
        dy = 1
    elif move == "D":
        dx = 1
    else:
        play = False
    
    if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y']: 
        player['x'] += dx
        player['y'] += dy    
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy
