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
    
    def as_row(self):
        return self.name + "," + str(self.age)




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

def longest_name_capis(listname):
    max_len = -1
    result = []
    for c in capy_list:
        if len(c.name) > max_len:
            max_len = len(c.name)
            result = [c.name]
        elif len(c.name) == max_len:
            result.append(c.name)
    
    return result

#to print not only name but full Capybara, create capybara dictionary

capy_dict = {}
for cp in capy_list:
    capy_dict[cp.name] = cp

#OR

new_capys_dic = {c.name: c for c in capy_list}


# function to find the oldest capybara in the list

def find_oldest_capi(listname):
    max_age = 0
    for c in listname:
        if c.age > max_age:
            max_age = c.age
            oldest_capi = c
    return oldest_capi

#function to find youngest capybara in the list

def find_youngest_capi(listname):
        youngest_capi = listname[0]
        for c in listname:
            if c.age < youngest_capi.age:
                youngest_capi = c
        return youngest_capi

#class which contains youngest and oldest capybara from the specified list

class CapybaraAgeExtremes:
    def __init__(self, capilist):
        self.youngest = find_youngest_capi(capilist)
        self.oldest = find_oldest_capi(capilist)
    
    def __str__(self):
        return "CapybaraAgeExtremes[" + str(self.youngest) + ", " + str(self.oldest) + "]"

#class that keeps a set of capybaras and can read and write capybaras into csv file

class CapybaraDataset:
    def __init__(self, path):
        self.capybaras = read_capis(path)
        
    def write(self, path):
        write_capybaras(path, self.capybaras)
    
    def read(self, path):
        self.capybaras = read_capis(path)
    
    def __str__(self):
        ret_val = "Name,Age\n"
        for c in self.capybaras:
            ret_val += (c.as_row() + "\n")
        return ret_val
    
    __repr__ = __str__