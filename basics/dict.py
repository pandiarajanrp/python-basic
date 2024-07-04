student = {"name": "Pandiarajan", "age": 25, "courses": ["react", "nodejs"]}

new_student = student  # copy as reference

student["adult"] = True

print(new_student["adult"]) # True

# accessing key
print("**** access ******")
print(student["name"])

# type check print(student['phone']) # throws KeyError
if "phone" in student:
    print(student["phone"])

# without key error
print(student.get("phone", "default value"))

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

#delete by key
student.pop("age")

#delete last item
student.popitem()
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


#delete all
student.clear()

#create with keys array
people = ["john", "smith", "loosy"]
people_dist = dict.fromkeys(people, "initial value")
print(people_dist)