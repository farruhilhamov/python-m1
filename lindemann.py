from os import write


#class Group:
#    album = []
#    def __init__(self,group,album,song):
#        self.group = group 
#        self.album_name = album
#        self.songs = []
#    
#    def albumpacker(self):
#        self.album.append(self.song)

def main():
    file = open("albums.txt","a+")
    group = input("input group name: ")
    album = input("input album name: ")

    file.write(group+ "\n")
    file.write("|"+"\n")
    for i in range(100):
        mas = input("input your song(press enter if its end of album)")
        if mas == "":
            breaker = True

            print("quiting..")
            break
        else:
            file.write(("|"+"-"*5 + mas + "\n"))
    file.write("\n")
        

#        lin = Group(group=group,album=album,)
        
if __name__ == "__main__":
    main()