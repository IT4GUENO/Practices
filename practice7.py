#Add elements an one list
qualifications = [5, 3, 4, 2, 1]
names = ["Paul", "Matthew", "Logan", "Lucas", "Miranda"]
varied_list = [True, 10.5, "abc", [0,1,1]]

print("Student:", names[2])
print("qualification", qualifications[-2])
print("List within another", varied_list[3][0])
print("Print a range or slices", names[1:2])
print(varied_list)

#Add elements a one list
names.append("Josh")
print(names)

#Remove elements to list
names.remove("Lucas")
print(names)