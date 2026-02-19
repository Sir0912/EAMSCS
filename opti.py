from flask import Flask, render_template, request, url_for, redirect, jsonify
import pymysql 
from datetime import datetime
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

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
    sql = "SELECT * FROM opti"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("opti_dashboard.html", ma=result)

@app.route("/log_in_admin", methods=["POST", "GET"])
def log_in_admin():
    admin = request.form.get('user_ad')
    password = request.form.get('ad_pass')

    sql = "SELECT * FROM opti_admin_db WHERE admin_name=%s AND admin_password=%s"
    cursor.execute(sql, (admin, password))
    account_found = cursor.fetchone()

    if account_found:
        return redirect(url_for('admin_log'))
    else:
        return redirect(url_for('landing_page'))


@app.route("/salary_status", methods=["POST", "GET"])
def sal_admin():
    sql = "SELECT * FROM opti"
    cursor.execute(sql)
    result1 = cursor.fetchall()
    return render_template("opti_salary.html", sm=result1)

@app.route("/employee_land")
def emp_land():
    return render_template("employee_login.html")

@app.route("/emp_dashboard", methods=["POST", "GET"])
def emp_dash():
    return render_template("employee_dashboard.html")

@app.route("/scan", methods=["POST"])
def scan():
    uid = request.json.get("uid")
    print("Received UID:", uid)

    cursor.execute("SELECT * FROM opti WHERE rfid=%s", (uid,))
    employee = cursor.fetchone()

    if not employee:
        return jsonify({"status": "not_found"})

    now = datetime.now()

    if employee["time_in"] is None:
        cursor.execute(
            "UPDATE opti SET time_in=%s WHERE rfid=%s",
            (now, uid)
        )
        connection.commit()

        # 🔥 EMIT TO ALL CONNECTED DASHBOARDS
        socketio.emit("attendance_update", {
            "name": employee["name"],
            "status": "time_in",
            "time": str(now)
        })

        return jsonify({"status": "time_in"})

    else:
        time_in = employee["time_in"]
        minutes = int((now - time_in).total_seconds() // 60)
        salary = minutes * 5

        cursor.execute(
            "UPDATE opti SET time_out=%s, salarys=%s WHERE rfid=%s",
            (now, salary, uid)
        )
        connection.commit()

        socketio.emit("attendance_update", {
            "name": employee["name"],
            "status": "time_out",
            "salary": salary
        })

        return jsonify({"status": "time_out"})

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
 