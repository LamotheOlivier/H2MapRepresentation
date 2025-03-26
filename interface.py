# Imports
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import ImageTk, Image, ImageDraw



def __jagged(slider, event, nb_jagged):
        # Make a slider jagged

        # slidder :     the slider to jag
        # event :       the event of the slider
        # nb_jagged :   the number of different state

        round = int(float(event)*(nb_jagged-1)) /(nb_jagged-1)
        if float(event) != round:
            slider.set(round)

def modify(image : Image):
     draw = ImageDraw.Draw(image)
     draw.rectangle([(10,10), (40,40)], fill ="#ffff33")


def interface():
    #Launch the interface 
    

    root = tb.Window(themename="darkly")
    root.geometry('1000x1000')

    map = Image.open("OccitanieMap.jpg")
    maptk = ImageTk.PhotoImage(map)

    label_img = tb.Label(image=maptk)
    label_img.pack(side='top', pady = 5)

    sc = tb.Scale(
         value=20, 
         command= lambda event : __jagged(sc, event, 5),
         bootstyle = "warning")
    sc.pack(side='bottom', padx = 5, pady=10)

    bt = tb.Button(root, text="wesh", command= lambda : modify(map))
    bt.pack(side='bottom', padx = 5, pady=10)


    # Launch the interface
    root.mainloop()