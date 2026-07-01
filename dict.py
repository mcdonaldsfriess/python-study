scores = {"Alice": 90, "Bob": 85}
a = scores["Alice"] 



d = {"a": 1, "b":2}

d["c"] = 3 #add

d["a"] = 10 #update(same ass add)
del d["b"] #delete
"a" in d # exists -> True
len(d) # count -> 2


d["NotKey"] # KeyError: 'NotKey', In java gives us null, in python, its an exception
d.get("NotKey") # None (default), This is Java's null
d.get("NotKey", 0) # 0 (default)
#if you are unsure about key, use .get()


for k in d: # iterate only over key. not valuse nor entry
    print(k)

for k, v in d.items(): # iterate both key + value 
    print(k, v)

for v in d.values(): # iterate only over values
    print(v)


#ex
subjects = {
    "Calculus 2": {
        "Integration Techniques": ["Partial Fractions", "Integration by Parts"],
        "Series": ["Taylor Series", "Ratio Test"],
    },
    "Calculus 1": { 
       "Derivatives": ["Chain Rule", "Product Rule"],
    },
}

subjects["Calculus 2"]["Series"] # ['Taylor Series', 'Ratio Test']