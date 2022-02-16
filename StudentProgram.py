from datetime import datetime
import StudentClass as st

#mystu = st.Student()
def main():
    studentid = input("What is your student ID?")
    dateob = int(input("What year were you born?"))
    name = input("What is your name?")
    classif = input("What is your classification?")

    st1 = st.Student(studentid,name,dateob,classif)
    st1.age()
    print("The students age is:", st1.get_age())

    st1.registrate()

main()
