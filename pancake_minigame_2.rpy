# klondike.rpy - Klondike Solitaire
# Copyright (C) 2008 PyTom <pytom@bishoujo.us>
#
# This software may be distributed in modified or unmodified form,
# provided:
#
# (1) This complete license notice is retained.
#
# (2) This software and all software and data files distributed
# alongside this software and intended to be loaded in the same
# memory space may be redistributed without requirement for
# payment, notification, or other forms of compensation.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Commercial licensing for this software is available, please
# contact pytom@bishoujo.us for information.

image bg pancake_minigame = "images/pancake_minigame/Background.png"
image table pancake_minigame = "images/pancake_minigame/Table.png"
image glass pancake_minigame = "images/pancake_minigame/Glass.png"
image Lophii pancake_minigame = "images/pancake_minigame/Character_Placeholder_lophii.png"
image lupin pancake_minigame = "images/pancake_minigame/Character_Placeholder_Lupin.png"
image tulip pancake_minigame = "images/pancake_minigame/Character_Placeholder_tulip.png"
image foreground pancake_minigame = "images/pancake_minigame/Foreground_asset.png"

transform pos_table:
    xpos 0
    ypos 845 

transform pos_glass_1:
    xpos 43
    ypos  790
transform pos_glass_2:
    xpos 669
    ypos 790
transform pos_glass_3:
    xpos 1259
    ypos 790

transform pos_lophii:
    xpos 111
    ypos 489
transform pos_lupin:
    xpos 739
    ypos 524
transform pos_tulip:
    xpos 1358
    ypos 553

transform pos_foreground_1:
    xpos 205
    ypos 928
transform pos_foreground_2:
    xpos 1242
    ypos 928

init python:

    class Klondike(object):

        # We represent a card as a (suit, rank) tuple. The suit is one of the
        # following four constants, while the rank is 1 for ace, 2 for 2,
        # ..., 10 for 10, 11 for jack, 12 for queen, 13 for king.        
        PANCAKE_SIZE_0 = 0
        PANCAKE_SIZE_1 = 1
        PANCAKE_SIZE_2 = 2
        PANCAKE_SIZE_3 = 3
        PANCAKE_SIZE_4 = 4
        
        def __init__(self, deal=3):

            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=770
            COL_SPACING = 628
            ROW_SPACING = 120
            CARD_XSPACING = 20
            CARD_YSPACING = -20

            # Store the parameters.
            self.deal = deal
            
            # Create the table, stock, and waste.
            self.table = t = Table(base="images/pancake_minigame/Plate.png", back="images/pancake_minigame/4.png")
            self.stock = t.stack(-1000, TOP, xoff=0, yoff=0, click=True)


            # The 4 foundation stacks.


            # The 7 tableau stacks.
            self.tableau = [ ]
            for i in range(0, 3):
                s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING, xoff=0, yoff=CARD_YSPACING, drag=DRAG_ABOVE, click=True, drop=True)
                self.tableau.append(s)

            # Create the stock and shuffle it.
            
            # Deal out the initial tableau.
            for j in range(0, 5):
                value = (0, j)
                t.card(value, "images/pancake_minigame/pancake_size_%d.png" % (4 - j))
                self.stock.append(value)
                self.tableau[0].append(value)              

            # Ensure that the bottom of each tableau is faceup.


        # This figures out the image filename for a given suit and rank.
        def card_num(self, suit):
            ranks = [ None, 1, 49, 45, 41, 37, 33, 29, 25, 21, 17, 13, 9, 5 ]
            return suit + ranks[rank]
                
        def show(self):
            self.table.show()

        def hide(self):
            self.table.hide()
            
        def tableau_drag(self, evt):

            card = evt.drag_cards[0]
            cards = evt.drag_cards
            stack = evt.drop_stack

            csuit, crank = card
            
            # If the stack is empty, allow a king to be dragged to it.
            if not stack:
                for i in cards:
                    stack.append(i)

                return "tableau_drag"

            # Otherwise, the stack has a bottom card.
            bottom = stack[-1]
            bsuit, brank = bottom

            # Figure out which of the stacks are black.
            cblack = (csuit == self.PANCAKE_SIZE_1) or (csuit == self.PANCAKE_SIZE_0)
            bblack = (bsuit == self.PANCAKE_SIZE_1) or (bsuit == self.PANCAKE_SIZE_0)
            

            # Can we legally place the cards?
            if crank > brank:
                for i in cards:
                    stack.append(i)

                return "tableau_drag"

            # Place the cards:
            

            return False
                    
        def foundation_drag(self, evt):

            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False

            suit, rank = evt.drag_cards[0]

            # If there is a card on the foundation already, then
            # check to see if we're dropping then next one in
            # sequence.

            return False
                
        def tableau_doubleclick(self, evt):

            # Make sure that there's at least one card in the stack.
            if not evt.stack:
                return False

            # The bottom card in the stack.
            card = evt.stack[-1]
            suit, rank = card

            # If the card is an ace, find an open foundation and put it
            # there.

            # Otherwise, see if there's a foundation where we can put
            # the card.

            return False

                    
        def interact(self):

            evt = ui.interact()
            rv = False
            
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag" and len(evt.drag_cards) == 1:
                if evt.drop_stack in self.tableau:
                    rv = self.tableau_drag(evt)

            if len(self.tableau[2]) == 5:
                return "win"
                    
            # Ensure that the bottom card in each tableau is faceup.

            # Check to see if any of the foundations has less than
            # 13 cards in it. If it does, return False. Otherwise,
            # return True.

        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
        
        # Utility functions.

        # Is it okay to drag the over card onto under, where under is
        # part of a tableau.

        # Returns the first faceup card in the stack.