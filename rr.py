# rr.py

def calculate_rr(processes, time_quantum):
    n = len(processes)

    # Add extra fields
    for p in processes:
        p["remaining"] = p["burst"]
        p["start"] = -1
        p["finish"] = 0
        p["waiting"] = 0
        p["turnaround"] = 0

    # Sort by arrival time (bubble sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if processes[j]["arrival"] > processes[j + 1]["arrival"]:
                temp = processes[j]
                processes[j] = processes[j + 1]
                processes[j + 1] = temp

    time = 0
    queue = []
    i = 0
    completed = 0

    while completed < n:

        # Add arrived processes
        while i < n and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        # CPU idle
        if len(queue) == 0:
            time += 1
            continue

        current = queue.pop(0)

        # First start
        if current["start"] == -1:
            current["start"] = time

        # Execute
        if current["remaining"] > time_quantum:
            time += time_quantum
            current["remaining"] -= time_quantum
        else:
            time += current["remaining"]
            current["remaining"] = 0

        # Add new arrivals
        while i < n and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        # Not finished
        if current["remaining"] > 0:
            queue.append(current)
        else:
            current["finish"] = time
            current["turnaround"] = current["finish"] - current["arrival"]
            current["waiting"] = current["turnaround"] - current["burst"]
            completed += 1

    return processes
