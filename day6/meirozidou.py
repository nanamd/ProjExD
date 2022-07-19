import pygame
import random
import numpy as np
from pygame.locals import *
import sys
from time import sleep
 
sys.setrecursionlimit(10**6)
 
VAL_SPACE = 0
VAL_WALL = 1
VAL_PLAYER = 2
VAL_GOAL = 3
 
maze_width, maze_height = 21, 21
random_seed = 4
start_pos = (1, 1)
direction = [(0, -2), (0, 2), (-2, 0), (2, 0)]
 
maze_array = np.ones((maze_height, maze_width))
 
maze_array[start_pos] = 0 # 初期位置設定
 
 
def fn_print_maze(maze_array):
	for dy_list in maze_array:
		for item in dy_list:
			if item == VAL_SPACE:
				print("　", end="")
			elif item == VAL_WALL:
				print("■", end="")
			elif item == VAL_PLAYER:
				print("◎", end="")
			elif item == VAL_GOAL:
				print("△", end="")
			else:
				pass
		print("")
		
 
def fn_create_maze(updX, updY):
	rnd_array = list(range(random_seed))
	random.shuffle(rnd_array)
	
	for index in rnd_array:
		if updY + direction[index][1] < 1 or updY + direction[index][1] > maze_height-1:
			continue
		elif updX + direction[index][0] < 1 or updX + direction[index][0] > maze_width-1:
			continue
		elif maze_array[updY+direction[index][1]][updX+direction[index][0]] == 0:
			continue
		else:
			pass
			
		maze_array[updY+direction[index][1]][updX+direction[index][0]] = 0
		if index == 0:
			maze_array[updY+direction[index][1]+1][updX+direction[index][0]] = 0
		elif index == 1:
			maze_array[updY+direction[index][1]-1][updX+direction[index][0]] = 0
		elif index == 2:
			maze_array[updY+direction[index][1]][updX+direction[index][0]+1] = 0
		elif index == 3:
			maze_array[updY+direction[index][1]][updX+direction[index][0]-1] = 0
		else:
			pass
		
		sleep(0.2)
		fn_print_maze(maze_array)
		fn_create_maze(updX+direction[index][0], updY+direction[index][1])
 
def fn_search_goal(search_array, dx, dy):
	if search_array[dy][dx] == VAL_GOAL:
		return [(dx, dy)]
	
	search_array[dy][dx] = VAL_WALL
	
	for updX, updY in [(dx, dy+1), (dx+1, dy), (dx-1, dy), (dx, dy-1)]:
		if search_array[updY][updX] == VAL_WALL:
			continue
		route = fn_search_goal(search_array, updX, updY)
		if route is not None:
			return [(dx, dy)] + route
		
	
 
def fn_set_goalpos():
	
	space_index = np.where(maze_array == 0)
 
	goal_index = random.randint(0, len(space_index[0]) - 1)
	
	max_dist = 0
	max_pos = start_pos
	for index in range(len(space_index[0])):
#		print(space_index[0][index], space_index[1][index])
 
		tmp_array = maze_array.copy()
		
		tmp_array[space_index[0][index]][space_index[1][index]] = VAL_GOAL
		
		result = fn_search_goal(tmp_array, start_pos[0], start_pos[1])
		
		if result is not None:
			if len(result) > max_dist:
				max_dist = len(result)
				max_pos = (space_index[0][index], space_index[1][index])
				
	
	maze_array[max_pos[0]][max_pos[1]] = VAL_GOAL
 
if __name__ == '__main__':
	fn_create_maze(start_pos[0], start_pos[1])
	maze_array[start_pos] = VAL_PLAYER
	fn_set_goalpos()
	
	print("result")
		
	fn_print_maze(maze_array)
 