# AI-LAB

**PRATICAL-01**

print("hello ! im ur cleaning robot 🤖")
print(2 + 3, "is the answer to 2 + 5")
room = ["dirty","clean","dirty","dirty","clean"]
def show_room(room):
  picture = " "
  for spot in room:
    if spot == "dirty":
      picture += "💩"
    else:
      picture += "✨"
  print(picture)

print("our room right now :")
show_room(room)

def clean_spot(spot):
  if spot == "dirty":
    return "clean"
  else:
    return "clean"

    result = clean_spot("dirty")
    print("the robot looked at a dirty spot 💩 and made it:",result,("clean ✨"))
    print("BEFORE - the dirty room:")
    def show_room(room):
      print(room)

      for i in range(len(room)):
        room[i] = clean_spot(room[i])
        print("AFTER - the clean spot number:" + str(i + 1) + ":")
        show_room(room)

  print()
  print("after - all done! ✨💩✨")
  room2 = ["dirty","clean","dirty","dirty","clean"]

  cleaned = 0
  for i in range(len(room2)):
    if room2[i] == "dirty":
      cleaned = cleaned + 1
      room2[i] = clean_spot(room2[i])

  print("the robot cleaned", cleaned, "dirty spots. ")






**PRATICAL-2**

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



  
