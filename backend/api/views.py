from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .db import get_connection


@api_view(["GET", "POST"])
def university(request):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM university")
        rows = cur.fetchall()
        data = [{"id": r[0], "name": r[1], "address": r[2]} for r in rows]
        cur.close()
        conn.close()
        return Response(data)
    name = request.data.get("name")
    address = request.data.get("address")
    cur.execute(
        "INSERT INTO department (name, address) VALUES (%s,%s) RETURNING *",
        [name, address],
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return Response(
        {"id": row[0], "name": row[1], "address": row[2]},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET", "PUT", "DELETE"])
def university_detail(request, id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM university WHERE id=%s", [id])
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Response({"id": row[0], "name": row[1], "address": row[2]})
        return Response({"error": "University not found"}, status=404)
    if request.method == "PUT":
        name = request.data.get("name")
        address = request.data.get("address")
        cur.execute(
            "UPDATE department SET name=%s, address=%s WHERE id=%s RETURNING *",
            [name, address, id],
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Response({"id": row[0], "name": row[1], "address": row[2]})
    cur.execute("DELETE FROM university WHERE id=%s", [id])
    conn.commit()
    cur.close()
    conn.close()
    return Response({"message": "university deleted"})


@api_view(["GET", "POST"])
def department(request):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM department")
        rows = cur.fetchall()
        data = [
            {"id": r[0], "name": r[1], "code": r[2], "university_id": r[3]}
            for r in rows
        ]
        cur.close()
        conn.close()
        return Response(data)
    name = request.data.get("name")
    code = request.data.get("code")
    university_id = request.data.get("university_id")
    cur.execute(
        "INSERT INTO department (name, code, university_id) VALUES (%s,%s,%s) RETURNING *",
        [name, code, university_id],
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return Response(
        {"id": row[0], "name": row[1], "code": row[2], "university_id": row[3]},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET", "PUT", "DELETE"])
def department_detail(request, id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM department WHERE id=%s", [id])
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Response(
                {"id": row[0], "name": row[1], "code": row[2], "university_id": row[3]}
            )
        return Response({"error": "Department not found"}, status=404)
    if request.method == "PUT":
        name = request.data.get("name")
        code = request.data.get("code")
        university_id = request.data.get("university_id")
        cur.execute(
            "UPDATE department SET name=%s, code=%s, university_id=%s WHERE id=%s RETURNING *",
            [name, code, university_id, id],
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Response(
            {"id": row[0], "name": row[1], "code": row[2], "university_id": row[3]}
        )
    cur.execute("DELETE FROM department WHERE id=%s", [id])
    conn.commit()
    cur.close()
    conn.close()
    return Response({"message": "Department deleted"})


@api_view(["GET", "POST"])
def faculty(request):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM faculty")
        rows = cur.fetchall()
        data = [
            {
                "id": r[0],
                "first_name": r[1],
                "last_name": r[2],
                "email": r[3],
                "phone": r[4],
                "department_id": r[5],
            }
            for r in rows
        ]
        cur.close()
        conn.close()
        return Response(data)
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    phone = request.data.get("phone")
    department_id = request.data.get("department_id")
    cur.execute(
        "INSERT INTO faculty (first_name,last_name,email,phone,department_id) VALUES (%s,%s,%s,%s,%s) RETURNING *",
        [first_name, last_name, email, phone, department_id],
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return Response(
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "phone": row[4],
            "department_id": row[5],
        },
        status=201,
    )


@api_view(["GET", "PUT", "DELETE"])
def faculty_detail(request, id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM faculty WHERE id=%s", [id])
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Response(
                {
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "department_id": row[5],
                }
            )
        return Response({"error": "Not found"}, status=404)
    if request.method == "PUT":
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        department_id = request.data.get("department_id")
        cur.execute(
            "UPDATE faculty SET first_name=%s,last_name=%s,email=%s,phone=%s,department_id=%s WHERE id=%s RETURNING *",
            [first_name, last_name, email, phone, department_id, id],
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Response(
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "phone": row[4],
                "department_id": row[5],
            }
        )
    cur.execute("DELETE FROM faculty WHERE id=%s", [id])
    conn.commit()
    cur.close()
    conn.close()
    return Response({"message": "Faculty deleted"})


@api_view(["GET", "POST"])
def student(request):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        data = [
            {
                "id": r[0],
                "first_name": r[1],
                "last_name": r[2],
                "email": r[3],
                "roll_number": r[4],
                "department_id": r[5],
            }
            for r in rows
        ]
        cur.close()
        conn.close()
        return Response(data)
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    roll_number = request.data.get("roll_number")
    department_id = request.data.get("department_id")
    cur.execute(
        "INSERT INTO student (first_name,last_name,email,roll_number,department_id) VALUES (%s,%s,%s,%s,%s) RETURNING *",
        [first_name, last_name, email, roll_number, department_id],
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return Response(
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "roll_number": row[4],
            "department_id": row[5],
        },
        status=201,
    )


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM student WHERE id=%s", [id])
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Response(
                {
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "roll_number": row[4],
                    "department_id": row[5],
                }
            )
        return Response({"error": "Not found"}, status=404)
    if request.method == "PUT":
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        roll_number = request.data.get("roll_number")
        department_id = request.data.get("department_id")
        cur.execute(
            "UPDATE student SET first_name=%s,last_name=%s,email=%s,roll_number=%s,department_id=%s WHERE id=%s RETURNING *",
            [first_name, last_name, email, roll_number, department_id, id],
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Response(
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "roll_number": row[4],
                "department_id": row[5],
            }
        )
    cur.execute("DELETE FROM student WHERE id=%s", [id])
    conn.commit()
    cur.close()
    conn.close()
    return Response({"message": "Student deleted"})


@api_view(["GET", "POST"])
def classroom(request):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM classroom")
        rows = cur.fetchall()
        data = [
            {"id": r[0], "room_no": r[1], "capacity": r[2], "location": r[3]}
            for r in rows
        ]
        cur.close()
        conn.close()
        return Response(data)
    room_no = request.data.get("room_no")
    capacity = request.data.get("capacity")
    location = request.data.get("location")
    cur.execute(
        "INSERT INTO classroom (room_no,capacity,location) VALUES (%s,%s,%s) RETURNING *",
        [room_no, capacity, location],
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return Response(
        {"id": row[0], "room_no": row[1], "capacity": row[2], "location": row[3]},
        status=201,
    )


@api_view(["GET", "PUT", "DELETE"])
def classroom_detail(request, id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == "GET":
        cur.execute("SELECT * FROM classroom WHERE id=%s", [id])
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Response(
                {
                    "id": row[0],
                    "room_no": row[1],
                    "capacity": row[2],
                    "location": row[3],
                }
            )
        return Response({"error": "Not found"}, status=404)
    if request.method == "PUT":
        room_no = request.data.get("room_no")
        capacity = request.data.get("capacity")
        location = request.data.get("location")
        cur.execute(
            "UPDATE classroom SET room_no=%s,capacity=%s,location=%s WHERE id=%s RETURNING *",
            [room_no, capacity, location, id],
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Response(
            {"id": row[0], "room_no": row[1], "capacity": row[2], "location": row[3]}
        )
    cur.execute("DELETE FROM classroom WHERE id=%s", [id])
    conn.commit()
    cur.close()
    conn.close()
    return Response({"message": "Classroom deleted"})
