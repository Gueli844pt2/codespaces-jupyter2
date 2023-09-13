print("hello world")
foo = ["a","b"]
foo2 = ["b","a"]
foo == foo2
foo2.sort()
foo == foo2
animals = {'dog','cat'}
type(animals)
animals2 = {'cat','dog'}
animals == animals
animals.add('turtle')
animals2.add('fish')
animals2
animals.union(animals2)
animals.intersection(animals2)
animals3 = {'cow'}
list(set(['a','b']))
list(set(['a','b','b','c']))


animals_legs['dog']
animals_legs['ant']
animals_legs['spider']
animals_legs['spider'] = 8
set(animals_legs.keys())
animals_legs.values()
legs = [4,4,4]
animals_leg_data = [('cat',4),('dog',4),('turtle',4)]
zip(animals,legs)
dict(list(zip(animals,legs)))
dict(zip(animals,legs))
animals_legs.items()
for key, value in animals_legs.items():
    print("animal: ",key, "number of legs: ", value)
data =[{'animals'}:'dog','legs']