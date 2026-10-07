# Phase 1: Condition and Looping
## Condition 
- block of code gets executed only when condition is true, if not it will move to the next condition 
- if-elif-else
- nested if
Ex: 
age = 16
has_id = True
if age >= 18:
    print("Adult")
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")

Note: 
Multiple `if`s
→ multiple blocks CAN execute

if / elif / else
→ only ONE branch executes

## Looping
- A loop repeatedly executes a block of code while a condition remains true.
- while and for
- while(condition) :
- for in range(start, stop, step): => (start = where to begin, stop = where to stop, excluded, step = how much to move each time)
continue → skip the current iteration and move to the next iteration.
break    → leave the loop completely
pass     → Do nothing, continue normally

ex: 
for i in range(1, 10):
    if i == 6:
        break
    if i == 4:
        continue
     print(i)
print("Done")

ex: 
- this while will be have a bug, as 3 == 3, it will go back to while condition, and again ente rinto 3 == 3
i = 1
while i <= 5:
    if i == 3:
        continue
    print(i)
    i += 1

for i in range(0,5):
    if i == 3:
        continue
    print(i)