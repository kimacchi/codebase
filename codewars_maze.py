from tokenize import String
from pathfinding.core.grid import Grid
import numpy as np
from pathfinding.finder.a_star import AStarFinder
import time




def solve(path, player):
    movements = []
    for i in range(len(path)-1):
        if(path[i][0] > path[i+1][0]):
            if(player !="<"):
                if(player == ">"):
                    movements.append("B")
                elif(player == "v"):
                    movements.append("R")
                else:
                    movements.append("L")
                player = "<"
            movements.append("F")
        elif(path[i][0] < path[i+1][0]):
            if(player !=">"):
                if(player == "<"):
                    movements.append("B")
                elif(player == "v"):
                    movements.append("L")
                else:
                    movements.append("R")
                player = ">"
            movements.append("F")      
        elif(path[i][1] > path[i+1][1]):
            if(player !="^"):
                if(player == "<"):
                    movements.append("R")
                elif(player == "v"):
                    movements.append("B")
                else:
                    movements.append("L")
                player = "^"
            movements.append("F")
        elif(path[i][1] < path[i+1][1]):
            if(player !="v"):
                if(player == "<"):
                    movements.append("L")
                elif(player == "^"):
                    movements.append("B")
                else:
                    movements.append("R")
                player = "v"
            movements.append("F")      
    return movements
          


def escape(maze):
    grid = np.zeros((len(maze), len(maze[0])),dtype=int)
    x, y = 0, 0
    player = "a"
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if(maze[i][j] == "#"):
                continue
            elif(maze[i][j] == " "):
                grid[i,j] = 1
            elif(maze[i][j] in "<>^v"):
                player = maze[i][j]
                grid[i,j] = 1
                x,y = j,i
    list1 = grid.tolist()
    start, end = -1,-1
    for i in range(len(maze[0])):
        if(grid[0,i] == 1):
            start,end = i,0
            break
        elif(grid[len(maze)-1,i] == 1):
            start,end = i,len(maze)-1
            break
    if(start == -1):
        for i in range(len(maze)):
            if(grid[i,0]==1):
                start, end = 0,i
                break
            elif(grid[i,len(maze[0])-1] == 1):
                 start,end = len(maze[0])-1,i
    solvingmaze = Grid(matrix=list1)
    finder = AStarFinder()
    a = solvingmaze.node(x,y)
    b= solvingmaze.node(start,end)
    path,runs = finder.find_path(a,b,solvingmaze)
    if(path == []):
        return []
    else:
        return solve(path,player) 

        
        

timenow = time.time()  

print(escape([
  "#########################################",
  "#<    #       #     #         # #   #   #",
  "##### # ##### # ### # # ##### # # # ### #",
  "# #   #   #   #   #   # #     #   #   # #",
  "# # # ### # ########### # ####### # # # #",
  "#   #   # # #       #   # #   #   # #   #",
  "####### # # # ##### # ### # # # #########",
  "#   #     # #     # #   #   # # #       #",
  "# # ####### ### ### ##### ### # ####### #",
  "# #             #   #     #   #   #   # #",
  "# ############### ### ##### ##### # # # #",
  "#               #     #   #   #   # #   #",
  "##### ####### # ######### # # # ### #####",
  "#   # #   #   # #         # # # #       #",
  "# # # # # # ### # # ####### # # ### ### #",
  "# # #   # # #     #   #     # #     #   #",
  "# # ##### # # ####### # ##### ####### # #",
  "# #     # # # #   # # #     # #       # #",
  "# ##### ### # ### # # ##### # # ### ### #",
  "#     #     #     #   #     #   #   #    ",
  "#########################################"
]))

print(time.time()-timenow)