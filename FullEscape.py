"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
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
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
#aaaaaaaaa = location(x1 ,y1 ,x2 ,y2 )
cajafuerte = location(4,247,63,299)
afiche1 = location(284,269,313,285)
afiche2 = location(293,289,322,323)
afiche3 = location(347,293,377,311)
afiche4 = location(368,270,389,296)
impresora = location(58,343,158,426)
monitor = location(357,314,433,345)
rendija = location(153,180,193,228)
cajonsus = location(486,360,516,375)
cajblanca = location(161,331,198,372)
cuadro1 = location(520,240,537,290)
cuadro2 = location(539,238,554,289)
cuadro3 = location(562,230,584,288)
radio = location(477,290,506,310)

# Ciudad
def begin_city(teamname):
    pygame.init()
    pygame.display.set_caption('Escapa del Museo - Centro Cívico')
    gameDisplay = pygame.display.set_mode((800,600))
    gameDisplay.blit(pygame.image.load("assets/bg/BgRoom1.jpg"),(0,0))
    pygame.display.update()
    clock = pygame.time.Clock()
    endcity = False
    gameDisplay.blit(pygame.image.load("pablo.png"),(100,300))
    while not endcity:
        clock.tick(1)
        pygame.time.delay(1500)
        pygame.display.update()
        pygame.time.delay(5000)
        gameDisplay.blit(pygame.image.load("assets/bg/BgRoom1.jpg"),(0,0))
        pygame.display.update()

    pygame.display.update()

# Museo, previo al escape room
def begin_room2(equipo):
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Museo del Rompecabezas")
    gameDisplay.blit(pygame.image.load("assets/bg/BgRoom2.png"))


def count(t):
    global timestopped
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    timestopped = True

def begin_room3(team):
    pygame.display.set_caption('Escapa del Museo') 
    global equipo
    equipo = team
    timeleft = 1800
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("assets/bg/BgRoom3.png"),(0,0))
    count(1800) # 1800 s = 30min
    ending = False
    while not timestopped:
        pygame.display.set_caption(f'{timeleft}  PARA ESCAPAR')
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cajafuerte.x1 <= mx <= cajafuerte.x2 and cajafuerte.y1 <= my <= cajafuerte.y2:
                    generate_popup("cajafuerte",
                                   "\nWhat is the cure and who was the murderer??\nThe CEO of ____ murdered Dr. Anthony\nfor the ____ cure! (name, cure)\n",
                                   "Zoom, mRNA",
                                   "\nCongrats, " + team + "!\nYou Solved the Murder and Found the Cure!\nThe World Thanks You!")
                    break
                if afiche1.x1 <= mx <= afiche1.x2 and afiche1.y1 <= my <= afiche1.y2:
                    generate_popup("afiche1",
                                   "\nWhat do St. Patrick's Day, coronavirus lockdowns,\nand daylight savings time have in common?\n",
                                   "March",
                                   "\nThere are some interesting slides under the afiche1...\nThis one shows the key ingredient to the cure is mRNA!")
                    break
                if impresora.x1 <= mx <= impresora.x2 and impresora.y1 <= my <= impresora.y2:
                    generate_popup("Journal",
                                   "Entry: Mx2uqdo, Lw'v rqh gdb vlqfh wkh glvfryhub.\nL kdg d vwudqjh ylvlw wrgdb iurp wkh FHR ri Crrp.\nWkhb vhhphg yhub dqjub dqg wkuhdwhqhg ph.\nWhich of your tools decodes messages?\n",
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



#    gameDisplay.blit(pygame.image.load("textopablo.png")),(600,400)

"""""
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
                if piezasus.x1 <= mx <= piezasus.x2 and piezasus.y1 <= my <= piezasus.y2:
                    generate_popup("Research Lab Access",
                                   "\nIdentification Required.\n(LAST_NAME.ID_NUMBER)\n",
                                   "ANTHONY.275403",
                                   "\nAccess Granted.")
                    global next_room
                    if next_room:
                        begin_room2(equipo)
                    break
                if tomacorrsus.x1 <= mx <= tomacorrsus.x2 and tomacorrsus.y1 <= my <= tomacorrsus.y2:
                    generate_popup("Body",
                                   "\nResearcher who found coronavirus cure was murdered!\nFind the murderer and the cure before its too late.\ny1pe 'help' for more info:\n",
                                   "help",
                                   "\nClick around the room to investigate clues.\nSolve puzzles and take notes along the way.\nHave fun!")
                    break
                if cuadro.x1 <= mx <= cuadro.x2 and cuadro.y1 <= my <= cuadro.y2:
                    generate_popup("Lab Coat",
                                   "\nIn the pockets you find:\nPAPERCLIP, GUM WRAPPER, PEN, ID CARD,\nNOTE to revise journal on desk\n",
                                   "ID Card",
                                   "\nHead Scientist at *smudge*\nName: S Anthony\nID NUM: *smudge*")
                    break
                if biblioteca.x1 <= mx <= biblioteca.x2 and biblioteca.y1 <= my <= biblioteca.y2:
                    generate_popup("Phone",
                                   "\nThe cell phone won't turn on.\nIt seems to be missing something...\n",
                                   "PHONE BATTERY",
                                   "\nI_: _ 7 5 _ 0 3\t_ f_u_d _h_ c_r_.\n_u_o_s _p_e_d _a_t _n_ t_i_ m_y _u_t _o_e _o_p_n_e_.\n_ j_s_ w_n_ t_ s_v_ l_v_s_ b_t _ f_a_ m_n_ i_ i_ d_n_e_.\n_t_y _a_e _n_ w_a_ a _a_k_ j_s_ i_ c_s_.")
                    break
                if toolbox.x1 <= mx <= toolbox.x2 and toolbox.y1 <= my <= toolbox.y2:
                    generate_popup("Toolbox",
                                   "\nThe toolbox is locked with a four-digit lock.\nTry a code:\n",
                                   "0529",
                                   "\nInside:\nCIPHER\nPHONE BATTERY\nMAGNIFYING GLASS")
                    break
                if wall_clock.x1 <= mx <= wall_clock.x2 and wall_clock.y1 <= my <= wall_clock.y2:
                    generate_popup("Clock",
                                   "\nTurn me on my side and I am everything.\nCut me in half and I am nothing.\nWhat am I?\n",
                                   "eight",
                                   "\nHuh that's strange.\nThe clock is stuck at 05:29")
                    break
                if journal.x1 <= mx <= journal.x2 and journal.y1 <= my <= journal.y2:
                    generate_popup("Journal",
                                   "Entry: Mx2uqdo, Lw'v rqh gdb vlqfh wkh glvfryhub.\nL kdg d vwudqjh ylvlw wrgdb iurp wkh FHR ri Crrp.\nWkhb vhhphg yhub dqjub dqg wkuhdwhqhg ph.\n\nIt seems to be encrypted. Done reading?\n",
                                   "yes",
                                   "\nMaybe the cipher to this message is in another room...\nshift 3")
                    break
                if trash.x1 <= mx <= trash.x2 and trash.y1 <= my <= trash.y2:
                    generate_popup("Trash",
                                   "\nWhat can you catch, but never throw?\nA  _ _ _ _\n",
                                   "cold",
                                   "\n_D_ 2 _ _ 4 _ _\tI _o_n_ t_e _u_e_\nR_m_r_ s_r_a_ f_s_ a_d _h_s _a_ h_r_ s_m_ c_m_a_i_s_\nI _u_t _a_t _o _a_e _i_e_, _u_ I _e_r _i_e _s _n _a_g_r_\nS_a_ s_f_ a_d _e_r _ m_s_, _u_t _n _a_e_")
                    break
                print(event)
        pygame.display.update()

    pygame.quit()
    quit()
"""


chair = location(388, 500, 518, 572)
door = location(600,700,120,460)

pygame.init()
surface = pygame.display.set_mode((1000,1000))

teamname = 'Jorge Vidal'

def equipo(name):
    global teamname
    teamname = name

def start_game():
        print('Begin Main Game')
        begin_city(teamname) # from City1
#        begin_room1(teamname) # from Room1

menu_theme = pygame_menu.themes.THEME_DARK.copy()
menu_theme.background_color = pygame_menu.baseimage.BaseImage(
    image_path=f"/home/mateo/Downloads/EscapeRoom-main/assets/bg/BgCarga.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER
)

menu = pygame_menu.Menu('Escape Room ', 1000, 1000,
                       theme=menu_theme)

menu.add.text_input('Nombre de equipo : ', default=' Jorge Vidal', onchange=equipo)
menu.add.button('Jugar', start_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)
