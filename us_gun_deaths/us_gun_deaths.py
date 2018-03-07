import csv
import datetime as d

# data import
f = open("guns.csv", "r")
data = list(csv.reader(f))

# erasing header row
headers = data[0]
data = data[1:]

# showing first five rows
print("First five rows: ", data[0:5])

# taking column with years
years = [item[1] for item in data]

# counting deaths per year
year_counts = {}

for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

print("Deaths per year: ", year_counts)

# counting deaths per year-month
dates = [d.datetime(year=int(item[1]), month=int(item[2]), day=1) for item in data]

date_counts = {}

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1

print("Deaths per year and month: ", date_counts)

# counting deaths per sex
sex = [item[5] for item in data]

sex_counts = {}

for item in sex:
    if item in sex_counts:
        sex_counts[item] += 1
    else:
        sex_counts[item] = 1

print("Deaths per sex: ", sex_counts)

# counting deaths per race
races = [item[7] for item in data]

race_counts = {}

for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

print("Deaths per race: ", race_counts)

# importing data with population size
g = open("census.csv", "r")
census = list(csv.reader(g))

# creating map, which translates races from file with deaths to races from file about population size
mapping = {"Asian/Pacific Islander": int(census[1][15]) + int(census[1][16]),
           "Black": int(census[1][13]),
           "Hispanic": int(census[1][12]),
           "Native American/Native Alaskan": int(census[1][14]),
           "White": int(census[1][11])}

# counting death ratio for each race
race_per_hundred = {}

for race, count in race_counts.items():
    race_per_hundred[race] = count / mapping[race] * 100000

print("Deaths ratio per race: ", race_per_hundred)

# taking column with intents
intents = [item[3] for item in data]

# counting deaths (homicide only) for each race
homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1

print("Deaths (homicide) per race: ", homicide_race_counts)

# counting death ratio (as homicide) for each race
race_per_hundred_hom = {}

for race, count in homicide_race_counts.items():
    race_per_hundred_hom[race] = count / mapping[race] * 100000

print("Deaths ratio (homicide) per race: ", race_per_hundred_hom)


def death_count(input_data, intent_str, intents_ind, features_ind):
    features = [item[features_ind] for item in input_data]
    intent_feature_counts = {}

    if intent_str is None:
        for feature in features:
            if feature in intent_feature_counts:
                intent_feature_counts[feature] += 1
            else:
                intent_feature_counts[feature] = 1
    else:
        intents = [item[intents_ind] for item in input_data]

        for i, feature in enumerate(features):
            if intents[i] == intent_str:
                if feature in intent_feature_counts:
                    intent_feature_counts[feature] += 1
                else:
                    intent_feature_counts[feature] = 1

    return intent_feature_counts


# counting deaths (as homicide) for each month
homicide_month_counts = death_count(input_data=data, intent_str="Homicide", intents_ind=3, features_ind=2)
print("Deaths (homicide) per month: ", homicide_month_counts)

# counting deaths (as homicide) for each sex
homicide_sex_counts = death_count(input_data=data, intent_str="Homicide", intents_ind=3, features_ind=5)
print("Deaths (homicide) per sex: ", homicide_sex_counts)

# counting deaths (as accidents) for each race
accidental_race_counts = death_count(input_data=data, intent_str="Accidental", intents_ind=3, features_ind=7)
print("Deaths (accidental) per race: ", accidental_race_counts)

# counting deaths (as accidents) for each sex
accidental_sex_counts = death_count(input_data=data, intent_str="Accidental", intents_ind=3, features_ind=5)
print("Deaths (accidental) per sex: ", accidental_sex_counts)

# counting deaths for each educational level:
edu_counts = death_count(input_data=data, intent_str=None, intents_ind=3, features_ind=10)
print("Deaths per educational level: ", edu_counts)

# counting deaths for each location:
location_counts = death_count(input_data=data, intent_str=None, intents_ind=3, features_ind=9)
print("Deaths per location: ", location_counts)