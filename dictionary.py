#Create a dictionary
sample_dict = {"name": "Robert","age":14,"city":"Amsterdam"}
print(f"sample_dict = {sample_dict}\n")
#accesing values in a dictionary
print(f"sample_dict = {sample_dict["name"]}\n")
#No. of it keys only
print(f" Keys:{sample_dict.keys()}")
print(f"\n no. of items in sample|_dict = {len(sample_dict)}\n")

#get the list ofle_dict.keys()}\n")

#Add a key-value pair to the dictionary
sample_dict["profession"] = "football player"
print(sample_dict)

#change a value in the dictionary

sample_dict["age"] = 15 
print(sample_dict)

#create a nested dictionary
classroom = {
    "Student1" : {
        "name": "robert",
        "age" :"14",
        "marks":[21,9,20,17,19]
    },
    "Student2" : {
        "name" : "Simon",
        "age" :"15",
        "marks" :[15,23,5,4,90]
    }
}
print(classroom)    

print(classroom["Student1"]["age"])
