# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool roots, actions, and settings.

from tkinter import *
from tkinter import ttk
from icons import icon
from tags import get_tags

#System
root = Tk()
root.title('TagManager v.1.12')
root.configure(bg='#262d35')

import base64
temp_icon = "icon.ico"
icon_file = open(temp_icon, "wb")
icon_file.write(base64.b64decode(icon))
icon_file.close()

icon_path = temp_icon
root.iconbitmap(icon_path)

#Class to inheris window icon by
def create_child_window(title):
    child_window = Toplevel(root)
    child_window.title(title)
    child_window.iconbitmap(icon_path)
    return child_window

#Window size
window_width = 950
window_height = 750


#Centring function
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

#Menubar
menu_bar = Menu(root)
root.config(menu=menu_bar)

#File
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

#Help
def open_guide_popup():
    popup = create_child_window("Guide")
    popup.title("Guide")
    popup.configure(bg='#262d35')

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    popup_width = 384
    popup_height = 216
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    label1 = Label(popup, text="TAG MANAGER GUIDE",
                   font=("Helvetica", 14, "bold"), bg='#262d35', fg="#8d9296")
    label1.pack(fill="both", expand=True, pady=(20, 5))

    label2 = Label(popup, text="1) Choose desired tags,\n2) copy generated tags,\n3) clear after use.",
                   font=("Helvetica", 11), bg='#262d35', fg="#8d9296", justify="left", anchor="w")
    label2.pack(fill="both", expand=True, padx=(10, 10), pady=(5, 5))

    label3 = Label(popup, text="Thank you for using!",
                   font=("Helvetica", 14, "bold"), bg='#262d35', fg="#8d9296")
    label3.pack(fill="both", expand=True, pady=(5, 20))

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Guide", command=open_guide_popup)
menu_bar.add_cascade(label="Help", menu=help_menu)

#About
def open_about_popup():
    popup = create_child_window("About")
    popup.title("About")
    popup.configure(bg="#262d35")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    popup_width = 600
    popup_height = 280
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    def about_lbl_bold(parent, row, text, font):
        label = Label(parent, text=text, bg='#262d35', fg="#8d9296", justify="left", anchor="w", font=font)
        label.grid(row=row, column=0, padx=(10, 10), pady=(5, 0), sticky="e")

    def about_lbl_regular(parent, text, row, font):
        label = Label(parent, text=text, bg='#262d35', fg="#8d9296", justify="left", anchor="w", font=font)
        label.grid(row=row, column=1, padx=(10, 10), sticky="w")

    helvetica_bold = ("Helvetica", 12, "bold")
    helvetica_regular = ("Helvetica", 12)

    # Skipper
    about_lbl_bold(popup, row=0, text="", font=helvetica_regular)
    about_lbl_regular(popup, row=1, text="Tag Manager", font=helvetica_bold)
    #Skipper
    about_lbl_bold(popup,    row=2, text="", font=helvetica_regular)
    about_lbl_bold(popup,    row=3, text="Version:", font=helvetica_regular)
    about_lbl_regular(popup, row=3, text="v.1.12", font=helvetica_regular)
    about_lbl_bold(popup,    row=4, text="Description:", font=helvetica_regular)
    about_lbl_regular(popup, row=4, text="This application allow user to combine different tags into 1 line.", font=helvetica_regular)
    about_lbl_bold(popup,    row=5, text="Author:", font=helvetica_regular)
    about_lbl_regular(popup, row=5, text="Natani Flutesong, nataniflutesong@gmail.com", font=helvetica_regular)
    about_lbl_bold(popup,    row=6, text="Tip jar:", font=helvetica_regular)
    about_lbl_regular(popup, row=6, text="https://www.buymeacoffee.com/nataniflutesong", font=helvetica_regular)
    #Skipper
    about_lbl_bold(popup,    row=7, text="", font=helvetica_regular)
    about_lbl_regular(popup, row=8, text="Thank you for using!", font=helvetica_bold)


#Update log
def open_update_log_popup():
    popup = create_child_window("Update log")
    popup.title("Update log")
    popup.configure(bg="#262d35")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    popup_width = 768
    popup_height = 432
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    def update_log_lbl_bold(parent, row, text, font):
        label = Label(parent, text=text, bg="#262d35", fg="#8d9296", justify="left", anchor="w", font=font)
        label.grid(row=row, column=0, columnspan=2, padx=(100, 10), pady=(5, 0), sticky="NSEW")

    def update_log_lbl_regular(parent, text, row, font):
        label = Label(parent, text=text, bg="#262d35", fg="#8d9296", justify="left", anchor="w", font=font)
        label.grid(row=row, column=0, columnspan=2, padx=(20, 10), pady=5, sticky="w")

    helvetica_bold = ("Helvetica", 12, "bold")
    helvetica_regular = ("Helvetica", 12)

    # Header
    lbl_header = Label(popup, text="UPDATE LOG", font=helvetica_bold, bg="#262d35", fg="#8d9296", pady=15)
    lbl_version = Label(popup, text="Version: ", font=helvetica_bold, bg="#262d35", fg="#8d9296")


    # Popup content
    lbl_header.grid(                row=0, column=0, columnspan=2, sticky="NSEW") # Header
    lbl_version.grid(               row=1, column=0, sticky="NSEW") # Version selector
    combo.grid(                     row=1, column=1, sticky="NSEW") # Combobox
    update_log_lbl_regular(popup,   row=2, text="Added update log section in file menu.\n"
                                                "Defender class changed to protector\n"
                                                "New tags received by classes: Defender, Marksman, Archer, Crossbowman.\n"
                                                "Shaman class received name fix.\n"
                                                "Added genders: man, woman, non-binary.\n"
                                                "Pack of other smaller fixes and changes.", font=helvetica_regular)
    # v.1.03 "Added update log section in file menu.\n" "Removed Ranged role\n" "Added tags to Druid role" "Added Barbarian role"
    # v.1.04 "Added Realm tags" "Added Fantasy/medieval tags" "Added male Succubus - Incubus" "Added Monk role" "Fixed Barbarian tags"
    # "Fixed feline species" "Fixed Tiefling tags"
    # v.1.05 "Fix DnD tags" "Code optimization: naming"
    # v.1.06 "Added Devil species." "Replaced Demon species as part of Devil species." "WoW realm got new tag".
    # v.1.07 "Added Dragonborn species." "Added Skeleton species.".
    # v.1.08 "Added Tauren species."
    # v.1.09 "Fixed icon."
    # v.1.10 "Added Drow species." "Added Halfling species." "Added Gnom species." "Added Goliath species." "Added Dwarf species."
    # v.1.11 "Expanded Templar role tags."
    # v.1.12 "Complex simplify"


# Привязка строки меню к корневому окну
about = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about)
about.add_command(label="About", command=open_about_popup)
menu_bar.add_cascade(label="Update log", command=open_update_log_popup) # Сотри эту строку и верни след-следующую строку !!
#about.add_command(label="Update log", command=open_update_log_popup)

#Header
lbl_Title = Label(root, text="TAG MANAGER: 1) Choose desired tags, 2) copy generated tags, 3) clear after use. Good luck!", font=("Helvetica", 11), bg='#262d35', fg="#8d9296", anchor="w")
lbl_Title.grid(row=0, column=0, columnspan=9, padx=(20,20), sticky="NSEW")


#Input field
def input_into_entry(symbol):
    entry.insert(END, symbol)

entry = Text(root, width=70, height=3, font=('Helvetica', 15), bg='#38414a', fg="#dde4ea")
entry.grid(row=1, column=0, rowspan=3, columnspan=5, padx=20, pady=5, sticky="NSEW")


#Word count updater
def update_word_count():
    content = entry.get("1.0", "end-1c")
    words = content.split()
    num_words = len(words)
    tag_counter.config(text=f"Tag count: {num_words}")

    if num_words > 30:
        tag_counter.config(fg="#c85655")
    elif num_words == 30:
        tag_counter.config(fg="#fcd677")
    elif num_words == 0:
        tag_counter.config(fg='#8d9296')
    else:
        tag_counter.config(fg="#1EE196")

#Input field
def input_into_entry(symbol):
    entry.insert(END, symbol)
    update_word_count()  # Updating word count while adding symbol


#Label configurator
class custom_lbl(Label):
    def __init__(self, master, text, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(text=text, bg='#262d35', fg='#8d9296', font=('Helvetica', 12, 'bold'), borderwidth=1, relief='ridge')

#Grid setup
for i in range(21):
    root.grid_rowconfigure(i, weight=1)
for i in range(8):
    root.grid_columnconfigure(i, weight=1)


#Clear button
def clear():
    entry.delete("1.0", END)
    update_word_count()
btn_clear = Button(root, bg='#c85655', fg='#1f272a', text='CLEAR TAGS', font=("Helvetica", 12, "bold"), borderwidth=5, command=clear)
btn_clear.grid(row=4, column=0, columnspan=2, padx=5, pady=15, sticky="NSEW")


#Copy button
def copy_text():
    text = entry.get("1.0", "end-1c")
    root.clipboard_clear()  # Очищаем буфер обмена
    root.clipboard_append(text)  # Добавляем текст в буфер обмена
    root.update()  # Обновляем интерфейс, чтобы обновленный буфер обмена был доступен

btn_copy = Button(root, bg='#fcd677', fg='#1f272a', text='COPY TAGS', font=("Helvetica", 12, "bold"), borderwidth=5, command=copy_text)
btn_copy.grid(row=4, column=4, padx=5, pady=15, sticky="NSEW")

#Tag counter
tag_counter = Label(root, text="Tag count: 0", bg='#262d35', fg="#8d9296", font=('Helvetica', 14, "bold"))
tag_counter.grid(row=4, column=2, sticky="NSEW")


#Button configurator
class custom_btn(Button):
    def __init__(self, master, text, command, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(text=text, bg='#8d9296', fg='#1f272a', font=('Helvetica', 10, 'bold'), width=20, command=command)

btn_Recount = custom_btn(root, text='RECOUNT', command=lambda: input_into_entry(''), bg='#c85655', fg='#1f272a', font=("Helvetica", 14, "bold"), borderwidth=5)
btn_Recount.grid(row=4, column=3, pady=15, sticky="NSEW")


# Column Common
lbl_Common = custom_lbl(root, text="COMMON")
lbl_Common.grid(row=5, column=0, padx=1, pady=3, sticky="NSEW")
btn_AI = custom_btn(root, text='AI tags', command=lambda: input_into_entry('AI fantasy '))
btn_Adopt = custom_btn(root, text='Adopt', command=lambda: input_into_entry('Adopt adoptable openadobt open openadoptable digitaldrawing '))
btn_Auction = custom_btn(root, text='Auction', command=lambda: input_into_entry('Auction auc bid '))
btn_AI.grid(row=6, column=0, padx=5, sticky="NSEW")
btn_Adopt.grid(row=7, column=0, padx=5, sticky="NSEW")
btn_Auction.grid(row=8, column=0, padx=5, sticky="NSEW")

lbl_Sex = custom_lbl(root, text="SEX")
lbl_Sex.grid(row=10, column=0, padx=1, pady=3,  sticky="NSEW")
btn_Fem = custom_btn(root, text='Female', command=lambda: input_into_entry('Woman girl female '))
btn_Fem.grid(row=11, column=0, padx=5, sticky="NSEW")
btn_Mal = custom_btn(root, text='Male', command=lambda: input_into_entry('Man male '))
btn_Mal.grid(row=12, column=0, padx=5, sticky="NSEW")
btn_NB = custom_btn(root, text='Non-binary', command=lambda: input_into_entry('Nonbinary NB '))
btn_NB.grid(row=13, column=0, padx=5, sticky="NSEW")


# Column Category and Realms
lbl_Category = custom_lbl(root, text="CATEGORY")
lbl_Category.grid(row=5, column=1, padx=1, pady=3,  sticky="NSEW")
btn_ChaShe = custom_btn(root, text='Character sheet', command=lambda: input_into_entry('Character charactersheet reference referencesheet conceptart characterdesign rpg roleplay '))
btn_ChaShe.grid(row=6, column=1, padx=5, sticky="NSEW")
btn_Loc = custom_btn(root, text='Location', command=lambda: input_into_entry('Locationpreview location rpg roleplay leveldesign level Locationinterior interior '))
btn_Loc.grid(row=7, column=1, padx=5, sticky="NSEW")
btn_WalPor = custom_btn(root, text='Wallpaper portrait', command=lambda: input_into_entry('Wallpaper portrait rpg '))
btn_WalPor.grid(row=8, column=1, padx=5, sticky="NSEW")

lbl_Realms = custom_lbl(root, text="REALMS")
lbl_Realms.grid(row=10, column=1, padx=1, pady=3,  sticky="NSEW")
btn_DnD = custom_btn(root, text='Dungeon & Dragons', command=lambda: input_into_entry('dnd dungeonanddragons Forgottenrealms pathfinder '))
btn_DnD.grid(row=11, column=1, padx=5, sticky="NSEW")
btn_WoW = custom_btn(root, text='World of Warcraft', command=lambda: input_into_entry('Warcraft worldofwarcraft '))
btn_WoW.grid(row=12, column=1, padx=5, sticky="NSEW")
btn_Mod = custom_btn(root, text='Modern', command=lambda: input_into_entry('Modern '))
btn_Mod.grid(row=13, column=1, padx=5, sticky="NSEW")


#Column Specie
lbl_Specie = custom_lbl(root, text="SPECIE")
lbl_Specie.grid(row=5, column=2, padx=1, pady=3,  sticky="NSEW", columnspan=2)
btn_Avi = custom_btn(root, text='Avian', command=lambda: input_into_entry('Avian bird aarakocra kenku aven crowfolk wings anthropomorphic furry '))
btn_Avi.grid(row=6, column=2, padx=5, sticky="NSEW")
btn_OAB = custom_btn(root, text='Bear', command=lambda: input_into_entry('Bear ursus anthropomorphic furry '))
btn_OAB.grid(row=7, column=2, padx=5, sticky="NSEW")
btn_Dra = custom_btn(root, text='Dragonborn', command=lambda: input_into_entry('Dragonborn draconoid draconite dragon scalie  anthropomorphic '))
btn_Dra.grid(row=8, column=2, padx=5, sticky="NSEW")
btn_Sat = custom_btn(root, text='Draenei/Satyr', command=lambda: input_into_entry('Draenei Satyr faun sheep goat anthro anthropomorphic furry '))
btn_Sat.grid(row=9, column=2, padx=5, sticky="NSEW")
btn_Dem = custom_btn(root, text='Demons', command=lambda: input_into_entry('Demon demonic horns '))
btn_Dem.grid(row=10, column=2, padx=5, sticky="NSEW")
btn_Dwa = custom_btn(root, text='Dwarf', command=lambda: input_into_entry('Dwarf beard stocky muscled short '))
btn_Dwa.grid(row=11, column=2, padx=5, sticky="NSEW")
btn_Elf = custom_btn(root, text='Elf/Drow', command=lambda: input_into_entry('Elf drow '))
btn_Elf.grid(row=12, column=2, padx=5, sticky="NSEW")
btn_Fox = custom_btn(root, text='Fox / Kitsune', command=lambda: input_into_entry('Fox kitsune vulpera anthropomorphic furry '))
btn_Fox.grid(row=13, column=2, padx=5, sticky="NSEW")
btn_Hal = custom_btn(root, text='Halfling', command=lambda: input_into_entry('Halfling short hobbit '))
btn_Hal.grid(row=14, column=2, padx=5, sticky="NSEW")
btn_Hum = custom_btn(root, text='Human', command=lambda: input_into_entry('Human '))
btn_Hum.grid(row=15, column=2, padx=5, sticky="NSEW")
btn_OAM = custom_btn(root, text='Monkey', command=lambda: input_into_entry('Monkey gorilla orangutan chimpanzee anthropomorphic furry '))
btn_OAM.grid(row=16, column=2, padx=5, sticky="NSEW")
btn_Orc = custom_btn(root, text='Orc', command=lambda: input_into_entry('Orc goblinoid greenskin fangs '))
btn_Orc.grid(row=17, column=2, padx=5, sticky="NSEW")
btn_OCr = custom_btn(root, text='Other creatures', command=lambda: input_into_entry('Creature '))
btn_OCr.grid(row=18, column=2, padx=5, sticky="NSEW")
btn_OAR = custom_btn(root, text='Rabbit', command=lambda: input_into_entry('Rabbit hare Lagomorph anthropomorphic furry '))
btn_OAR.grid(row=6, column=3, padx=5, sticky="NSEW")
btn_Rep = custom_btn(root, text='Reptile', command=lambda: input_into_entry('Reptile lizard scalie scaly lizardman reptilian anthropomorphic '))
btn_Rep.grid(row=7, column=3, padx=5, sticky="NSEW")
btn_Rod = custom_btn(root, text='Skaven/Rodent', command=lambda: input_into_entry('Rodent skaven mouse rat anthro anthropomorphic furry '))
btn_Rod.grid(row=8, column=3, padx=5, sticky="NSEW")
btn_Ske = custom_btn(root, text='Skeleton', command=lambda: input_into_entry('Skeleton bones dead boned '))
btn_Ske.grid(row=9, column=3, padx=5, sticky="NSEW")
btn_Suc = custom_btn(root, text='Succubus/Incubus', command=lambda: input_into_entry('Succubus incubus demon horns wings tail '))
btn_Suc.grid(row=10, column=3, padx=5, sticky="NSEW")
btn_Fel = custom_btn(root, text='Tabaxi', command=lambda: input_into_entry('Tabaxi khajiit cat anthropomorphic furry '))
btn_Fel.grid(row=11, column=3, padx=5, sticky="NSEW")
btn_Tau = custom_btn(root, text='Tauren', command=lambda: input_into_entry('Tauren bull cow hooved hooves '))
btn_Tau.grid(row=12, column=3, padx=5, sticky="NSEW")
btn_Dev = custom_btn(root, text='Tiefling/Devils', command=lambda: input_into_entry('Tiefling Devil horns tail '))
btn_Dev.grid(row=13, column=3, padx=5, sticky="NSEW")
btn_Vam = custom_btn(root, text='Vampire', command=lambda: input_into_entry('Vampire fangs '))
btn_Vam.grid(row=14, column=3, padx=5, sticky="NSEW")
btn_Wer = custom_btn(root, text='Werewolf', command=lambda: input_into_entry('Werewolf wolf coyote anthropomorphic furry '))
btn_Wer.grid(row=15, column=3, padx=5, sticky="NSEW")


# Column Role
lbl_Role = custom_lbl(root, text="ROLE")
lbl_Role.grid(row=5, column=4, padx=1, pady=3,  sticky="NSEW", columnspan=1)
btn_Arc = custom_btn(root, text='Archer', command=lambda: input_into_entry('Archer bow marksman ranged '))
btn_Arc.grid(row=6, column=4, padx=5, sticky="NSEW")
btn_Bar = custom_btn(root, text='Barbarian', command=lambda: input_into_entry('Barbarian berserk warrior  muscled '))
btn_Bar.grid(row=7, column=4, padx=5, sticky="NSEW")
btn_Bar = custom_btn(root, text='Bard', command=lambda: input_into_entry('Bard minstrel '))
btn_Bar.grid(row=8, column=4, padx=5, sticky="NSEW")
btn_Def = custom_btn(root, text='Defender', command=lambda: input_into_entry('Defender shield guardian warrior melee '))
btn_Def.grid(row=9, column=4, padx=5, sticky="NSEW")
btn_Dru = custom_btn(root, text='Druid', command=lambda: input_into_entry('Druid bird haman totem '))
btn_Dru.grid(row=10, column=4, padx=5, sticky="NSEW")
btn_Kni = custom_btn(root, text='Knight', command=lambda: input_into_entry('Knight armor warrior sword '))
btn_Kni.grid(row=11, column=4, padx=5, sticky="NSEW")
btn_Mag = custom_btn(root, text='Mage', command=lambda: input_into_entry('Mage elementalist Summoner '))
btn_Mag.grid(row=12, column=4, padx=5, sticky="NSEW")
btn_Mar = custom_btn(root, text='Marksman', command=lambda: input_into_entry('Marksman gunner firearm gun rifle '))
btn_Mar.grid(row=13, column=4, padx=5, sticky="NSEW")
btn_Pri = custom_btn(root, text='Priest', command=lambda: input_into_entry('Priest divine holy saint '))
btn_Pri.grid(row=14, column=4, padx=5, sticky="NSEW")
btn_Rog = custom_btn(root, text='Rogue', command=lambda: input_into_entry('Rogue dagger knives '))
btn_Rog.grid(row=15, column=4, padx=5, sticky="NSEW")
btn_Sam = custom_btn(root, text='Samurai', command=lambda: input_into_entry('Samurai katana warrior melee '))
btn_Sam.grid(row=16, column=4, padx=5, sticky="NSEW")
btn_War = custom_btn(root, text='Warlock', command=lambda: input_into_entry('Warlock curse '))
btn_War.grid(row=17, column=4, padx=5, sticky="NSEW")
btn_Fig = custom_btn(root, text='Warrior', command=lambda: input_into_entry('Warrior sword melee '))
btn_Fig.grid(row=18, column=4, padx=5, sticky="NSEW")


center_window(root, window_width, window_height)
root.mainloop()
