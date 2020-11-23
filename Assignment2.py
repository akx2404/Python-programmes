def group_list(group, users):
  members = ""
  for i in range(len(users)):
      if i< len(users)-1:
          members = members + users[i] + ", "
      else:
          members = members + users[i] + ""

  return  "{}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
