import pymongo
import streamlit as st
import pandas as pd


# Connect to MongoDB
client = pymongo.MongoClient(
    "mongodb+srv://Shruti7262:Shruti224986@cluster0.veqleso.mongodb.net/"
)
db = client.sdbs


# Streamlit app title
st.title("Student Database Management System")


# Define functions for database operations
def add_student(name, roll_no, year, dept, course1, course2, course3):
    student = {
        "name": name,
        "roll_no": roll_no,
        "year": year,
        "dept": dept,
        "course1": course1,
        "course2": course2,
        "course3": course3,
    }
    db.students.insert_one(student)


def view_students():
    students = list(db.students.find())
    return students


def search_student(roll_no):
    student = db.students.find_one({"roll_no": roll_no})
    return student


# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students", "Search Student"])

if menu == "Add Student":
    st.header("Add Student")
    name = st.text_input("Name")
    roll_no = st.text_input("Roll Number")
    year = st.radio("Year", ("1st", "2nd", "3rd", "4th"))
    dept = st.selectbox(
        "Department Name",
        (
            "Automobile Engineering",
            "Civil Engineering",
            "Computer Science and Engineering",
            "Electrical and Electronics Engineering",
            "Mechanical Engineering",
            "Electronics & Communication",
            "Information Technology",
        ),
    )
    course1 = st.text_input("Course 1")
    course2 = st.text_input("Course 2")
    course3 = st.text_input("Course 3")
    if st.button("Add"):
        add_student(name, roll_no, year, dept, course1, course2, course3)
        st.success("Student added successfully!")

elif menu == "View Students":
    st.header("View Students")
    students = view_students()
    columns = [
        "Name",
        "Roll Numbee",
        "Year",
        "Department",
        "Course 1",
        "Course 2",
        "Course 3",
    ]
    data = []

    for student in students:
        data.append(
            [
                student["name"],
                student["roll_no"],
                student["year"],
                student["dept"],
                student["course1"],
                student["course2"],
                student["course3"],
            ]
        )

    df = pd.DataFrame(data, columns=columns)

    st.dataframe(df)

elif menu == "Search Student":
    st.header("Search Student")
    roll_no_to_search = st.text_input("Enter Roll Number to search")
    if st.button("Search"):
        student = search_student(roll_no_to_search)
        if student:
            st.write(
                f"Name: {student['name']}, Roll Number: {student['roll_no']},  Year: {student['year']},Department: {student['dept']}, Course 1: {student['course1']} , Course 2: {student['course2']}, Course 3: {student['course3']}"
            )
        else:
            st.warning("Student not found")
