student = {"name": "Pandiarajan", "age": 25, "courses": ["react", "nodejs"]}

new_student = student  # copy as reference

student["adult"] = True

print(new_student)

# accessing key
print("**** access ******")
print(student["name"])
# print(student['phone']) # throws KeyError
if "phone" in student:
    print(student["phone"])
print(student.get("phone"))

# set values
print("**** set value ******")
student["name"] = "Pandiarajan Rajagopal"
print(student)

student.update({"name": "Pandiarajan R", "address": ["tamilnadu", "india"]})
print(student)
print(new_student)

# get length
print("**** length ******")
print(len(student))

# delete an item
print("**** delete ******")

del student["address"]
print(student)

# clone
print("**** clone ******")
new_student1 = dict(student)
new_student2 = student.copy()
student["name"] = "Pandi"
print(new_student1)
print(new_student2)

# looping each item
for key in student:
  print("key ::: " + key)

for key in student.keys():
  print("key ::: " + key)

for value in student.values():
  print("value ::: " + str(value))

for key, value in student.items():
  print("key ::: " + key)
  print("value ::: " + str(value))
