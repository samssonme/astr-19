 
 # Write a Python program that declares a class describing your favorite animal. 
# Have the data members of the class represent the following physical parameters of the animal:
#  length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail?
#  (bool), is it furry? (bool). Write an initialization function that sets the values of the data members 
# when an instance of the class is created. Write a member function of the class to print out and describe 
# the data members representing the physical characteristics of the animal.
class favorite_animal:
    def __init__(jaguar,arms_leng,legs_leng,num_eyes,has_tail,is_fury):
        jaguar.arms_leng=arms_leng #float
        jaguar.legs_leng=legs_leng #float
        jaguar.num_eyes=num_eyes   #int 
        jaguar.has_tail=has_tail   #boolean
        jaguar.is_fury=is_fury    #boolean 

    def describe(jaguar):
        print(f"the physical characteristics of the animal:")
        print(f"the arm length is: {jaguar.arms_leng} inches")
        print(f"the leg length is: {jaguar.legs_leng} inches")
        print(f"number of eyes: {jaguar.num_eyes}")
        # printing boolean 

        if jaguar.has_tail:
            print("yes, it does have tail")
        else:
            print("no")
        if  jaguar.is_fury:
            print("yes, it does have fur")
        else:
            print('no')
        
    
my_favorite_animal = favorite_animal(35.0, 45.0, 2, True, True)


my_favorite_animal.describe()
