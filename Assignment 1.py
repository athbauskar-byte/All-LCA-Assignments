studentdata_using_dict={
    1:{"Name":"Atharva Bauskar",
      "Roll number":1262260908,
      "Branch":"Computer Science and Engineering",
      "Marks":75}
}

Studentdata_using_tuple=("Atharva Bauskar",1262260908,"Computer Science and Engineering",75)

Studentdata_using_list=["Atharva Bauskar",1262260908,"Computer Science and Engineering",75]

#adding a new record to the dictionary
studentdata_using_dict[2]={"Name":"Rahul Rajput",
                           "Roll number":1262260909,
                           "Branch":"Computer Science and Engineering",
                           "Marks":80}
print(studentdata_using_dict)

#deleting a record from the dictionary
del studentdata_using_dict[1]
print(studentdata_using_dict)

#updating a record in the dictionary
studentdata_using_dict[2].update({"Marks":85})
print(studentdata_using_dict)