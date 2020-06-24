def tallest_people(**persons):
    tallest_persons = []
    for name in persons:
        if persons[name] == persons[max(persons, key=persons.get)]:
            tallest_persons.append(name)
    tallest_persons.sort()
    for name in tallest_persons:
        print(name + " : " + str(persons[name]))
