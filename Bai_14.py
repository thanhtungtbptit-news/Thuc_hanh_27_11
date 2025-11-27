value=[(1,2),(3,4),(5,6)]
value_x=[t[0] for t in value]
value_y=[t[1] for t in value]

x=sum(value_x)/len(value_x)
y=sum(value_y)/len(value_y)

print("Trung bình x : ",x)
print("Trung bình y : ",y)