# sjf.py

def calculate_sjf(processes):
    n = len(processes)

    # Add extra fields
    for p in processes:
        p["start"] = 0
        p["finish"] = 0
        p["waiting"] = 0
        p["turnaround"] = 0
        p["completed"] = False

    time = 0
    completed = 0

    while completed < n:
        idx = -1
        min_burst = 9999

        # Find shortest job among arrived processes
        for i in range(n):
            if processes[i]["arrival"] <= time and not processes[i]["completed"]:
                if processes[i]["burst"] < min_burst:
                    min_burst = processes[i]["burst"]
                    idx = i

        # If no process is ready → CPU idle
        if idx == -1:
            time += 1
            continue

        # Execute selected process
        p = processes[idx]

        p["start"] = time
        p["finish"] = p["start"] + p["burst"]
        p["waiting"] = p["start"] - p["arrival"]
        p["turnaround"] = p["finish"] - p["arrival"]

        time = p["finish"]
        p["completed"] = True
        completed += 1

    return processes
