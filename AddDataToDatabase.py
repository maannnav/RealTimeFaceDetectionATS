import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-224e7-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "111111":
        {
            "name":"Manav Gupta",
            "major":"Electronics",
            "starting_year":2018,
            "total_attendance":7,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2024-04-17 00:54:34"
        },
    "852741":
        {
            "name":"Emily Blunt",
            "major":"Economics",
            "starting_year":2019,
            "total_attendance":12,
            "standing":"B",
            "year":3,
            "last_attendance_time":"2024-04-17 00:54:34"
        },
    "963852":
        {
            "name":"Elon Musk",
            "major":"Physics",
            "starting_year":2020,
            "total_attendance":7,
            "standing":"G",
            "year":2,
            "last_attendance_time":"2024-04-17 00:54:34"
        },
}

for key,value in data.items():
    ref.child(key).set(value)