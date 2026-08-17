print("hey!Iam your Tressure Hunt Robot")
print("chumcham bey..Lets Hunt together")
map_rooms = {
    "A": [ "B" , "C"],
    "B": [ "D"],
    "C": [ "D"],
    "D": ["G"],
    "G": []

}


print("map room")
print( "       A ")
print("      //  \\")
print("      B    C")
print("      \\  //")
print("         D  ")
print("         || ")
print("         G  ")



def Tressure_hunt(start,goal):
  to_do=[start]
  visited=[]
  order=[]

  while to_do:
    room=to_do.pop(0)

    if room in visited:
      continue
    visited.append(room)
    order.append(room)
    if room == goal:
      return order
    for nxt in map_rooms[room]:
      to_do.append(nxt)
  return order
order=Tressure_hunt("A","G")
print("BFS order ",order)
print("length of path",len(order))






def Tressure_hunt(start,goal):
  to_do=[start]
  visited=[]
  order=[]

  while to_do:
    room=to_do.pop()

    if room in visited:
      continue
    visited.append(room)
    order.append(room)
    if room == goal:
      return order
    for nxt in map_rooms[room]:
      to_do.append(nxt)
  return order
order=Tressure_hunt("A","G")
print("DFS order ",order)
print("length of path",len(order))




door_cost = {
    ( "A" , "B"):1,
    ( "B" , "D"):1,
    ( "D" , "G"):1,
    ( "A" , "C"):5,
    ( "C" , "D"):1
  }
def path_cost(path):
  total=0
  for i in range(len(path) -1):
    door=(path[i],path[i+1])
    total += door_cost[door]
  return total
path1 = ["A" , "B" , "D" , "G"]
path2 = ["A",  "C" , "D" , "G"]
path1_cost = path_cost(path1)
path2_cost = path_cost(path2)
print("path1 cost",path1_cost)
print("path2 cost",path2_cost)





if path1_cost <= path2_cost:
  print("best path :",path1,"best cost :",path1_cost)
else :
  print("best path :",path2,"best cost :",path2_cost)
