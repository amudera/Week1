def traffic(file_object):
    foottraffic={} #defining the data as a dictionary
    for line in file_object:
            _,room,visitors,time = line.split() #setting each parameter with a space
            if room not in foottraffic: 
                    foottraffic[room]=[0,0] #first elemet
            if visitors=='I':  # If direction is I, subtract minutes and add a visit; if O, add minutes
                    foottraffic[room][0]+=1 
                    foottraffic[room][1]+=-int(time)
            else: 
                    foottraffic[room][1]+=int(time)    
    return foottraffic

if __name__=='__main__':
    data=[]
    with open('traffic.txt','r') as text:
        data=traffic(text) #run function on text file specified
        sort=sorted(data,key=int) #sort the data by key value (Room) as an integer
    for x in sort:
            count=data[x][0] #sum of time
            mean=data[x][1]//count #average min
            print('Room {0}, {1} average minutes, {2} total visitors'.format(x,mean,count))