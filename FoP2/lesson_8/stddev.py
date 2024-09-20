class Person:
    def __init__(self, name, age) :
        self._name = name
        self._age = age
    def __str__(self) -> str:
        return f"{self._name} {self._age}"
    def get_age(self):
        return self._age
    

def std_dev(Person_list):
    total_age = 0 
    for person in Person_list:
        total_age += person.get_age()
    # print(total_age) 
    mean = total_age / len(Person_list)
    # print(mean)
    each_num_list = []
    for person in Person_list:
        each_num = (person.get_age() - mean) ** 2
        each_num_list.append(each_num)
    # print(each_num_list)
    total = 0
    for num in each_num_list:
        total += num
    variance = total / len(each_num_list)
    # print(mean_difference_squared)
    population_std_dev = variance ** 0.5
    # print(population_std_dev)
    return population_std_dev



p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
print(p1,p2,p3)
person_list = [p1, p2, p3]
answer = std_dev(person_list)
print(answer)