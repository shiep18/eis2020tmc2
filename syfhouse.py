
from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import os
import csv


class house():
    def __init__(self,data):
        self.data = data
        
    
    def buildhouse(self):
        x,y,z,L,W,H,M,roof,floor = self.data
        mc.setBlocks(x,y,z,x+10,y+6,z+10,220)
        mc.setBlocks(x+1,y+1,z+1,x+9,y+5,z+9,0) # 挖空
        mc.setBlocks(x+5,y+1,z,x+5,y+3,z+1,0) # 门
        mc.setBlocks(x+8,y+2,z+2,x+10,y+4,z+4,block.GLASS.id) # 窗




mc=Minecraft.create("47.100.46.95",4782)
pos = mc.player.getTilePos()
def syfhouse():
    reader = csv.reader(open('team2_clan.csv'))
    data = []
    for r in reader:
        if r[0] == 'clancenter':
            posx=int(r[1])
            posy=int(r[2])
            posz=int(r[3])
        if r[0] == 'syf':
            posx+=int(r[1])
            posy+=int(r[2])
            posz+=int(r[3])
    L = 10
    W = 10
    H = 6
    M = 1
    roof = 1
    floor = 1

    syfshouse = house([posx,posy,posz,L,W,H,M,roof,floor])
    syfshouse.buildhouse()

if __name__ == "__main__":
    syfhouse()


            

