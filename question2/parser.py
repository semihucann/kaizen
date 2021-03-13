import json 

## Json Load Part #####################################
with open('response.json') as json_file:
    data = open('response.json',) 
    jfile = json.load(data)
    
## Get coordinate function ############################    
def get_coordinate(node):
	vertices = i["boundingPoly"]["vertices"]

	p1 = vertices[0]
	p2 = vertices[1]
	p3 = vertices[2]
	p4 = vertices[3]

	start_x = (int((p1["x"]+p4["x"])/2))
	stop_x  = (int((p2["x"]+p3["x"])/2))

	start_y = (int((p1["y"]+p2["y"])/2))
	stop_y  = (int((p3["y"]+p4["y"])/2))

	x = [start_x,stop_x]
	y = [start_y,stop_y]
	
	ort_x =  (int((start_x+stop_x)/2))
	rounded_x =  round(ort_x/10)*10
	
	ort_y =  (int((start_y+stop_y)/2))
	ort_y =  round(ort_y/10)*10
	rounded_y = (ort_y//20)*20
	
	return rounded_x, rounded_y

### Parse Data to (Description, x, y) #################################
a = 0
parsed_data = []

for i in jfile:
	if a != 0:
		new_rounded_x, new_rounded_y = get_coordinate(i)
		value = [i["description"],new_rounded_x,new_rounded_y]
		parsed_data.append(value)
	a+=1	

##Sorting ##############################################################
sorted_data = sorted(parsed_data, key=lambda parsed_data: parsed_data[2])

##Creating txt #########################################################
last_rounded = 0
result = ""
for i in sorted_data:
	new_rounded = i[2]
	if last_rounded == new_rounded:
		result += (i[0])
		result += " "
	else:
		result += "\n"
		result += (i[0])
		result += " "
	last_rounded = new_rounded
		
print(result)
