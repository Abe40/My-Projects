ab# import necessary modules to build the 2048 game
import random
import copy
grid =[[0]*4 for k in range(4)] # a matrix with all entries zero
# function to draw the grid
def draw_grid():
    large_tile =grid[0][1]
    for row in grid:
        for element in row:
            if large_tile<element:
                large_tile= element
    grid_space = len(str(large_tile))
    for row in grid:
        current_row = "|"
        for element in row:
            if element ==0:
                current_row +="_"*grid_space + "|"
            else:
                current_row += "_" * (grid_space-len(str(element))) + str(element) + "|"
        print(current_row)
# Function to merge a single row or column to left
def merge(row):
    # move all non-zero tiles to left
    def move_tiles(tile):
        sub_grid= []
        for i in range(0,len(tile)):
            if tile[i]!=0:
                sub_grid.append(tile[i])
        if len(sub_grid)<len(tile):
            sub_grid.extend([0]*(len(tile)-len(sub_grid)))
        return sub_grid
    # add tiles together
    def add_tiles(tile):
        for i in range(0,len(tile)-1):
            if tile[i]==tile[i+1]:
                tile[i] = tile[i]*2
                tile[i+1] = 0
        return tile

    sub_grid1 = move_tiles(row)
    sub_grid2= add_tiles(sub_grid1)
    sub_grid3 = move_tiles(sub_grid2)
    return sub_grid3
# function to transpose the grid into the corners
def transpose(current_grid):
    for j in range(4):
        for i in range(j,4):
            if i != j:
                current_grid[j][i],current_grid[i][j]=current_grid[i][j],current_grid[j][i]
    return current_grid
# reverse the order of each row
def reverse(row):
    new =[]
    for i in range (3,-1,-1):
        new.append(row[i])
    return new
# function to merge the grid to the left
def merge_left(current_grid):
    for i in range(4):
        current_grid [i]=merge(current_grid[i])
    return current_grid
# function to merge the grid to the right
def merge_right(current_grid):
    for i in range(4):
        current_grid[i] = reverse(current_grid[i])
        current_grid[i] = merge(current_grid[i])
        current_grid[i] = reverse(current_grid[i])
    return current_grid
# function to merge the grid up
def merge_up(current_grid):
        current_grid=transpose(current_grid)
        current_grid=merge_left(current_grid)
        current_grid=transpose(current_grid)
        return current_grid
# function to merge the grid down
def merge_down(current_grid):
    current_grid= transpose(current_grid)
    current_grid = merge_right(current_grid)
    current_grid = transpose(current_grid)
    return current_grid
# function to generate 2 and 4 in the grid
def generate_value():
    if random.randint(1,8) ==1:
        return 4
    else:
        return 2
# function to generate new 2s and 4s in  each move
def generate_new_value():
    row_value=random.randint(0,3)
    column_value = random.randint(0,3)

    while not grid[row_value][column_value]==0:
        row_value = random.randint(0, 3)
        column_value= random.randint(0, 3)
    grid[row_value][column_value]=generate_value()
# function to check if the player arrive to its goal 2048
def won():
    for row in grid:
        if 2048 in row:
            return True
    return False
# function to check if the player has more moves to play the game
def no_move():
    temp_grid1= copy.deepcopy(grid)
    temp_grid2 = copy.deepcopy(grid)
    temp_grid2= merge_up(temp_grid2)
    if temp_grid2==temp_grid1:
        temp_grid2 =merge_down(temp_grid2)
        if temp_grid2==temp_grid1:
            temp_grid2 =merge_left(temp_grid2)
            if temp_grid2==temp_grid1:
                temp_grid2 =merge_right(temp_grid2)
                if temp_grid2 == temp_grid1:
                    return True
    return False
number_needed = 2
# function to fill the grid with two value at the start of the game
while number_needed >0:
    row_value = random.randint(0,3)
    column_value = random.randint(0,3)
    if grid[row_value][column_value]==0:
        grid[row_value][column_value]= generate_value()
        number_needed -=1

start = input("Hello Welcome to 2048.\nEnter your name to play the game:") # the welcome console of the game
if start.isalnum() == True:
    print(f"Hello '{start}' the aim of the game is to tile numbers to a larger number\n"
        " in any direction till the largest numebr  is 2048")
    print(">>>> use the following keys to tile numbers:\n"
        ">>>>H = to move left\n"
        ">>>>K = to move right\n"
        ">>>>P = to move up\n"
        ">>>>M = to move down\n")
    print("---------")
    draw_grid()

game_over = False
# function to check whether the game is over or not
while not  game_over:
    move = input("which way to go?").lower()

    valid_input = True
    temp_grid = copy.deepcopy(grid)
    # control keys
    if move =="p": # to merge the grid up
        grid= merge_up(grid)
    elif move == "m": # to merge the grid down
        grid= merge_down(grid)
    elif move == "h": # to merge the grid left
        grid = merge_left(grid)
    elif move == "k": # to merge the grid right
        grid = merge_right(grid)
    else:
        valid_input = False

    if not valid_input:
        print("invalid input, Plz try again")
    else:
        if grid == temp_grid:
            print("try another move:")
        else:
            if won():
                draw_grid()
                print("you won!")
                game_over=True
            else:
                generate_new_value()
                print("---------")
                draw_grid()
                if no_move():
                    print("you lost")
                    game_over = True




