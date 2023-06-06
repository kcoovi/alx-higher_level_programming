#!/usr/bin/python3
print("".join([chr(i).lower() if (i-65) % 2 == 0 else chr(i).upper() for i in range(90, 64, -1)]))
