input_file=open('input.txt','r')
array=input_file.readlines()


elist=[]
for i in array[1:]:
    elist+=[i.split()]
       
c_dict={}

for i in elist:
    c_dict[i[0]]=i[1:]
      
def Is_Bipartite(graph,source):
    queue=[]
    colour={}
    for i in graph:
        colour[i]='white'
    queue.append(source)
    
    while len(queue)!=0:
        m=queue.pop(0)
        for neighbor in graph[m]:
            if colour[neighbor]=='white':
                if colour[m]=='red':
                    colour[neighbor]='green'
                else:
                    colour[neighbor]='red'
                queue.append(neighbor)
            elif colour[neighbor]==colour[m]:
                return 'Not Bipartite'
    return 'Bipartite'
                
        

output=Is_Bipartite(c_dict,'a')
print(output)
input_file.close()