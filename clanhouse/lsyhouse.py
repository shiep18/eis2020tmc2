import mcpi.minecraft as minecraft
import mcpi.block as block
import numpy as np
import os
import csv

mc = minecraft.Minecraft.create("47.100.46.95",4782)
pos = mc.player.getTilePos()
print(pos.x, pos.y, pos.z)

def csv_read(name):
    with open(name, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    return result

class house():
    def __init__(self,data):
        self.data = data

    def buildhouse(self):
        x,y,z,L,W,H,M,roof,floor = self.data
        mc.setBlocks(x,y,z, x+10,y+6,z+10, M)
        mc.setBlocks(x+1,y+1,z+1, x+9,y+5,z+9, 0)
        mc.setBlocks(x+5,y+1,z, x+5,y+3,z+1, 0)                           # door
        mc.setBlocks(x+10,y+2,z+4, x+10,y+4,z+6, block.GLASS.id)          # window
        mc.setBlocks(x,y+2,z+4, x,y+4,z+6, block.GLASS.id)                # window
        mc.setBlocks(x,y+6,z, x+10,y+6,z+10, block.DIAMOND_ORE.id)        # roof
        mc.setBlocks(x,y+6,z, x+10,y+6,z+10, block.DIAMOND_ORE.id)        # roof


    
def lsyhouse():
    name_list = csv_read('./team2_clan.csv')
    pos_dic = {}
    for name in name_list:
        pos_dic[name[0]] = tuple(map(eval,name[1:]))

    myname = 'lsy'
    posx = pos_dic[myname][0] + pos_dic['clancenter'][0]
    posy = pos_dic[myname][1] + pos_dic['clancenter'][1]
    posz = pos_dic[myname][2] + pos_dic['clancenter'][2]

    L = 10
    W = 10
    H = 6
    M = 79
    roof = 1
    floor = 1

    lsyshouse = house([posx,posy,posz,L,W,H,M,roof,floor])
    lsyshouse.buildhouse()

if __name__ == "__main__":
    lsyhouse()
