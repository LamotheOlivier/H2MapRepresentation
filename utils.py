import ttkbootstrap as tb 
from PIL import Image, ImageTk

def jagged(slider : tb.Scale, event : any, nb_jagged : int):
    # Make a slider jagged
    # 
    # slidder :     the slider to jag
    # event :       the event of the slider
    # nb_jagged :   the number of different state

    slider_value = float(event)

    r = round(slider_value*(nb_jagged-1)) /(nb_jagged-1)
    if slider_value != r:
        slider.set(r)


def resize_image(event, canvas : tb.Canvas, image : Image.Image):

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