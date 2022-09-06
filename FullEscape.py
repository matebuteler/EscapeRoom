from ctypes import alignment
import pygame, pygame_menu
import tkinter as tk
import time

equipo = 'Jorge Vidal'
next_room = False

def generate_popup(pista, titulo, correcto, unlocked):    
    global equipo
    # popup setup
    root = tk.Tk()
    root.title(pista)
    root.geometry("300x200")
    root.eval('tk::PlaceWindow . center')
    ans_var = tk.StringVar()

    # popup submission
    def submit():
        answer = ans_var.get()
        print(f"Respuesta : %answer%")
        if answer.lower() == correcto.lower():
            print("Respuesta Correcta")
            ans_var.set(correcto)
            display = tk.Label(root, text = unlocked)
            display.grid(row=5,column=1)
            if pista == "Acceso a la sala de investigacion":
                global next_room
                next_room = True
        else:
            ans_var.set("")

    # popup display
    message = tk.Label(root, text = titulo)
    ans_entry = tk.Entry(root, textvariable = ans_var, font = ('calibre',10,'normal'))
    sub_btn = tk.Button(root, text = 'Submit', command = submit)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    message.grid(row=1, column=1)
    ans_entry.grid(row=2,column=1)
    sub_btn.grid(row=3,column=1)
    
    
    root.mainloop()

class location:
    def __init__(self, lx, rx, ty, by):
        self.lx = lx
        self.rx = rx
        self.ty = ty
        self.by = by
vials = location(270,401,383,551)
microscope = location(432,495,250,409)
lab_journal = location(435,529,425,465)
tablet = location(92,246,453,531)
pictures1 = location(385,440,109,193)
pictures2 = location(330,396,202,290)
papers = location(307,371,102,167)
lamp = location(16,154,210,446)

# Museo, previo al escape room
def begin_room3(equipo):
    pygame.display.set_caption("Museo del Rompecabezas")
    gamedisplay.blit(pygame.image.load("Hab3"))


def begin_room4(team):
    pygame.display.set_caption('Escape Room') 
    global equipo
    equipo = team
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("ciudad.png"),(0,0))

    ending = False
    while not ending:

        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vials.lx <= mx <= vials.rx and vials.ty <= my <= vials.by:
                    generate_popup("Vials",
                                   "\nWhat is the cure and who was the murderer??\nThe CEO of ____ murdered Dr. Anthony\nfor the ____ cure! (name, cure)\n",
                                   "Zoom, mRNA",
                                   "\nCongrats, " + team + "!\nYou Solved the Murder and Found the Cure!\nThe World Thanks You!")
                    break
                if microscope.lx <= mx <= microscope.rx and microscope.ty <= my <= microscope.by:
                    generate_popup("Microscope",
                                   "\nWhat do St. Patrick's Day, coronavirus lockdowns,\nand daylight savings time have in common?\n",
                                   "March",
                                   "\nThere are some interesting slides under the microscope...\nThis one shows the key ingredient to the cure is mRNA!")
                    break
                if lamp.lx <= mx <= lamp.rx and lamp.ty <= my <= lamp.by:
                    generate_popup("Journal",
                                   "Entry: Mrxuqdo, Lw'v rqh gdb vlqfh wkh glvfryhub.\nL kdg d vwudqjh ylvlw wrgdb iurp wkh FHR ri Crrp.\nWkhb vhhphg yhub dqjub dqg wkuhdwhqhg ph.\nWhich of your tools decodes messages?\n",
                                   "CIPHER",
                                   "\nEntry: Journal, It's one day since the discovery.\nI had a strange visit today from the CEO of Zoom.\nThey seemed very angry and threatened me.\n")
                    break
        pygame.display.update()

    pygame.quit()
    quit()

piezasus = location(671,799,1,264)
tomacorrsus = location(130,531,416,595)
cuadro = location(613,650,51,272)
biblioteca = location(206,285,343,397)
cuerpo = location(581,775,318,406)
wall_clock = location(258,306,19,114)
journal = location(321,482,133,167)
trash = location(204,294,236,316)


# main loop
def begin_city(teamname):
    pygame.init()
    pygame.display.set_caption('Centro Civico')
    gameDisplay = pygame.display.set_mode((800,600))
    gameDisplay.blit(pygame.image.load("ciudadtx1.png"),(0,0))
#    sleep(5)
#    gameDisplay.blit(pygame.image.load("texto1.png"),(100,300))

#    gameDisplay.blit(pygame.image.load("textopablo.png")),(600,400)


def begin_room1(teamname):
    pygame.display.set_caption('Escape Room')
    global equipo
    equipo = teamname
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("ciudad.jpg"),(0,0))

    ending = False
    while not ending:

        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piezasus.lx <= mx <= piezasus.rx and piezasus.ty <= my <= piezasus.by:
                    generate_popup("Research Lab Access",
                                   "\nIdentification Required.\n(LAST_NAME.ID_NUMBER)\n",
                                   "ANTHONY.275403",
                                   "\nAccess Granted.")
                    global next_room
                    if next_room:
                        begin_room2(equipo)
                    break
                if tomacorrsus.lx <= mx <= tomacorrsus.rx and tomacorrsus.ty <= my <= tomacorrsus.by:
                    generate_popup("Body",
                                   "\nResearcher who found coronavirus cure was murdered!\nFind the murderer and the cure before its too late.\nType 'help' for more info:\n",
                                   "help",
                                   "\nClick around the room to investigate clues.\nSolve puzzles and take notes along the way.\nHave fun!")
                    break
                if cuadro.lx <= mx <= cuadro.rx and cuadro.ty <= my <= cuadro.by:
                    generate_popup("Lab Coat",
                                   "\nIn the pockets you find:\nPAPERCLIP, GUM WRAPPER, PEN, ID CARD,\nNOTE to revise journal on desk\n",
                                   "ID Card",
                                   "\nHead Scientist at *smudge*\nName: S Anthony\nID NUM: *smudge*")
                    break
                if biblioteca.lx <= mx <= biblioteca.rx and biblioteca.ty <= my <= biblioteca.by:
                    generate_popup("Phone",
                                   "\nThe cell phone won't turn on.\nIt seems to be missing something...\n",
                                   "PHONE BATTERY",
                                   "\nI_: _ 7 5 _ 0 3\t_ f_u_d _h_ c_r_.\n_u_o_s _p_e_d _a_t _n_ t_i_ m_y _u_t _o_e _o_p_n_e_.\n_ j_s_ w_n_ t_ s_v_ l_v_s_ b_t _ f_a_ m_n_ i_ i_ d_n_e_.\n_t_y _a_e _n_ w_a_ a _a_k_ j_s_ i_ c_s_.")
                    break
                if toolbox.lx <= mx <= toolbox.rx and toolbox.ty <= my <= toolbox.by:
                    generate_popup("Toolbox",
                                   "\nThe toolbox is locked with a four-digit lock.\nTry a code:\n",
                                   "0529",
                                   "\nInside:\nCIPHER\nPHONE BATTERY\nMAGNIFYING GLASS")
                    break
                if wall_clock.lx <= mx <= wall_clock.rx and wall_clock.ty <= my <= wall_clock.by:
                    generate_popup("Clock",
                                   "\nTurn me on my side and I am everything.\nCut me in half and I am nothing.\nWhat am I?\n",
                                   "eight",
                                   "\nHuh that's strange.\nThe clock is stuck at 05:29")
                    break
                if journal.lx <= mx <= journal.rx and journal.ty <= my <= journal.by:
                    generate_popup("Journal",
                                   "Entry: Mrxuqdo, Lw'v rqh gdb vlqfh wkh glvfryhub.\nL kdg d vwudqjh ylvlw wrgdb iurp wkh FHR ri Crrp.\nWkhb vhhphg yhub dqjub dqg wkuhdwhqhg ph.\n\nIt seems to be encrypted. Done reading?\n",
                                   "yes",
                                   "\nMaybe the cipher to this message is in another room...\nshift 3")
                    break
                if trash.lx <= mx <= trash.rx and trash.ty <= my <= trash.by:
                    generate_popup("Trash",
                                   "\nWhat can you catch, but never throw?\nA  _ _ _ _\n",
                                   "cold",
                                   "\n_D_ 2 _ _ 4 _ _\tI _o_n_ t_e _u_e_\nR_m_r_ s_r_a_ f_s_ a_d _h_s _a_ h_r_ s_m_ c_m_a_i_s_\nI _u_t _a_t _o _a_e _i_e_, _u_ I _e_r _i_e _s _n _a_g_r_\nS_a_ s_f_ a_d _e_r _ m_s_, _u_t _n _a_e_")
                    break
                print(event)
        pygame.display.update()

    pygame.quit()
    quit()



chair = location(388, 500, 518, 572)
door = location(600,700,120,460)

# main loop
def start_tutorial(teamname):
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("library.png"),(0,0))

    ending = False
    while not ending:

        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chair.lx <= mx <= chair.rx and chair.ty <= my <= chair.by:
                    generate_popup("Chair",
                                   "\nThere was a clue under the seat!\n\nThe more of this there is, the less you see.\nWhat is it?\n",
                                   "darkness",
                                   "\nOpen the door by saying OPEN")
                    pygame.time.wait(500)
                    break
                if door.lx <= mx <= door.rx and door.ty <= my <= door.by:
                    generate_popup("Door",
                                   "\nWhat's the password?\n",
                                   "OPEN",
                                   "\nFelicidades, " + teamname + "!\nGanaste!")
                    break
            #print(event)
        pygame.display.update()

    pygame.quit()
    quit()




pygame.init()
surface = pygame.display.set_mode((1000,1000))

teamname = 'Jorge Vidal'

def equipo(name):
    global teamname
    teamname = name

def start_game():
        print('Begin Main Game')
        begin_city(teamname) # from City
#        begin_room1(teamname) # from Room1

menu_theme = pygame_menu.themes.THEME_DARK.copy()
menu_theme.background_color = pygame_menu.baseimage.BaseImage(
    image_path=f"/home/mateo/Downloads/EscapeRoom-main/BgCarga.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER
)

menu = pygame_menu.Menu('Escape Room ', 1000, 1000,
                       theme=menu_theme)

menu.add.text_input('Nombre de equipo : ', default=' Jorge Vidal', onchange=equipo)
menu.add.button('Jugar', start_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)
