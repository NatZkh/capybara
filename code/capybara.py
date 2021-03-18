import csv

#define Capybara class with two attributes - name and age
class Capybara:
    def __init__(self,name,age):
        self.name=name
        self.age=int(age)
    
    def greet(self,othername):
        print("Hello "+othername+"!")
        print("I am "+self.name+" the Capybara.")
        print("I am "+str(self.age)+" years old.")
    
    def __iter__(self):
        return self.as_list().__iter__()
    
    def level_up(self):
        self.age=self.age+1
        
    def level_down(self):
        self.age=self.age-1
    
    def __str__(self):
        return "Capybara(" + self.name + ", " + str(self.age) + ")"
    
    __repr__ = __str__

    def as_list(self):
        return [self.name, self.age]

capybara1=Capybara('Dora',32)
capybara2=Capybara('Tim',24)
capybara3=Capybara('Lulu',27)
capybara4=Capybara('Nancy',37)
capybara5=Capybara('Tod',30)
capybara6=Capybara('Paddy',20)

#read_capis function to extract capybara from csv into list
def read_capis(filename):
    with open(filename,'r',newline='') as file:
        reader=csv.reader(file)
        capis = []
        next(reader)
        for row in reader:
            capis.append(Capybara(row[0], row[1]))
    return capis


#function write_capybaras that creates capybara csv
def write_capybaras(filename, capis):
    with open(filename,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        writer.writerows(capis)


#final way to get the list of capybaras with longest name
capy_list = [capybara1, capybara2, capybara3, capybara4, capybara5, capybara6]

max_len = -1
result = []
for c in capy_list:
    if len(c.name) > max_len:
        max_len = len(c.name)
        result = [c.name]
    elif len(c.name) == max_len:
        result.append(c.name)
    
print(result)

#to print not only name but full Capybara, create capybara dictionary

capy_dict = {}
for cp in capy_list:
    capy_dict[cp.name] = cp

#OR

new_capys_dic = {c.name: c for c in capy_list}

#then

for v in result:
    print(capy_dict[v])

