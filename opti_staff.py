from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_socketio import SocketIO
from flask import session
from datetime import datetime, date
import pymysql

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "blackpower"

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Myservermybestfriend09941991294",
    database = "opti_db",
    cursorclass=pymysql.cursors.DictCursor
)
cursor=connection.cursor()

@app.route("/")
def landing_page():
    return render_template("opti_pass.html")

@app.route("/admin_dashboard", methods=["POST","GET"])
def admin_log():
    if "admin" not in session:
        return redirect(url_for("landing_page"))

    today = datetime.now().strftime("%Y-%m-%d")  # FIXED date format

    sql = (
        "SELECT opti.name, opti_rec.time_in, opti_rec.time_out "
        "FROM opti_rec "
        "JOIN opti ON opti_rec.id_employee = opti.id_employee "
        "WHERE DATE(opti_rec.time_in) = %s "
        "ORDER BY opti_rec.time_in DESC"
    )

    cursor.execute(sql, (today, ))  
    records = cursor.fetchall()

    return render_template("opti_dashboard.html", ma=records)

@app.route("/salary_status", methods=["POST", "GET"])
def sal_admin():
    if "admin" not in session:
        return redirect(url_for("landing_page"))

    today = datetime.now().strftime("%Y-%m-%d")

    sql = (
        "SELECT opti.name, opti_rec.time_in, opti_rec.time_out, "
        "opti_rec.duration, opti_rec.salary "
        "FROM opti_rec "
        "JOIN opti ON opti_rec.id_employee = opti.id_employee "
        "WHERE DATE(opti_rec.time_in) = %s "
        "ORDER BY opti_rec.time_in DESC"
    )

    cursor.execute(sql, (today,))
    records = cursor.fetchall()

    return render_template("opti_salary.html", sm=records)

@app.route("/scan", methods=["POST"])
def scan():
    uid = request.json.get("uid")

    # Check RFID
    cursor.execute("SELECT * FROM opti WHERE rfid=%s", (uid,))
    employee = cursor.fetchone()
    if not employee:
        return jsonify({"status": "not_found"})

    now = datetime.now()

    # Check today's record
    now_str = now.strftime("%Y-%m-%d")
    cursor.execute(
        "SELECT * FROM opti_rec WHERE id_employee=%s AND DATE(time_in)=%s",
        (employee["id_employee"], now_str)
    )
    record = cursor.fetchone()

    # First scan → Time In
    if not record:
        cursor.execute(
            "INSERT INTO opti_rec (id_employee, time_in) VALUES (%s, %s)",
            (employee["id_employee"], now)
        )
        connection.commit()

        # Emit real-time attendance
        socketio.emit("attendance_update", {
            "name": employee["name"],
            "status": "time_in",
            "time": now.strftime("%Y-%m-%d %I:%M %p"),
            "duration": "0h 0m",
            "salary": 0
        })

        return jsonify({
            "status": "time_in",
            "time": now.strftime("%Y-%m-%d %I:%M %p")
        })

    # Second scan → Time Out
    elif record and not record["time_out"]:
        time_in_db = record["time_in"]
        if isinstance(time_in_db, str):
            time_in_db = datetime.strptime(time_in_db, "%Y-%m-%d %H:%M:%S")

        duration_min = int((now - time_in_db).total_seconds() // 60)
        salary = duration_min * 5

        cursor.execute(
            "UPDATE opti_rec SET time_out=%s, duration=%s, salary=%s WHERE id=%s",
            (now, duration_min, salary, record["id"])
        )
        connection.commit()

        # Convert duration to h m format
        hours = duration_min // 60
        minutes = duration_min % 60
        duration_str = f"{hours}h {minutes}m"

        # Emit real-time attendance & salary update
        socketio.emit("attendance_update", {
            "name": employee["name"],
            "status": "time_out",
            "time": now.strftime("%Y-%m-%d %I:%M %p"),
            "duration": duration_str,
            "salary": salary
        })

        return jsonify({
            "status": "time_out",
            "time": now.strftime("%Y-%m-%d %I:%M %p"),
            "duration": duration_str,
            "salary": salary
        })

    else:
        return jsonify({"status": "already_done"})
@app.route("/log_in_admin", methods=["POST", "GET"])
def log_in_admin():
    admin = request.form.get('user_ad')
    password = request.form.get('ad_pass')

    sql = "SELECT * FROM opti_admin_db WHERE admin_name=%s AND admin_password=%s"
    cursor.execute(sql, (admin, password))
    acc_f = cursor.fetchone()

    if acc_f:
        session["admin"] = admin
        return redirect(url_for('admin_log'))
    else:
        return redirect(url_for('landing_page'))

@app.route("/add_drop", methods=["POST", "GET"])
def add_drop():
    sql = "SELECT * FROM opti"
    cursor.execute(sql)
    result_em = cursor.fetchall()
    return render_template("add_drop.html", e=result_em)

@app.route("/add", methods=["POST", "GET"])
def add():
    name = request.form.get('name_inp')
    age = request.form.get('age_inp')
    sex = request.form.get('sex_inp')
    email = request.form.get('email_inp')
    num = request.form.get("num_inp")
    rfid = request.form.get('rfid_inp')

    sql = "INSERT INTO opti (name, age, sex, email, number, rfid) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (name, age, sex, email, num, rfid))
    connection.commit()

    return redirect(url_for('add_drop'))

@app.route("/drop_con", methods=["POST", "GET"])
def drop_con():
    btn = request.form.get("act_btn")
    print(btn)

    if btn == "upd_btn":
        print("SHIT")
    else:
        employ = request.form.get("em")
        sql = "DELETE FROM opti WHERE id_employee=%s"
        cursor.execute(sql, (employ, ))
        connection.commit()
        return redirect(url_for("add_drop"))


@app.route("/list", methods=["POST", "GET"])
def list_admin():
    sql = "SELECT * FROM opti"
    cursor.execute(sql) 
    result = cursor.fetchall()
    return render_template("list.html", li = result)




@app.route("/employee_land")
def emp_land():
    return render_template("employee_login.html")

@app.route("/emp_dashboard", methods=["POST", "GET"])
def emp_dash():
    return render_template("employee_dashboard.html")

@app.route("/app_link", methods=["POST", "GET"])
def link_app():
    emp = request.form.get('email')
    emp_pass = request.form.get('password')
    sql = "SELECT * FROM opti WHERE email=%s AND password=%s"
    cursor.execute(sql, (emp, emp_pass))
    account_found = cursor.fetchone()

    if account_found:
        return redirect(url_for("emp_dash"))
    
    else:
        return redirect(url_for("emp_land"))

if __name__ == "__main__":
    socketio.run(app, port=5000)
