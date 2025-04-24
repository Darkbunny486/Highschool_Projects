lockers = []
for a in range (1000):
    lockers = lockers + ["open"]


for b in range (2, 1000, 2):
    lockers.pop (b)
    lockers.insert (b, "close")

for c in range (3, 1000, 3):
    if (lockers[c] == "open"):
        lockers.pop (c)
        lockers.insert (c, "close")
    else:
        lockers.pop (c)
        lockers.insert (c, "open")


for e in range (4, 1000):
    for d in range (e, 100, e):
        if (lockers[c] == "open"):
            lockers.pop (c)
            lockers.insert (c, "close")
        else:
            lockers.pop (c)
            lockers.insert (c, "open")

opens = 0
close = 0
for f in range (1000):
    if (lockers[f] == "open"):
        opens += 1
    else:
        close += 1

print (opens, close)