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
import threading
import time
from playsound import playsound
next_room = False


def generate_text(contenido,titulo = "Mensaje",size = ("400x150")):
    root = tk.Tk()
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    root.title(titulo)
    root.geometry(size)
    label = tk.Label(frame1,text=contenido,justify=tk.LEFT)
    label.pack(side=tk.LEFT)
    B1 = tk.Button(frame2,text="Aceptar",command=root.destroy)
    B1.pack()
    frame1.pack(padx=1,pady=1)
    frame2.pack(padx=10,pady=10)
    root.mainloop()


def generate_popupyesno(titulo, contenido):
    root = tk.Tk()
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    root.title(titulo)
    label = tk.Label(frame1,text=contenido,justify=tk.LEFT)
    label.pack(side=tk.LEFT)
    def anspopup(x):
        global anspopup
        anspopup = x
        root.destroy()
    B1 = tk.Button(frame2,text="Sí",command=anspopup(True))
    B1.pack()
    B2 = tk.Button(frame2,text="No",command=anspopup(False))
    B2.pack()
    frame1.pack(padx=1,pady=1)
    frame2.pack(padx=10,pady=10)
    root.mainloop()
#    time.sleep(0.5)
    return anspopup


def generate_popup(pista, titulo, correcto, unlocked):
    # popup setup
    root = tk.Tk()
    root.title(pista)
    root.geometry("400x350")
    root.eval('tk::PlaceWindow . center')
    ans_var = tk.StringVar()

    # popup submission
    def submit():
        answer = ans_var.get()
        print(f"Respuesta : {answer}")
        if answer.lower() == correcto.lower():
            print("Respuesta Correcta")
            ans_var.set(correcto)
            display = tk.Label(root, text = unlocked)
            display.grid(row=5,column=1)
            root.update()
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
    if unlocked == "COMPUTADORA DESBLOQUEADA. INICIANDO SISTEMA...":
        time.sleep(1)
        open_computer()
        
    
    root.mainloop()


class location:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
#aaaaaaaaa = location(x1 ,y1 ,x2 ,y2 )
#Locations (Room 1)
tcsus = location(311, 268, 359, 325)
piezasus = location(377, 517, 406, 546)
cadaver = location(376, 408, 503, 516)


#Locations (Room 2)
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
def begin_city():
    pygame.init()
    pygame.display.set_caption('Escapa del Museo - Centro Cívico')
    gameDisplay = pygame.display.set_mode(size=(800,600))
    gameDisplay.blit(pygame.image.load("assets/bg/BgRoom1.jpg"),(0,0))
    pygame.display.update()
    clock = pygame.time.Clock()
    endcity = False
    gameDisplay.blit(pygame.image.load("assets/pablo.png"),(100,300))
    gameDisplay.blit(pygame.image.load("assets/txpablo.png"),(100,350))
    while not endcity:
        clock.tick(1)
        pygame.time.delay(1500)
        pygame.display.update()
        pygame.time.delay(5000)
        begin_room2()
        pygame.display.update()

    pygame.display.update()


# Museo, previo al escape room
def begin_room2():
    pygame.display.set_caption("Museo del Rompecabezas")
    gameDisplay.blit(pygame.image.load("assets/bg/BgRoom2.png"),(0,0))
    hasTouchedCadaver = False
    while not next_room:
        mx, my = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #ensure the user can quit the game at all times
                pygame.quit()
                quit()
            if event.type == pygame.K_SPACE:    #whenever the user presses space
                
                if (generate_popupyesno("Cadaver", "El detective Pablo no te permitió tocar nada.\n Sin embargo, ese cadáver parece esconder algo... \n Acercarse?" )):
                        hasTouchedCadaver = True
                        time.sleep(0.5)
                        if generate_popupyesno("Pieza sospechosa", "Cayó una pieza de rompecabezas al suelo! \n Tiene un sólo diente; algo no cuadra... \n ¿Guardarla?"):
                            tienePiezaSus = True
                            generate_text("Pieza sospechosa", "La pieza se guardó en tu inventario.")
                            time.sleep(0.5)

                
                
                if (generate_popupyesno("Tomacorriente", "El tomacorriente parece estar dañado, pero no puedes ver bien.\n Acercarse?" )):
                    gameDisplay.blit(pygame.image.load("assets/bg/TCsus.png"),(0,0)) #Detalle del tomacorriente sospechoso
                    time.sleep(2.5)
                    if generate_popupyesno("Tomacorriente extraño","La pieza de antes parece encajar... \n ¿Encajar en el tomacorriente?"):
                        if generate_popupyesno("¡Algo extraño sucede!","¡La biblioteca era una puerta secreta! \n Se abrió al encajar la pieza que estaba en el cadáver con el tomacorriente. \n ¡Seguramente tenga que ver con el caso! ¿Entrar?") == True:
                            begin_room3() #Entered the true escape room


def begin_room3():
    pygame.display.set_caption('Escapa del Museo') 
    timeleft = 1800
    timestopped = False
    pygame.init()
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("assets/bg/BgRoom3.png"),(0,0))
#    threading.Thread(target=count, args=(1800)).start()
    ending = False
    while not timestopped:
        time.sleep(1)
        timeleft = timeleft - 1
        if timeleft == 0:
            timestopped = True
        mins, secs = divmod(timeleft, 60)
        hleft = '{:02d}:{:02d}'.format(mins, secs)
        pygame.display.set_caption(f'{hleft}  PARA ESCAPAR')
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cajafuerte.x1 <= mx <= cajafuerte.x2 and cajafuerte.y1 <= my <= cajafuerte.y2:
                    if hasCrackedPC == True:
                        if generate_popupyesno("Caja fuerte", "La caja fuerte está abierta. \n ¿Quieres ver lo que hay dentro?"):
                            generate_text("Caja fuerte", "¡Encontraste un texto extraño! \n ¡Guardala en tu inventario!")
                            
                    else:    
                        generate_text("Caja Fuerte","\La caja fuerte está cerrada. \n No parece haber manera de abrirla...")
                    break
                if monitor.x1 <= mx <= monitor.x2 and monitor.y1 <= my <= monitor.y2:
                    generate_popup("Computadora",
                                   "\La computadora requiere una contraseña. \n Intenta una:",
                                   "ax027",
                                   "COMPUTADORA DESBLOQUEADA. INICIANDO SISTEMA...")
                    break
                if afiche1.x1 <= mx <= afiche1.x2 and afiche1.y1 <= my <= afiche1.y2:
                    generate_text("Afiche 1", "El afiche dice: \n ¡El arte es la única forma de comunicación que no se puede censurar! \n - Pablo Picasso")
                    break
                if afiche2.x1 <= mx <= afiche2.x2 and afiche2.y1 <= my <= afiche2.y2:
                    generate_text("Afiche extraño"," ⏭    K \n ➳    L \n𝀦    M\n𝀓    N\n➙    O\n【    P\n】    Q\n『    R\n』    S\n」    T")
                if cajonsus.x1 <= mx <= cajonsus.x2 and cajonsus.y1 <= my <= cajonsus.y2:
                    generate_text("Cajón","Hay un papel en el cajón. Escrito tiene esto:\n」〓 ⇒ ↑ ㉿ ↑ ㉿ 〘 ᑘ ᔜ 〙⧬ ⇒ ⧬ 』")
                    break
                if rendija.x1 <= mx <= rendija.x2 and rendija.y1 <= my <= rendija.y2:
                    if generate_popupyesno("Rendija","Hay algo en la rendija, pero no puedes verlo bien.\nUsa tu linterna para verlo mejor.",) == True:
                        gameDisplay.blit(pygame.image.load("assets/rendijailuminada.png"),(152,164))
                    break
                if radio.x1 <= mx <= radio.x2 and radio.y1 <= my <= radio.y2:
                    if generate_popupyesno("Radio","La radio está apagada.\nLa perilla para seleccionar frecuencia parece estar rota.\n ¿Encender?") == True:
                        pygame.mixer.music.load("assets/radio.mp3")
                        pygame.mixer.music.play(0)
                    break
    pygame.quit()
    quit()


def open_computer():
    listbox = []
    global hasCrackedPC
    hasCrackedPC = False
    def play(track):
        if track == "del":
            listbox = []
            return
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(0)
        listbox.append(track)
        if len(listbox) == 3 and listbox[0] == "assets/sound/3.mp3" and listbox[1] == "assets/sound/0.mp3" and listbox[2] == "assets/sound/1.mp3" and listbox[3] == "assets/sound/1.mp3":
            generate_text("¡Encontraste la contraseña! \n ¡Ahora puedes abrir la caja fuerte!")
            hasCrackedPC = True
            root.destroy()
    root = tk.Tk()
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    root.title("Mensaje")
    root.geometry("350x350")
    label = tk.Label(frame1,text="BIENVENIDO AL SISTEMA",justify=tk.CENTER)
    label.pack(side=tk.LEFT)
    B1 = tk.Button(frame2,text="⬤",command=root.destroy)
    B1.pack()
    B2 = tk.Button(frame2,text="⭕",command=root.destroy)
    B2.pack()
    B3 = tk.Button(frame2,text="⬛",command=root.destroy)
    B3.pack()
    B4 = tk.Button(frame2,text="◁",command=root.destroy)
    B4.pack()
    B5 = tk.Button(frame2,text="BORRAR",command=play("del"))
    frame1.pack(padx=1,pady=1)
    frame2.pack(padx=10,pady=10)
    root.mainloop()


pygame.init()
surface = pygame.display.set_mode((800,600))

equipo = 'Jorge Vidal'


def teamname(n):
    global equipo
    equipo = n

def start_game():
    generate_text("!Bienvenido al Escape Room!\n Controles: Para avanzar en la historia/diálogos, presiona espacio.\n Busca cosas sospechosas y clickealas para interactuar con ellas. \n ¡Buena Suerte!")
    print('Begin Main Game')
#    begin_city() # from City1
    begin_room3() # from Room1
    

gameDisplay = pygame.display.set_mode(size=(800,600))
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
pygame.display.set_caption("Escapa del Museo - Menú")
menu_theme = pygame_menu.themes.THEME_DARK.copy()
menu_theme.background_color = pygame_menu.baseimage.BaseImage(
    image_path="assets/bg/BgCarga.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER
)
menu = pygame_menu.Menu('Escape Room ', 800, 600,
                       theme=menu_theme)

menu.add.text_input('Nombre de equipo : ', default='Jorge Vidal', onchange=teamname)
menu.add.button('Jugar', start_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(surface)
