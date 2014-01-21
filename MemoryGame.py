# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, exposed, deck, turns
    numbers = [i for i in range(8)] #list of numbers from 0 to 8
    deck = numbers + numbers #double list of numbers
    random.shuffle(deck) #shuffled list of numbers
    exposed = [False for i in range(16)]
    state = 0
    turns = 0
    #print "DEBUG memory list", deck
    #print "DEBUG exposed list", exposed
     
# define event handlers
def mouseclick(pos):
    global state, exposed, turns, card1, card2
    card_index = pos[0] // 50
    #print "DEBUG card position", card_index
    if not exposed[card_index]:
        if state == 0:
            exposed[card_index] = True
            card1 = card_index
            state = 1
        elif state == 1:
            exposed[card_index] = True
            card2 = card_index
            state = 2
        elif state == 2:
            exposed[card_index] = True
            if deck[card1] == deck[card2]:
                pass
            else:
                exposed[card1] = False
                exposed[card2] = False
            card1 = card_index
            state = 1
            turns += 1
            #print "DEBUG Turns = ", turns
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global turns
    for card_index in range(len(deck) - 1):
        canvas.draw_line([(card_index + 1) * 50, 0], [(card_index + 1) * 50, 100], 2, "White")
    for card_index in range(len(deck)):
        canvas.draw_text(str(deck[card_index]), [(15 + card_index * 50), 65], 50, "White")
        if not exposed[card_index]:
            canvas.draw_polygon([[card_index * 50, 0],
                                 [(card_index + 1) * 50, 0],
                                 [(card_index + 1) * 50, 100],
                                 [card_index * 50, 100]], 2, "Black", "Green")
    label.set_text("Turns = " + str(turns))
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0 ")
frame.add_label("Made by Anastasia Filatova")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
