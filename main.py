"""Say What Actually Broke — entry for make.fun.

Writes one error line to /output/entry.txt.
The line is one error message, under 200 characters, telling the brutal truth and making the user laugh.
"""
import os

LINE = "Something broke, and it was the update you installed five minutes ago. Undo it, restart, and we will pretend this never happened."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
