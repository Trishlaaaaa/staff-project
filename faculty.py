from flask import *  
import sqlite3  
  
app = Flask(__name__)


@app.route("/")  
def index():  
    return render_template("index.html"); 

@app.route("/add4")  
def add4():  
    return render_template("add4.html")

@app.route("/savecoursefacultydetails", methods = ["GET","POST"])  
def savecoursefacultydetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            EmpId = request.form["EmpId"]  
            C_no = request.form["C_no"]  

            con = sqlite3.connect('staff.db')  
            cur = con.cursor()  
            cur.execute("INSERT into Teaches (EmpId , C_no ) VALUES (?,?)",(EmpId , C_no ))  
            con.commit()  
            msg = "Faculty associated with course successfully Added"      
        except:  
            con.rollback()  
            msg = "We can not add faculty and associated course to the list"  
        finally:  
            return render_template("success4.html",msg = msg)  
            con.close()  


@app.route("/view4")  
def viewfacultywithCourse():  
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Teaches")  
    rows = cur.fetchall()  
    return render_template("view4.html",rows = rows)  

@app.route("/delete4")  
def deletefacultyCousre():  
    return render_template("delete4.html")  
 
@app.route("/deletefacultycourserecord",methods = ["POST","GET"])  
def deletefacultycourserecord(): 
    if request.method == "POST": 
        EmpId = request.form["EmpId"]  
        
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("delete from Teaches where EmpId = ? ",(EmpId,)) 
            con.commit() 
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record4.html", msg = msg)

if __name__ == "__main__":  
    app.run(debug = True)  

