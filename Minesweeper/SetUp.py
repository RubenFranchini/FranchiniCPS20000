import pygame
import os

pygame.init()

white = (255,255,255)
black = (0,0,0)
darkgray = (40,40,40)
lightgray = (100,100,100)
green = (0,255,0)
darkgreen = (0,200,0)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
gray = (200,196,196)

tilesize = 32
rows = 15
cols = 15
amount_mines = 16
width = tilesize*cols
header = tilesize * 3
height = tilesize*rows + header
fps = 60
title = "Minesweeper"

tile_numbers = []
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Images", f"Tile{i}.png")), (tilesize, tilesize)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Images", "TileEmpty.png")), (tilesize, tilesize))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("Images", "TileExploded.png")), (tilesize, tilesize))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Images", "TileFlag.png")), (tilesize, tilesize))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("Images", "TileMine.png")), (tilesize, tilesize))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Images", "TileUnknown.png")), (tilesize, tilesize))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("Images", "TileNotMine.png")), (tilesize, tilesize))

font = pygame.font.Font(os.path.join("Images", "Pixeltype.ttf"), 50)
