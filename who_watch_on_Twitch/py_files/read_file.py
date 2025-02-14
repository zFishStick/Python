import sys

path = 'py_files\\dist\\'

def get_streamers_from_file():
    streamers = []
    
    if getattr(sys, 'frozen', False):
        file = open("streamers.txt")
    else:     
        file = open(path+"streamers.txt")
    
    name = file.readlines()
    
    for x in name:
        streamers.append(x.replace('\n', ''))
    file.close()
    return streamers
    
    
# streamers = get_streamers_from_file()
# print(streamers)