image pieces_store = "images/map/pieces_store.png"

transform pos_store:
    xpos 40
    ypos 40

init python:

    def map_frqagment_dragged(drop, drags):
        global current_dragged
        global minimap_places
        store.current_dragged = -1
        q = 150
        w = int(drags[0].drag_name)
        #drags[0].snap(q+w*200, 700, 0.1)
        if not drop:
            q = 150
            w = int(drags[0].drag_name)
            drags[0].snap(q+w*200, 700, 0.1)
            return
        #elif drop.drag_name == drags[0].drag_name:
        else:
            drags[0].snap(drop.x - 50,drop.y - 51)
            temo = str(drop.x) + " " + str(drop.y)
            store.minimap_places[int(drop.drag_name)]=w
            finished=0
            for i in range(16):
                if minimap_places[i]==i:
                    if store.minimap_rotations[i]==0:
                        finished +=1
            if finished == 16:
                return() # renpy.jump("l_after_minimap_minigame")
            else:
                renpy.restart_interaction()
                return


        return

    def map_space_pressed():
        pass

    def map_fragmen_clicked(drags):
        store.current_dragged = int(drags[0].drag_name)
        pass

    def map_space_pressed():
        if store.current_dragged+1:
            store.minimap_rotations[store.current_dragged] += 90
            if store.minimap_rotations[store.current_dragged] >= 360:
                store.minimap_rotations[store.current_dragged] = 0
        pass
    
transform map_fragment_selected:
    matrixcolor TintMatrix("#f5e06a")
    # zoom 0.6

transform map_fragment_idle:
    matrixcolor TintMatrix("#FFF")
    #zoom 0.6
transform map_piece_rotation(piece):
    rotate minimap_rotations[piece]

transform map_fragment_idle_1:
    matrixcolor TintMatrix("#FFF")
    zoom 0.6
    rotate minimap_rotations[1]

transform map_fragment_idle_2:
    matrixcolor TintMatrix("#FFF")
    zoom 0.6
    rotate minimap_rotations[2]

define qwe = Solid("#613661",xsize=700,ysize=200)

default minimap_places = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
default minimap_rotations = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
default current_dragged =-1

label l_after_minimap_minigame:
    return()

screen scr_map_minigame():
    #background color
    add Solid("#0000004d")
    text "{color=#00ff00}Drag with mouse, \nrotate with SPACE{/color}":
        xalign 0.1
        xsize 500
        yalign 0.2

    #vbox:
    #    for i in minimap_places:
    #       text "[i]"
    #vbox:
    #   xpos 50
    #   for i in minimap_rotations:
    #       text "[i]"
    #text "[current_dragged]" xpos 100

    draggroup:
        # pieces
        for i in range(16):
            $temp = map_piece_rotation(i)
            #if not i in minimap_places:
            drag:
                drag_name str(i)
                ypos 10 + 40 + int((i%2))*5 + int((i%2))*250
                xpos 10 + 40 + int((i%2))*5 + (i%2)*250
                draggable True
                droppable False
                #dragged map_frqagment_dragged
                activated map_fragmen_clicked
                idle_child At("images/map/"+ str(i+1) +".png",map_fragment_idle,temp)
                hover_child At("images/map/"+ str(i+1) + ".png",map_fragment_selected,temp)
                selected_hover_child At("images/map/"+ str(i+1) + ".png",map_fragment_selected,temp)

    #    $temp = minimap_places[0]
        for i in range(16):
            drag:
                drag_name str(i)
                draggable False
                droppable True
                dropped map_frqagment_dragged
                xpos 800 + (i%4)*250
                ypos 10 + int((i/4))*250
                #if minimap_places[i]==-1:
                idle_child Solid("#0000004d") xsize 250 ysize 250
                #else:
                #    idle_child At("images/"+str(minimap_places[i]+1) +".png", map_fragment_idle)

    key "K_SPACE" action Function(map_space_pressed)
    pass
