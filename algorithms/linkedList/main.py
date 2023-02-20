from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.value.grade() * course.value.credit_hr()
        credits += course.value.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, len(lyst)  - 1):
        if lyst[i].value > lyst[i + 1].value:
            return False
    return True

def testInsertSList():
    numList = SList() 
    numList.insert(10)
    numList.insert(20)
    numList.insert(15)
    numList.insert(1)
    numList.insert(16)
    numList.insert(0)
    numList.insert(14)
    numList.insert(13)
    numList.insert(17)
    numList.insert(3)
    numList.insert(-5)
    numList.insert(10)
    numList.insert(16)
    numList.insert(69)
    numList.insert(420)
    print(numList)
    print(f"IS SORTED: {is_sorted(numList)}")

def testCourse():
    course1 = Course(1030, "Intro to cs", 3.0, 4.0)
    print(course1)
    
def testCalcGpa():
    
    courseList = SList()
    sum = calculate_gpa(courseList)
    
    course1 = Course(1030, "Intro to cs", 3.0, 4.0)
    course2 = Course(2420, "Algos and Data", 3.5, 4.0)
    course3 = Course(305, "Comp Ethics", 3.0, 3.5)
    
    courseList.insert(course1)
    courseList.insert(course2)
    courseList.insert(course3)
    sum = calculate_gpa(courseList)
    print(sum)
    
def testIndex():
    courseList = SList()
    course1 = Course(1030, "Intro to cs", 3.0, 4.0)
    course2 = Course(2420, "Algos and Data", 3.5, 4.0)
    course3 = Course(305, "Comp Ethics", 3.0, 3.5)
    courseList.insert(course1)
    courseList.insert(course2)
    courseList.insert(course3)
    
    print(courseList[0])
    print(courseList[1])
    print(courseList[2])
    
    print(f"Is sorted: {is_sorted(courseList)}")
    
def testRemoveSList():
    courseList = SList()
    course1 = Course(1030, "Intro to cs", 3.0, 4.0)
    course2 = Course(2420, "Algos and Data", 3.5, 4.0)
    course3 = Course(305, "Comp Ethics", 3.0, 3.5)
    courseList.insert(course1)
    courseList.insert(course2)
    courseList.insert(course3)

    print(courseList)
    courseList.remove(course2)
    print(courseList)
    print(f"IS SORTED: {is_sorted(courseList)}")
    
def testRemoveAll():
    courseList = SList()
    course1 = Course(1030, "Intro to cs", 3.0, 4.0)
    course2 = Course(2420, "Algos and Data", 3.5, 4.0)
    course3 = Course(305, "Comp Ethics", 3.0, 3.5)
    courseList.insert(course1)
    courseList.insert(course1)
    courseList.insert(course1)
    courseList.insert(course2)
    courseList.insert(course3)
    print(f"ID {id(course1)}")
    print(courseList)
    
    courseList.remove_all(course1)
    print(courseList)
    
def testFind():
    courseList = SList()
    course1 = Course(1030, "Intro to cs", 3.0, 4.0)
    course2 = Course(2420, "Algos and Data", 3.5, 4.0)
    course3 = Course(305, "Comp Ethics", 3.0, 3.5)
    course4 = 1
    courseList.insert(course1)
    courseList.insert(course2)
    courseList.insert(course3)
    print(courseList)
    print(courseList.find(course3))
    
def main():
    # testFind()
    # testRemoveAll()
    # testRemoveSList()
    # testIndex()
    testInsertSList()
    print()
    testCourse()
    print()
    testCalcGpa()
if __name__ == "__main__":
    main()