"""
PyLab 19 March 2016
Analyzing JSON and US Passport Data with python3
Valid passportIssuanceByCalendarYear
https://catalog.data.gov/dataset/passportissuancebycalendaryear
"""

#### Imports
import arcpy
import os    #
import json  #
try:  #tries something, and if doesn't work, then do the except
    from urllib.request import urlopen ## python3

except ImportError:  #excepts the error
    print('python2 alert')
    from urllib import urlopen ## python2

### Constants

# url = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:56:10.098Z/validpassportsbyyear.json'
# validpassport_json = 'validpassportsbyyear.json'

# if not os.path.isfile(validpassport_json):  #if file does not yet exist
#     with urlopen(url) as f:  #opening the url and assigning it as f
#         text = f.read()  #read that opened url
#         decoded_text = text.decode('utf8')
#         data =  json.loads(decoded_text)
#     print('Requested JSON and converted to python dictionary')

#     with open(validpassport_json, 'w+') as f:  #with means that it's only open until it is fininshed.  can this be used with other connections, like odbc? w+ writes
#         json.dump(data, f)
#     print('Saved JSON to file')

# else:
#     with open(validpassport_json, 'r+') as f:  #r+ means read
#         data = json.load(f)
#     print('File {fn} opened. Time to get to work.'.format(fn=validpassport_json))

# print(type(data[0].keys()))

# ### Questions


# ### What data type is 'data'? What operations can we do on it?
# #List


# ### How many years are in this dataset?
# print(len(data)) #24


# ### What is the total number of passports issues in this data set?
# sum = 0
# index = 1
# for year in data:
#     sum += year['Count']
#     print(year['Year'])
#     index += 1
# print(sum)

# ### What is number of passports issues in the last ten years? What is the average number issued per year since then?
# print(sum / len(data))

# last_ten_sum = 0
# for year in data:
#     if year['Year'] >= 2002:
#         last_ten_sum += year['Count']
# print(last_ten_sum)

# ### Since 2001, has the average number of passports increased or decreased since then?
# sum_2001 = 0
# sum_before_2001 = 0
# index_2001 = 0
# index_non_2001 = 0
# for year in data:
#     if year['Year'] > 2001:
#         sum_2001 += year['Count']
#         index_2001 += 1
#     else:
#         sum_before_2001 += year['Count']
#         index_non_2001 += 1
# if sum_2001 >  sum_before_2001:
#     print('2001 has a higher average')
# else:
#     print('2001 has a lower average')



# # PART II

# """
# USAcceptanceFacilities for passports
# https://catalog.data.gov/dataset/usacceptancefacilities
# """

# url2 = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:52:39.651Z/facilities.json'


# ### Write a small script to save this json file to a file. (hint look at code above)
# ### Advanced: can you write this script as a function? (code reuser)
# url = 'https://cadatacatalog.state.gov/storage/f/2013-11-24T20:52:39.651Z/facilities.json'
# validpassport_json = 'usacceptancefacilities.json'

def url_json(url, filepath):
    if not os.path.isfile(filepath):  #if file does not yet exist
        with urlopen(url) as f:  #opening the url and assigning it as f
            text = f.read()  #read that opened url
            decoded_text = text.decode('utf8')
            data =  json.loads(decoded_text)
        print('Requested JSON and converted to python dictionary')

        with open(filepath, 'w+') as f:  #with means that it's only open until it is fininshed.  can this be used with other connections, like odbc? w+ writes
            json.dump(data, f)
        print('Saved JSON to file')

    else:
        with open(filepath, 'r+') as f:  #r+ means read
            data = json.load(f)

        print('File {fn} opened. Time to get to work.'.format(fn=filepath))
    return data


data = url_json('https://cadatacatalog.state.gov/storage/f/2013-11-24T20:52:39.651Z/facilities.json', 'usacceptancefacilities.json')

### How many facilities are in this dataset?
print(data[0])

### How many states?
states = []
for entry in data:
    if entry['StateCode'] not in states:
        states.append(entry['StateCode'])
# print(states)
# print(len(states))

### Ask a question of this data.


### can you convert this to a csv file and create a map using Google maps?
### https://www.google.com/maps/d/u/0/?hl=en_US&app=mp

# Brandon Rhodes Tutorial for Pandas