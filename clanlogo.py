import binvox_rw
import mcpi.minecraft as minecraft
import mcpi.block as block
import numpy as np
import os
import csv

mc = minecraft.Minecraft.create("47.100.46.95",4782)
pos=mc.player.getTilePos()

with open('clanlogo.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
#print(model.dims)
#print(model.scale)
#print(model.translate)
#print(model.data)

def csv_read(name):
    with open(name, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    return result

def clanlogo():
    name_list = csv_read('./team2_clan.csv')
    pos_dic = {}
    for name in name_list:
        pos_dic[name[0]] = tuple(map(eval,name[1:]))
        
    myname = 'clanlogo'
    posx = pos_dic[myname][0] + pos_dic['clancenter'][0]
    posy = pos_dic[myname][1] + pos_dic['clancenter'][1]
    posz = pos_dic[myname][2] + pos_dic['clancenter'][2]
    for y in range(model.dims[1]):
        print("layer y=",y)
        layer_data=model.data[y]
        stringlayer=""
        for x in range(model.dims[0]):
            stringlayer=stringlayer+"\n"
            for z in range(model.dims[2]):
                if model.data[x][y][z] == True:
                    stringlayer = stringlayer+'1'
                    mc.setBlock(posx+y,posy+z,posz+x,block.GOLD_BLOCK.id)
                else:
                    stringlayer=stringlayer+'0'
                    mc.setBlock(posx,posy,posz,block.AIR.id)
        print(stringlayer)

if __name__ == "__main__":
    clanlogo()

