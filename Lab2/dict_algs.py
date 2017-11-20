def WorkersNames (Workers, age):
    filtered = []
    for worker in Workers:
        for i in range(len(worker['children'])):
            if worker['children'] [i] ['age'] > age:
                filtered.append(worker['name'])
                break
    return filtered
ivan = {
"name" : "ivan" ,
"age" : 34 ,
"children" : [{
"name" : "vasja" ,
"age" : 120 ,
}, {
"name" : "petja" ,
"age" : 100 ,
}],
}
darja = {
"name" : "darja" ,
"age" : 41 ,
"children" : [{
"name" : "kirill" ,
"age" : 210 ,
}, {
"name" : "pavel" ,
"age" : 150 ,
}],
}
emps = [ ivan , darja]
WorkersNames(emps, 18)


print(WorkersNames(emps, 18))