from sys import argv
n=int(argv[1])
import time as t
print(f"after {n} seconds ,your pc will shutdown......")
print("processing......")
t.sleep(n)
print("bye bye")
