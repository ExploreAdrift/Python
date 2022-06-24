# # x = [[5, 2, 3], [10, 8, 9]]
# # students = [
# #     {'first_name':  'Michael', 'last_name': 'Jordan'},
# #     {'first_name': 'John', 'last_name': 'Rosales'}
# # ]
# # sports_directory = {
# #     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
# #     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# # }
# # z = [{'x': 10, 'y': 20}]


# # x[1][0] = 15
# # print(x)

# # students[0]['last_name'] = ('Bryant')
# # print(students)

# # sports_directory["soccer"][0] = ('Andres')
# # print(sports_directory)

# # z[0]['y'] = 30
# # print(z)

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# # def iterateDictionary(some_list):
# #     for x in range(0, len(some_list)):
# #         for key in some_list[x]:
# #             print(some_list[x][key])

# # iterateDictionary(students)


# def iterateDictionary2(key_name, some_list):
#     for i in range(0, len(some_list)):
#         print(some_list[i][key_name])


# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printInfo(some_dict):
#     for i in some_dict:
#         print(len(some_dict[i]), i.upper())
#         for l in range(0, len(some_dict[i])):
#             print(some_dict[i][l])


# printInfo(dojo)
