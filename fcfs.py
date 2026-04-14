# fcfs.py

def calculate_fcfs(processes):
    n = len(processes)

    # Add extra fields
    for p in processes:
        p["start"] = 0
        p["finish"] = 0
        p["waiting"] = 0
        p["turnaround"] = 0

    # Sort by arrival time (bubble sort - easy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if processes[j]["arrival"] > processes[j + 1]["arrival"]:
                temp = processes[j]
                processes[j] = processes[j + 1]
                processes[j + 1] = temp

    current_time = 0

    for p in processes:
        # CPU idle condition
        if current_time < p["arrival"]:
            current_time = p["arrival"]

        p["start"] = current_time
        p["finish"] = p["start"] + p["burst"]
        p["waiting"] = p["start"] - p["arrival"]
        p["turnaround"] = p["finish"] - p["arrival"]

        current_time = p["finish"]

    return processes
