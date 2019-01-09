import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Objects
#
#nothing = 0x00
#sword = 0x01
#bomb = 0x02
#power bracelet = 0x03
#shield = 0x04
#bow = 0x05
#hookshot = 0X06
#wand = 0X07
#boots = 0x08
#ocarina = 0x09
#feather = 0x0a
#shovel = 0x0b
#magic powder = 0x0c
#boomerang = 0x0d

data={
    #name length is 5 characters
    'name':'Link',
    #max of heart is 14
    'max_life': 4,
    #you got 4 piece for each heart
    'life': 16,
    #max money is 999
    'money': 999,
    #max arrow and bomb is 30
    'arrow': 30,
    'bomb': 30,
    #stuff level max 2 (except shield ?)
    'bracelet_level': 2,
    'shield_level': 3,
    'sword_level': 2,
    'left_hand': 0x04,
    'right_hand': 0x00,
    'stuff1': 0x00,
    'stuff2': 0x00,
    'stuff3': 0x00,
    'stuff4': 0x00,
    'stuff5': 0x00,
    'stuff6': 0x00,
    'stuff7': 0x00,
    'stuff8': 0x00,
    'stuff9': 0x00,
    'stuff10': 0x00
    }

data_position={
    'name': int("0x0000d454", 16),
    'max_life': int("0x0000d460", 16),
    'life': int("0x0000d45f", 16),
    'money': int("0x0000d462", 16),
    'arrow': int("0x0000d44a", 16),
    'bomb': int("0x0000d452", 16),
    'bracelet_level': int("0x0000d448", 16),
    'shield_level': int("0x0000d449", 16),
    'sword_level': int("0x0000d453", 16),
    'left_hand': int("0x0000d405", 16),
    'right_hand': int("0x0000d406", 16),
    'stuff1': int("0x0000d407", 16),
    'stuff2': int("0x0000d408", 16),
    'stuff3': int("0x0000d409", 16),
    'stuff4': int("0x0000d40a", 16),
    'stuff5': int("0x0000d40b", 16),
    'stuff6': int("0x0000d40c", 16),
    'stuff7': int("0x0000d40d", 16),
    'stuff8': int("0x0000d40e", 16),
    'stuff9': int("0x0000d40f", 16),
    'stuff10': int("0x0000d410", 16)
    }

filename = "Legend of Zelda, The - Link_s Awakening DX (France).state"

def load():
    global data, data_position
    with open(filename, 'r+b') as f:
        f.seek(data_position['name'])
        encoded_name = f.read(5)
        data['name'] = ""
        for k in range(len(encoded_name)):
            if(encoded_name[k]==0):
                data['name'] += " "
            else :
                data['name'] += chr(encoded_name[k]-1)
        f.seek(data_position['max_life'])
        encoded_max_life = f.read(1)
        data['max_life'] = int.from_bytes(encoded_max_life, byteorder='little')
        f.seek(data_position['life'])
        encoded_life = f.read(1)
        data['life'] = int(int(encoded_life.hex(), 16)/2)
        f.seek(data_position['money'])
        encoded_money = f.read(2)
        data['money'] = encoded_money[0]*100+int(hex(encoded_money[1])[2:])
        f.seek(data_position['arrow'])
        encoded_arrow = f.read(1)
        data['arrow'] = int(hex(encoded_arrow[0])[2:])
        f.seek(data_position['bomb'])
        encoded_bomb = f.read(1)
        data['bomb'] = int(hex(encoded_bomb[0])[2:])
        f.seek(data_position['bracelet_level'])
        encoded_bracelet_level = f.read(1)
        data['bracelet_level'] = int.from_bytes(encoded_bracelet_level, byteorder='little')
        f.seek(data_position['shield_level'])
        encoded_shield_level = f.read(1)
        data['shield_level'] = int.from_bytes(encoded_shield_level, byteorder='little')
        f.seek(data_position['sword_level'])
        encoded_sword_level = f.read(1)
        data['sword_level'] = int.from_bytes(encoded_sword_level, byteorder='little')
        f.seek(data_position['left_hand'])
        encoded_left_hand = f.read(1)
        data['left_hand'] = int(encoded_left_hand.hex(), 16)
        f.seek(data_position['right_hand'])
        encoded_right_hand = f.read(1)
        data['right_hand'] = int(encoded_right_hand.hex(), 16)
        f.seek(data_position['stuff1'])
        encoded_stuff1 = f.read(1)
        data['stuff1'] = int(encoded_stuff1.hex(), 16)
        f.seek(data_position['stuff2'])
        encoded_stuff2 = f.read(1)
        data['stuff2'] = int(encoded_stuff2.hex(), 16)
        f.seek(data_position['stuff3'])
        encoded_stuff3 = f.read(1)
        data['stuff3'] = int(encoded_stuff3.hex(), 16)
        f.seek(data_position['stuff4'])
        encoded_stuff4 = f.read(1)
        data['stuff4'] = int(encoded_stuff4.hex(), 16)
        f.seek(data_position['stuff5'])
        encoded_stuff5 = f.read(1)
        data['stuff5'] = int(encoded_stuff5.hex(), 16)
        f.seek(data_position['stuff6'])
        encoded_stuff6 = f.read(1)
        data['stuff6'] = int(encoded_stuff6.hex(), 16)
        f.seek(data_position['stuff7'])
        encoded_stuff7 = f.read(1)
        data['stuff7'] = int(encoded_stuff7.hex(), 16)
        f.seek(data_position['stuff8'])
        encoded_stuff8 = f.read(1)
        data['stuff8'] = int(encoded_stuff8.hex(), 16)
        f.seek(data_position['stuff9'])
        encoded_stuff9 = f.read(1)
        data['stuff9'] = int(encoded_stuff9.hex(), 16)
        f.seek(data_position['stuff10'])
        encoded_stuff10 = f.read(1)
        data['stuff10'] = int(encoded_stuff10.hex(), 16)
        f.close()

    name_input.delete(0, END)
    name_input.insert(0, data['name'])
    max_life_input.delete(0, END)
    max_life_input.insert(0, data['max_life'])
    life_input.delete(0, END)
    life_input.insert(0, data['life'])
    money_input.delete(0, END)
    money_input.insert(0, data['money'])
    arrow_input.delete(0, END)
    arrow_input.insert(0, data['arrow'])
    bomb_input.delete(0, END)
    bomb_input.insert(0, data['bomb'])
    bracelet_level_input.delete(0, END)
    bracelet_level_input.insert(0, data['bracelet_level'])
    shield_level_input.delete(0, END)
    shield_level_input.insert(0, data['shield_level'])
    sword_level_input.delete(0, END)
    sword_level_input.insert(0, data['sword_level'])
    left_hand_input.delete(0, END)
    left_hand_input.insert(0, data['left_hand'])
    right_hand_input.delete(0, END)
    right_hand_input.insert(0, data['right_hand'])
    stuff1_input.delete(0, END)
    stuff1_input.insert(0, data['stuff1'])
    stuff2_input.delete(0, END)
    stuff2_input.insert(0, data['stuff2'])
    stuff3_input.delete(0, END)
    stuff3_input.insert(0, data['stuff3'])
    stuff4_input.delete(0, END)
    stuff4_input.insert(0, data['stuff4'])
    stuff5_input.delete(0, END)
    stuff5_input.insert(0, data['stuff5'])
    stuff6_input.delete(0, END)
    stuff6_input.insert(0, data['stuff6'])
    stuff7_input.delete(0, END)
    stuff7_input.insert(0, data['stuff7'])
    stuff8_input.delete(0, END)
    stuff8_input.insert(0, data['stuff8'])
    stuff9_input.delete(0, END)
    stuff9_input.insert(0, data['stuff9'])
    stuff10_input.delete(0, END)
    stuff10_input.insert(0, data['stuff10'])

def save():
    data['name'] = name_input.get()
    data['max_life'] = int(max_life_input.get())
    data['life'] = int(life_input.get())
    data['money'] = int(money_input.get())
    data['arrow'] = int(arrow_input.get())
    data['bomb'] = int(bomb_input.get())
    data['bracelet_level'] = int(bracelet_level_input.get())
    data['shield_level'] = int(shield_level_input.get())
    data['sword_level'] = int(sword_level_input.get())
    data['left_hand'] = int(left_hand_input.get())
    data['right_hand'] = int(right_hand_input.get())
    data['stuff1'] = int(stuff1_input.get())
    data['stuff2'] = int(stuff2_input.get())
    data['stuff3'] = int(stuff3_input.get())
    data['stuff4'] = int(stuff4_input.get())
    data['stuff5'] = int(stuff5_input.get())
    data['stuff6'] = int(stuff6_input.get())
    data['stuff7'] = int(stuff7_input.get())
    data['stuff8'] = int(stuff8_input.get())
    data['stuff9'] = int(stuff9_input.get())
    data['stuff10'] = int(stuff10_input.get())
    with open(filename, 'r+b') as f:
        # name
        encoded_name=b''
        if(len(data['name'])>5):
            data['name'] = data['name'][:5]
        for k in range(len(data['name'])):
            letter = data['name'][k]
            encoded_name += bytes([ord(letter)+1])
        for k in range(5-len(data['name'])):
            encoded_name += b'\x00'
        #life
        encoded_max_life = bytes([data['max_life']])
        encoded_life = bytes([int(data['life']*2)])
        #money
        if(data['money']>999):
            data['money'] = 999
        encoded_money = bytes([int(data['money']/100)])
        encoded_money += bytes([int(str(data['money']%100), 16)])
        #bomb and arrow qty
        if(data['arrow']>30):
            data['arrow'] = 30
        if(data['bomb']>30):
            data['bomb'] = 30
        encoded_arrow = bytes([int(str(data['arrow']), 16)])
        encoded_bomb = bytes([int(str(data['bomb']), 16)])
        #stuff level
        if(data['shield_level']>3):
            data['shield_level'] = 3
        if(data['bracelet_level']>2):
            data['bracelet_level'] = 2
        if(data['sword_level']>2):
            data['sword_level'] = 2
        encoded_bracelet_level = bytes([int(str(data['bracelet_level']), 16)])
        encoded_shield_level = bytes([int(str(data['shield_level']), 16)])
        encoded_sword_level = bytes([int(str(data['sword_level']), 16)])
        #left_hand
        encoded_left_hand = bytes([int(str(data['left_hand']), 16)])
        #right_hand
        encoded_right_hand = bytes([int(str(data['right_hand']), 16)])
        #stuff
        encoded_stuff1 = bytes([data['stuff1']])
        encoded_stuff2 = bytes([data['stuff2']])
        encoded_stuff3 = bytes([data['stuff3']])
        encoded_stuff4 = bytes([data['stuff4']])
        encoded_stuff5 = bytes([data['stuff5']])
        encoded_stuff6 = bytes([data['stuff6']])
        encoded_stuff7 = bytes([data['stuff7']])
        encoded_stuff8 = bytes([data['stuff8']])
        encoded_stuff9 = bytes([data['stuff9']])
        encoded_stuff10 = bytes([data['stuff10']])

        #save name
        f.seek(data_position['name'])
        f.write(encoded_name)
        #save max life
        f.seek(data_position['max_life'])
        f.write(encoded_max_life)
        #save life
        f.seek(data_position['life'])
        f.write(encoded_life)
        #save money
        f.seek(data_position['money'])
        f.write(encoded_money)
        #save arrow
        f.seek(data_position['arrow'])
        f.write(encoded_arrow)
        #save bomb
        f.seek(data_position['bomb'])
        f.write(encoded_bomb)
        #save level
        f.seek(data_position['bracelet_level'])
        f.write(encoded_bracelet_level)
        f.seek(data_position['shield_level'])
        f.write(encoded_shield_level)
        f.seek(data_position['sword_level'])
        f.write(encoded_sword_level)
        #save hands
        f.seek(data_position['left_hand'])
        f.write(encoded_left_hand)
        f.seek(data_position['right_hand'])
        f.write(encoded_right_hand)
        #save stuff
        f.seek(data_position['stuff1'])
        f.write(encoded_stuff1)
        f.seek(data_position['stuff2'])
        f.write(encoded_stuff2)
        f.seek(data_position['stuff3'])
        f.write(encoded_stuff3)
        f.seek(data_position['stuff4'])
        f.write(encoded_stuff4)
        f.seek(data_position['stuff5'])
        f.write(encoded_stuff5)
        f.seek(data_position['stuff6'])
        f.write(encoded_stuff6)
        f.seek(data_position['stuff7'])
        f.write(encoded_stuff7)
        f.seek(data_position['stuff8'])
        f.write(encoded_stuff8)
        f.seek(data_position['stuff9'])
        f.write(encoded_stuff9)
        f.seek(data_position['stuff10'])
        f.write(encoded_stuff10)
        
        f.close()
    load()
    messagebox.showinfo("Information", "Data saved !")

def open_file():
    global filename
    fenetre = Tk()
    fenetre.filename=filedialog.askopenfilename(title="Select file", filetypes=(("state files", "*.state"),))
    filename = fenetre.filename
    fenetre.destroy()
    load()

root = Tk()

title = Label(root, text="Link's Awakening save Editor")
name_label = Label(root, text="Name (5 characters) :")
max_life_label = Label(root, text="Max Life (14 heart slot) :")
life_label = Label(root, text="Life (4 piece for each heart) :")
money_label = Label(root, text="Money (max 999 rupees) :")
arrow_label = Label(root, text="Arrow quantity (max 30) :")
bomb_label = Label(root, text="Bomb quantity (max 30) :")
bracelet_level_label = Label(root, text="Force bracelet level (max 2) :")
shield_level_label = Label(root, text="Shield level (max 3) :")
sword_level_label = Label(root, text="Sword level (max 2) :")
left_hand_label = Label(root, text="Left hand :")
right_hand_label = Label(root, text="Right hand :")
stuff_label = Label(root, text="Stuff slot :")
stuff_hexa = Label(root, text="Objects\n\nnothing = 0\nsword = 1\nbomb = 2\npower bracelet = 3\nshield = 4\nbow = 5\nhookshot = 6\nwand = 7\nboots = 8\nocarina = 9\nfeather = 10\nshovel = 11\nmagic powder = 12\nboomerang = 13")

name_input = Entry(root, width=20)
max_life_input = Entry(root, width=20)
life_input = Entry(root, width=20)
money_input = Entry(root, width=20)
arrow_input = Entry(root, width=20)
bomb_input = Entry(root, width=20)
bracelet_level_input = Entry(root, width=20)
shield_level_input = Entry(root, width=20)
sword_level_input = Entry(root, width=20)
left_hand_input = Entry(root, width=20)
right_hand_input = Entry(root, width=20)
stuff1_input = Entry(root, width=20)
stuff2_input = Entry(root, width=20)
stuff3_input = Entry(root, width=20)
stuff4_input = Entry(root, width=20)
stuff5_input = Entry(root, width=20)
stuff6_input = Entry(root, width=20)
stuff7_input = Entry(root, width=20)
stuff8_input = Entry(root, width=20)
stuff9_input = Entry(root, width=20)
stuff10_input = Entry(root, width=20)

load_button = Button(root, text="Load file", command=open_file)
save_button = Button(root, text="Save file", command=save)

title.grid(row=0, column=0)
stuff_hexa.grid(row=1, column=3, rowspan=8)
name_label.grid(row=1, column=0)
name_input.grid(row=2, column=0)
max_life_label.grid(row=1, column=1)
max_life_input.grid(row=2, column=1)
life_label.grid(row=1, column=2)
life_input.grid(row=2, column=2)
money_label.grid(row=3, column=0)
money_input.grid(row=4, column=0)
arrow_label.grid(row=5, column=0)
arrow_input.grid(row=6, column=0)
bomb_label.grid(row=5, column=1)
bomb_input.grid(row=6, column=1)
bracelet_level_label.grid(row=5, column=2)
bracelet_level_input.grid(row=6, column=2)
shield_level_label.grid(row=7, column=2)
shield_level_input.grid(row=8, column=2)
sword_level_label.grid(row=9, column=2)
sword_level_input.grid(row=10, column=2)
left_hand_label.grid(row=8, column=0)
left_hand_input.grid(row=9, column=0)
right_hand_label.grid(row=8, column=1)
right_hand_input.grid(row=9, column=1)
stuff_label.grid(row=11, column=0, columnspan=2)
stuff1_input.grid(row=12, column=0)
stuff2_input.grid(row=12, column=1)
stuff3_input.grid(row=13, column=0)
stuff4_input.grid(row=13, column=1)
stuff5_input.grid(row=14, column=0)
stuff6_input.grid(row=14, column=1)
stuff7_input.grid(row=15, column=0)
stuff8_input.grid(row=15, column=1)
stuff9_input.grid(row=16, column=0)
stuff10_input.grid(row=16, column=1)

load_button.grid(row=17, column=0)
save_button.grid(row=17, column=1)

root.mainloop()
