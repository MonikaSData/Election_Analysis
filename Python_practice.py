counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if counties[2] != 'Jefferson':

   print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

#Getting keys in dictionary
for county in counties_dict.keys():
    print(county)
#Getting values in dictionary
for voters in counties_dict.values():
    print(voters)
#Getting keys and values in dictionary
for key, value in counties_dict.items():
    print(key, value)
#Getting keys and values in dictionary
for county, voters in counties_dict.items():
    print(county, voters)
#Printing counties and voters including a statement
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
voting_data.append({"county":"El Passo", "registered voters": 455698})

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,.2f} number of votes. "
    f"The total number of votes in the election was {total_votes:,.2f}. "
    f"You received {candidate_votes / total_votes * 100:,.2f}% of the total votes.")

print(message_to_candidate)