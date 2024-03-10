
animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 
'hippopotamus', 'monkey', 'crocodile',
'bear', 'panda', 'penguin', 'kangaroo', 
'lion', 'gazelle', 'parrot', 'toucan', 
'giraffe', 'elephant','kangaroo', 'monkey']

print('')
print(animal_list)
print('')
print('<--------------------------------------------------------------------------------------------------->')
print('')

output_dictionary = {animal:animal_list.count(animal) for animal in animal_list} 
print(output_dictionary)

# output_dictionary = {x+1: animals for x, animals in enumerate(animal_list)}
# print(output_dictionary)