from statistics import mean, median, mode
# import statistics as s
class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    
    def __str__(self) ->str:
        return f"{self._name}  {self._grade}"
 
    def get_grade(self):
        return self._grade
    
def basic_stats(student_obj_lst):
    # return tuple containing mean, median, and mode of all grades
    # grade_list = [student.get_grade() for student in student_obj_lst]
    grade_list = []
    for student in student_obj_lst:
        grade = student.get_grade()
        grade_list.append(grade)
    grade_mean = mean(grade_list)
    grade_median = median(grade_list)
    grade_mode = mode(grade_list)
    # print(grade_mean, grade_median, grade_mode)
    return (grade_mean, grade_median, grade_mode)


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values