from collections import defaultdict
from collections import Counter
logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]
print(logs)
l=[]
user_log=defaultdict(int)
j=0
for i in logs:
    l.append(i.split())
    user_log[l[j][2]]+=1
    j+=1
print(user_log)

c = 3
recent_logs = logs[-c:] 
for i in recent_logs:
    print(i)

l=Counter()
for i in logs:
    parts = i.split()
    lev = parts[1]
    l[lev]+=1
for lev, count in l.items():
    print(f"{lev}: {count}")