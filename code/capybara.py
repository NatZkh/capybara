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
    
    def as_list(self):
        return [self.name, self.age]

capybara1=Capybara('Dora',32)
capybara2=Capybara('Tim',24)
capybara3=Capybara('Lulu',27)
capybara4=Capybara('Nancy',37)
capybara5=Capybara('Tod',30)