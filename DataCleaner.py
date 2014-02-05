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

for person in people:
    v = person['randReal']
    print(v)
    print(float(v))
