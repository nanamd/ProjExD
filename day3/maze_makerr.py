import pygame
import sys
import random

CYAN= ( 0, 255,255)
GRAY = (96,96,96)

MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0]*MAZE_W)

def make_maze():
    XP = [0,1,0,-1]
    YP=[-1,0,1,0]

    #周りの壁
    for x in range(MAZE_W):
        maze[0][x]=1
        maze[MAZE_H-1][x]=1
    for y in range(1,MAZE_H-1):
        maze[y][0] =1
        maze[y][MAZE_W-1] = 1

    #中を何もない状態に
    for y in range(1,MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0

    #柱
    for y in range(2, MAZE_H-2,2):
        for x in range(2,MAZE_W-2,2):
            maze[y][x]=1

    #柱から上下左右に壁を作る
    for y in range(2,MAZE_H-2,2):
        for x in range(2, MAZE_W-2,2):
            d= random.randint(0,3)
            if x > 2:
                
