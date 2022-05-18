# counties = ["Arapahoe", "Denver","Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# counties = ["Arapahoe", "Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353,"Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county, voters in counties_dict.items():
#     print(county, voters)
#print(counties_dict["Arapahoe"])
#print(counties_dict.keys()[0])
#print(f"{counties_dict.key()[0]} county has {counties_dict["Arapahoe"]} registered voters" )
# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters ")

print(f"{list(counties_dict.keys())[0]} county has {counties_dict['Arapahoe']} registered voters")
