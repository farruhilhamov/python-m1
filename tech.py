#!/usr/bin/env/ python3

class pc():
    def cm():
        com = ["corpus","window","mouse"]
        return com
class note():
    com = pc.cm()
    def cm():
        com = note.com
        com.remove("corpus")
class plan():
    com = note.com
    note.cm()
    def cm():
        com = plan.com
        com.remove("mouse")
        com.append("touchscreen")
class smart():
    com = plan.com
    plan.cm()
    def cm():
        com = smart.com
        com.append("small size")

def main():
#action = input("pc/notebook/planshet/smartphone: ")
    device = smart.com
    print(device)

if __name__ == "__main__":
    main()