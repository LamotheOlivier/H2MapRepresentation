# Imports
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import ImageTk, Image, ImageDraw

# The class representing the interface itself
class interface:


     def __jagged(slider : tb.Scale, event : any, nb_jagged : int):
          # Make a slider jagged
          # 
          # slidder :     the slider to jag
          # event :       the event of the slider
          # nb_jagged :   the number of different state

          slider_value = float(event)

          r = round(slider_value*(nb_jagged-1)) /(nb_jagged-1)
          if slider_value != r:
               slider.set(r)

     def __resize_image(event, canvas : tb.Canvas, image : Image.Image):

          # TODO : Change the image based on the date
          global resized

          width_canvas = event.width
          height_canvas = event.height

          width_image = image.width
          height_image = image.height

          w_ratio = width_canvas/width_image
          h_ratio = height_canvas/height_image

          if w_ratio < h_ratio:
               h_resi = int(height_image*w_ratio)
               resized = ImageTk.PhotoImage(image.resize((width_canvas, h_resi)))
               canvas.create_image(0,int((height_canvas - h_resi)/2), image=resized, anchor = 'nw')
          
          else:
               w_resi = int(width_image*h_ratio)
               resized = ImageTk.PhotoImage(image.resize((w_resi, height_canvas)))
               canvas.create_image(int((width_canvas - w_resi)/2),0, image=resized, anchor = 'nw')




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


          #slider frame
          bottom_frame = tb.Frame(self.root)
          bottom_frame.pack(side='bottom', fill='x', padx=20)
          self.scale = tb.Scale(bottom_frame,
               value=20, 
               command= lambda event : interface.__jagged(self.scale, event, 5),
               bootstyle = "warning")
          self.scale.pack(side='right', fill='x', padx = 5, pady=10, expand=True)


          # Canvas containing the image
          map = Image.open("OccitanieMap.jpg")              #A SUPPR
          canvas = tb.Canvas(self.root, background= 'red')
          canvas.pack( fill='both', expand=True)
          canvas.bind('<Configure>', lambda event : interface.__resize_image(event, canvas, map))

          # Launch the interface
          self.root.mainloop()