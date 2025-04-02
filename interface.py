# Imports
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import ImageTk, Image, ImageDraw
from utils import *


class Main_frame(tb.Frame):
     def __init__(self, master):

          tb.Frame.__init__(self,master)

          #slider frame
          bottom_frame = tb.Frame(self)
          bottom_frame.pack(side='bottom', fill='x', padx=20)
          self.scale = tb.Scale(bottom_frame,
               value=20, 
               command= lambda event : jagged(self.scale, event, 5),
               bootstyle = "warning")
          self.scale.pack(side='right', fill='x', padx = 5, pady=10, expand=True)

          self.date_label = tb.Label(bottom_frame, text="2030", font=40)
          self.date_label.pack(side='right')


          # Canvas containing the image
          map = Image.open("OccitanieMap.jpg")              #A SUPPR
          canvas = tb.Canvas(self, background= 'red')
          canvas.pack( fill='both', expand=True)
          canvas.bind('<Configure>', lambda event : resize_image(event, canvas, map))

          self.pack(side='bottom', fill='both', expand = True)

class Map_data_frame(tb.Frame):
     def __init__(self, master):

          tb.Frame.__init__(self, master)

          #slider frame
          bottom_frame = tb.Frame(self)
          bottom_frame.pack(side='bottom', fill='x', padx=20, pady = 5)

          self.download_map = tb.Button(bottom_frame, text="Télécharger les settings")
          self.download_map.pack(side='right', padx = 10)

          self.import_map_b = tb.Button(bottom_frame, text="Importer les settings")
          self.import_map_b.pack(side='right', padx = 10)

          self.save_modification = tb.Button(bottom_frame, text="Enregistrer les modifications")
          self.save_modification.pack(side='right', padx = 10)

          top_frame = tb.Frame(self)
          top_frame.pack(side='top', fill='both', padx=20, expand = True) 

          top_bot_frame = tb.Frame(top_frame)
          top_bot_frame.pack(side='bottom', fill='x', padx=20) 

          entry_start_frame = tb.Frame(top_bot_frame)
          entry_start_frame.pack(side='left', padx=20) 
          label_start = tb.Label(entry_start_frame, text="Début")
          label_start.pack(side='top')
          self.entry_start = tb.DateEntry(entry_start_frame)
          self.entry_start.pack(side='bottom')


          entry_number_frame = tb.Frame(top_bot_frame)
          entry_number_frame.pack(side='left', padx=20) 
          label_number = tb.Label(entry_number_frame, text="Nombre de Période")
          label_number.pack(side='top')
          self.entry_number = tb.Entry(entry_number_frame)
          self.entry_number.pack(side='bottom')

          entry_laps_frame = tb.Frame(top_bot_frame)
          entry_laps_frame.pack(side='left', padx=20) 
          label_lasp = tb.Label(entry_laps_frame, text="Incrément par période")
          label_lasp.pack(side='top')
          self.entry_laps_number = tb.Entry(entry_laps_frame)
          self.entry_laps_number.pack(side='left')

          self.laps_var_unit = tb.StringVar()
          self.entry_laps_menu = tb.Menubutton(entry_laps_frame, text="?")
          self.entry_laps_menu.pack(side='right')
          inside_menu = tb.Menu(self.entry_laps_menu)
          for i in ['jour', 'mois','année']:
               inside_menu.add_radiobutton(label=i, variable=self.laps_var_unit, command= lambda i=i: self.entry_laps_menu.config(text=i))
          
          self.entry_laps_menu['menu'] = inside_menu


          top_left_frame = tb.Frame(top_frame)
          top_left_frame.pack(side='left', fill='both', expand=True)
          # Canvas containing the image
          map = Image.open("OccitanieMap.jpg")              #A SUPPR
          canvas = tb.Canvas(top_left_frame, background= 'red') 
          canvas.pack(side='top', fill='both', expand=True)
          canvas.bind('<Configure>', lambda event : resize_image(event, canvas, map))

          self.import_map_image_button = tb.Button(top_left_frame, text="Changer l'image")
          self.import_map_image_button.pack(side='bottom', pady = 10)


# The class representing the interface itself
class interface:
     def __init__(self):
          #Launch the interface 
          self.root = tb.Window(themename="darkly")
          self.root.state('zoomed')

          #Button at the top
          top_frame = tb.Frame(self.root)
          top_frame.pack(side='top', fill='x')
          self.import_button = tb.Button(top_frame, text="Importer des donnés")
          self.import_button.pack(side= 'left', padx=5)
          self.map_button = tb.Button(top_frame, text="Changer la carte")
          self.map_button.pack(side= 'left', padx=5)
          self.parameter_button = tb.Button(top_frame, text="Paramètres")
          self.parameter_button.pack(side= 'left', padx=5)

          # self.main_frame = Main_frame(self.root)
          self.map_data_frame = Map_data_frame(self.root)

          self.map_data_frame.pack(side='bottom', fill='both', expand= True)

          # Launch the interface
          self.root.mainloop()