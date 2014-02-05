#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
f = open ("Datamining2012/survey.csv")
titles = []
first_line = True
people = []

def heading(line):
    titles = line.split(';')
    return titles

def parse(line,titles):
    values = line.split(';')
    person = {}
    for i,value in enumerate(values):
        person[titles[i]] = values[i]
    return person
        
for line in f:
    if first_line:
        titles = heading(line)
        first_line = False
    else:
        people.append(parse(line,titles))
f.close()

def clean_float(v):
    v = v.replace(',','.')
    v = v.replace('?','')
    v = v.replace("π",'3.14')
    try :
        return float(v)
    except :
        return "Error: " + v

def clean_int(v):
    v = v.replace(',','.')
    v = v.replace('?','')
    try :
        return int(v)
    except :
        return "Error: " + v

def clean_string(v):
    return v

def clean_bool(v):
    v = v.upper()
    if re.match('YES',v):
        return True
    if re.match('NO',v):
        return False
    return "Error: " + v

types = {'randReal': clean_float, 'yearsUniversity': clean_float, 'randInt': clean_int, 'ann': clean_string, 'englishSpeaker': clean_int, 'therbfortt': clean_string, 'danishMountains': clean_bool, 'solarSystem\n': clean_int, 'programmingSkill': clean_int, 'togelius': clean_string, 'apriori': clean_bool, 'favAnimal': clean_string, 'canteenFood': clean_string, 'favSQLServ': clean_string, 'sqrt': clean_float, 'yannakakis': clean_string, 'fedUpWWinter': clean_bool, 'sql': clean_string, 'favProgLang': clean_string, 'randReal2': clean_float, 'svm': clean_bool, 'age': clean_int, 'favColour': clean_string, 'favOS': clean_string}

#for person in people:
for person in people:
    for k, v in person.iteritems():
        person[k] = types[k](v)

#CLEAN DONE.

print(people)
