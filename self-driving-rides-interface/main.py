# @author Colin de Seroux, phenix333.dev@gmail.com

import tkinter as tk
from _decimal import Decimal, ROUND_HALF_DOWN


# Ouvrir le fichier de sortie
def draw_path(x0, y0, x1, y1, color):
    start_x = x0 * scale_factor
    start_y = (rows - y0) * scale_factor

    end_x = x1 * scale_factor
    end_y = (rows - y1) * scale_factor

    width = scale_factor / 100

    while start_x != end_x or start_y != end_y:
        if start_x < end_x:
            next_x = start_x + scale_factor
            canvas.create_line(start_x, start_y, next_x, start_y, fill=color, width=width)
            start_x = next_x
        elif start_x > end_x:
            next_x = start_x - scale_factor
            canvas.create_line(start_x, start_y, next_x, start_y, fill=color, width=width)
            start_x = next_x
        elif start_y < end_y:
            next_y = start_y + scale_factor
            canvas.create_line(start_x, start_y, start_x, next_y, fill=color, width=width)
            start_y = next_y
        elif start_y > end_y:
            next_y = start_y - scale_factor
            canvas.create_line(start_x, start_y, start_x, next_y, fill=color, width=width)
            start_y = next_y


# Ouvrir le fichier d'entrée'
with open('b.txt', 'r') as file:
    lines = file.readlines()

# Ouvrir le fichier de sortie
with open('ends_b.txt', 'r') as file:
    red_path_lines = file.readlines()

# Extraire les informations de la première ligne du fichier d'entrée
rows, columns, vehicles, trips, bonus, max_steps = map(int, lines[0].split())

# Échelle actuelle de la fenêtre
current_scale = 1.0
# Région de défilement initial
scroll_region = (0, 0, 0, 0)


# Fonction pour zoomer (agrandir)
def zoom_in():
    global current_scale
    current_scale *= 1.2
    canvas.scale('all', 0, 0, current_scale, current_scale)


# Fonction pour dé-zoomer (réduire)
def zoom_out():
    global current_scale
    current_scale /= 1.2
    canvas.scale('all', 0, 0, current_scale, current_scale)


# Fonction pour faire défiler vers la gauche
def pan_left():
    canvas.xview_scroll(-1, 'units')


# Fonction pour faire défiler vers la droite
def pan_right():
    canvas.xview_scroll(1, 'units')


# Fonction pour faire défiler vers le haut
def pan_up():
    canvas.yview_scroll(-1, 'units')


# Fonction pour faire défiler vers le bas
def pan_down():
    canvas.yview_scroll(1, 'units')


# Création de la fenêtre principale
window = tk.Tk()
window.title('Self-driving-rides')

# Calcul du facteur d'échelle en fonction de la hauteur de l'écran
scale_factor = window.winfo_screenheight() / rows
scale_factor = Decimal(scale_factor).quantize(Decimal('.01'), rounding=ROUND_HALF_DOWN)

# Création du canevas
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack()

# Associer des événements de zoom et de défilement aux touches du clavier
window.bind('<KeyPress-plus>', lambda event: zoom_in())
window.bind('<KeyPress-minus>', lambda event: zoom_out())
window.bind('<Left>', lambda event: pan_left())
window.bind('<Right>', lambda event: pan_right())
window.bind('<Up>', lambda event: pan_up())
window.bind('<Down>', lambda event: pan_down())


# Le cadrillage
# for i in range(rows + 1):
#     canvas.create_line(0, i * scale_factor, columns * scale_factor, i * scale_factor)
# for j in range(columns + 1):
#     canvas.create_line(j * scale_factor, 0, j * scale_factor, rows * scale_factor)

# Fonction pour dessiner les trajets faits
def draw_red_paths(index=0):
    if index < len(red_path_lines):
        parts = red_path_lines[index].strip().split()

        if len(parts) >= 2:
            num_trips = int(parts[0])
            for i in range(1, num_trips + 1):
                trip_num = int(parts[i])
                if trip_num < len(lines):
                    x0, y0, x1, y1, _, _ = map(int, lines[trip_num + 1].split())
                    print('x0:', x0, ', y0:', y0, ', x1:', x1, ', y1:,', y1)
                    draw_path(x0, y0, x1, y1, 'red')

        print(index)
        window.after(1, draw_red_paths, index + 1)


# Fonction pour dessiner les trajets
def trips(index=1):
    if index < len(lines):
        x0, y0, x1, y1, earliest_start, finish = map(int, lines[index].split())

        if x0 + y0 <= earliest_start:
            color = 'green'
        elif x1 + y1 > finish:
            color = 'yellow'
        else:
            color = 'blue'

        draw_path(x0, y0, x1, y1, color)
        print(index - 1)
        window.after(1, trips, index + 1)
    else:
        # Appel de la fonction pour afficher les trajets faits
        draw_red_paths()


def print_rides_not_assigned():
    rides_assigned = []

    for index in range(len(red_path_lines)):
        vehicle = red_path_lines[index].strip().split()

        if len(vehicle) >= 2:
            for i in range(len(vehicle)):
                if i != 0:
                    rides_assigned.append(int(vehicle[i]))

    rides_assigned.sort()

    last_ride_number = -1

    for ride_number in rides_assigned:
        if abs(last_ride_number - ride_number) != 1:
            for num in range(abs(last_ride_number - ride_number) - 1):
                print('Ride number:', last_ride_number + num + 1)
                x0, y0, x1, y1, earliest_start, latest_finish = map(int, lines[last_ride_number + num + 1].split())
                print('x0:', x0, ', y0:', y0, ', x1:', x1, ', y1:,', y1, ', earliest_start:', earliest_start,
                      ', latest_finish:', latest_finish)

        last_ride_number = ride_number


# Appel de la fonction pour afficher  dans la console les trajets non attribués
print_rides_not_assigned()

# Appel de la fonction pour dessiner les trajets
window.after(1000, trips)

# Appel de la fonction pour dessiner les trajets effectués (ajoutez ceci si vous souhaitez afficher uniquement les trajets effectués, sans les trajets possibles)
# window.after(1000, draw_red_paths)

# Création d'une légende pour les couleurs des trajets
legend_frame = tk.Frame(window)
legend_frame.pack()

label_reachable = tk.Label(legend_frame, text='Reachable Ride', fg='yellow')
label_reachable.grid(row=0, column=0)
label_unreachable_bonus = tk.Label(legend_frame, text='Unreachable Bonus', fg='blue')
label_unreachable_bonus.grid(row=1, column=0)
label_reachable_bonus = tk.Label(legend_frame, text='Reachable Bonus', fg='green')
label_reachable_bonus.grid(row=2, column=0)

window.mainloop()
