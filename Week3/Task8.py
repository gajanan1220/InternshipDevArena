import pandas as pd

student_data = {
    "StudentID": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Amit","Neha","Ravi","Pooja","Arjun","Kiran","Meena","Sachin","Anita","Rahul"],
    "Math": [78,92,65,80,55,89,72,84,90,60],
    "Science": [85,88,70,75,60,95,68,79,92,65],
    "English": [74,90,68,82,58,91,70,88,94,62]
}

data=pd.DataFrame(student_data)
print(data)