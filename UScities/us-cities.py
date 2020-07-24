
import tkinter
import time



CANVAS_WIDTH = 1000;
CANVAS_HEIGHT = 750;

MIN_LONGITUDE = -130;
MAX_LONGITUDE = -60;
MIN_LATITUDE = +22;
MAX_LATITUDE = +55;

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'US CITIES')
    n_done = 0
    with open("us-cities.txt") as cities_file:
        next(cities_file)

        for line in cities_file:
            line = line[:-1]
            parts = line.split(',')

            lat = float(parts[2])
            long = float(parts[3])
            plot_one_city(canvas, lat, long)

            n_done += 1
            if n_done % 100 == 0:
                canvas.update()
                time.sleep(1/50)


    canvas.mainloop()

def plot_one_city(canvas, latitude, longitude):
     # plots the city depending on latitude and longitude
    x = longitude_to_x(longitude)
    y = latitude_to_y(latitude)
    plot_pixel(canvas, x, y)



def plot_pixel(canvas, x, y):
    # creates the physical dot
    canvas.create_rectangle(x, y, x + 1, y + 1, fill = 'blue', outline = 'blue')



def longitude_to_x(longitude):
    long = CANVAS_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)
    return long



def latitude_to_y(latitude):
    lat = CANVAS_HEIGHT * (1.0 - (latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE))
    return lat




def make_canvas(width,height, title = None):
    top = tkinter.Tk()
    top.minsize(width = width, height = height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width = width + 1, height = height + 1)
    canvas.pack()
    return canvas




if __name__ == '__main__':
    main()
