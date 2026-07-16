import streamlit as st

from database.mongodb import (
    students_collection,
    attendance_collection
)

st.title("Attendance Management")

# Fetch all students
students = list(students_collection.find())

if not students:
    st.warning("No students found. Please register students first.")
    st.stop()

# Create student name list
students_names = []
for student in students:
    full_name = f"{student['first_name']} {student['last_name']}"
    students_names.append(full_name)

# Attendance Form
selected_student = st.selectbox("Select a Student", students_names)

attendance_date = st.date_input("Attendance Date")

status = st.selectbox(
    "Attendance Status",
    ["Present", "Absent"]
)

# Save Attendance
if st.button("Mark Attendance"):

    attendance_collection.insert_one({
        "student_name": selected_student,
        "date": str(attendance_date),
        "status": status
    })

    st.success("Attendance marked successfully!")

# Display Attendance Records
st.subheader("Attendance Records")

records = list(attendance_collection.find())

if records:
    for record in records:
        st.write(
            record["student_name"],
            "|",
            record["date"],
            "|",
            record["status"]
        )
else:
    st.info("No attendance records found.")

# Attendance Summary
st.subheader("Attendance Summary")

for student in students_names:

    total = attendance_collection.count_documents({
        "student_name": student
    })

    present = attendance_collection.count_documents({
        "student_name": student,
        "status": "Present"
    })

    if total > 0:
        percentage = (present / total) * 100
        st.write(f"**{student}** : {percentage:.2f}% ({present}/{total})")
    else:
        st.write(f"**{student}** : No attendance recorded")
