# animation.py

import time

# Draw Gantt Chart (with simple animation)
def draw_gantt(canvas, processes):
    canvas.delete("all")

    x = 50   # starting position
    y = 100  # vertical position

    for p in processes:
        width = p["burst"] * 40   # adjust size

        # Draw rectangle
        rect = canvas.create_rectangle(x, y, x + width, y + 50, fill="skyblue")

        # Process ID text
        canvas.create_text(x + width/2, y + 25, text=p["pid"])

        # Start time below
        canvas.create_text(x, y + 70, text=str(p["start"]))

        # Finish time
        canvas.create_text(x + width, y + 70, text=str(p["finish"]))

        canvas.update()
        time.sleep(0.5)  # animation delay

        x += width  # move to next position
