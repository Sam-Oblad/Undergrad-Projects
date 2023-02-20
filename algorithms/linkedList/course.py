''' Course Class for Project 4 of CS 2420 '''
import typing

class Course:
    ''' Course object '''
    def __init__(self, number = 0, name = "", credit_hour = 0.0, grade = 0.0):
        if not isinstance(number, int) or number < 0:
            raise ValueError("Please enter a positive int for course num")
        if not isinstance(name, str):
            raise ValueError("Please enter a string for the course name")
        if not isinstance(credit_hour, float) or credit_hour < 0:
            raise ValueError("Please enter a positive float for credit hour")
        if not isinstance(grade, float) or grade < 0:
            raise ValueError("Please enter a positive float for credit hour")
        self.num = number
        self.class_name = name
        self.credit_hour = credit_hour
        self.class_grade = grade

    def number(self):
        return self.num
        
    def name(self):
        return self.class_name
        
    def credit_hr(self):
        return self.credit_hour
        
    def grade(self):
        return self.class_grade

    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb
      
    def __ne__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
  
    def __lt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() < cnumb
  
    def __gt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() > cnumb
  
    def __le__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() <= cnumb
  
    def __ge__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() >= cnumb
  
    def __str__(self):
        return f"cs{self.num} {self.class_name} Grade: {self.class_grade} Credit Hours: {self.credit_hour}"