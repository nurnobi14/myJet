class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins can swimming")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
print('\n\n first print end') 
obj_parr.intro()
obj_parr.flight()
print('\n\n first print end') 
obj_peng.intro()
obj_peng.flight()
print('\n\n first print end') 