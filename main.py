# main.py

import tkinter as tk
from fcfs import calculate_fcfs
from sjf import calculate_sjf
from rr import calculate_rr
from animation import draw_gantt

# Store processes
processes = []

# Add process
def add_process():
    pid_val = pid.get()
    at = int(arrival.get())
    bt = int(burst.get())

    processes.append({
        "pid": pid_val,
        "arrival": at,
        "burst": bt
    })

    output_text.insert(tk.END, f"Added: {pid_val}\n")

    pid.delete(0, tk.END)
    arrival.delete(0, tk.END)
    burst.delete(0, tk.END)


# FCFS button
def run_fcfs():
    if len(processes) == 0:
        return

    data = [p.copy() for p in processes]
    result = calculate_fcfs(data)

    show_output(result)
    draw_gantt(canvas, result)


# SJF button
def run_sjf():
    if len(processes) == 0:
        return

    data = [p.copy() for p in processes]
    result = calculate_sjf(data)

    # sort by start time (no lambda)
    for i in range(len(result)):
        for j in range(0, len(result)-i-1):
            if result[j]["start"] > result[j+1]["start"]:
                temp = result[j]
                result[j] = result[j+1]
                result[j+1] = temp

    show_output(result)
    draw_gantt(canvas, result)


# RR button
def run_rr():
    if len(processes) == 0:
        return

    tq = int(time_quantum.get())

    data = [p.copy() for p in processes]
    result = calculate_rr(data, tq)

    # sort by start time
    for i in range(len(result)):
        for j in range(0, len(result)-i-1):
            if result[j]["start"] > result[j+1]["start"]:
                temp = result[j]
                result[j] = result[j+1]
                result[j+1] = temp

    show_output(result)
    draw_gantt(canvas, result)


# Display results
def show_output(result):
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "PID\tWT\tTAT\n")

    for p in result:
        output_text.insert(tk.END, f"{p['pid']}\t{p['waiting']}\t{p['turnaround']}\n")


# GUI Window
root = tk.Tk()
root.title("CPU Scheduling Visualizer")
root.geometry("800x600")

# Input fields
tk.Label(root, text="PID").pack()
pid = tk.Entry(root)
pid.pack()

tk.Label(root, text="Arrival Time").pack()
arrival = tk.Entry(root)
arrival.pack()

tk.Label(root, text="Burst Time").pack()
burst = tk.Entry(root)
burst.pack()

tk.Button(root, text="Add Process", command=add_process).pack(pady=5)

# Time Quantum (for RR)
tk.Label(root, text="Time Quantum (RR)").pack()
time_quantum = tk.Entry(root)
time_quantum.pack()

# Buttons
tk.Button(root, text="Run FCFS", command=run_fcfs).pack(pady=5)
tk.Button(root, text="Run SJF", command=run_sjf).pack(pady=5)
tk.Button(root, text="Run RR", command=run_rr).pack(pady=5)

# Output
output_text = tk.Text(root, height=10)
output_text.pack()

# Canvas for animation
canvas = tk.Canvas(root, width=700, height=200, bg="white")
canvas.pack(pady=20)

root.mainloop()
