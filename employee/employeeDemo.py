from employee import Employee, Manager, Executive

def main():
    em = Employee("John Smith", 45000)
    print(em)
        
    m = Manager("Jane Doe", 60000, "Widgets")
    print(m)

    e = Executive("Weird Guy", 90000, "Thingies")
    print(e)

main()