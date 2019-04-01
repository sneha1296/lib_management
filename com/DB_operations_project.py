import employee_operations as emp
import student_operations as stu
import sqlite3 as db
import tkMessageBox as tkmsg
def getConnection():
    global conn
    conn=db.connect("stpproject.db")

#getConnection()


def loginValidate(uid,password):
    getConnection()
    c = conn.cursor()
    try:
        c.execute("select count(*),role from login where lid='%s' and pass ='%s'"%(uid,password))
        rcount=c.fetchone()
        #print rcount[0],rcount[1]

        if rcount[0] == 1:
            return rcount[1]
        else:
            return  False
    except Exception, e:
        print(e)
    finally:
        conn.close()

#dbo.register_student(nm, id1, dep, date, s,p)
def register_newemployee (name,eid,dept,doj,sal,p):
    getConnection()
    c = conn.cursor()
    reg_type = "employee"
    v1 = (name,eid,dept,doj,sal,)
    v2 = (eid,p,reg_type,name,)
    try:
        c.execute("insert into empdetail values(?,?,?,?,?)",v1)
        c.execute("insert into login values(?,?,?,?)", v2)
        tkmsg.showinfo("REGISTRATION", "Employee Registered  Successfully")
    except Exception,e:
        tkmsg.showinfo("REGISTRATION", e)

    finally:
        conn.commit()
        conn.close()


def register_student(n,r,dep,sem,bat):
    getConnection()
    c = conn.cursor()
    reg_type="student"
    v1=(n, r, dep, sem, bat,)
    v2=(r,  reg_type, n)
    try:
        c.execute("insert into studetail values(?,?,?,?,?)",v1)
        c.execute("insert into login values(?,?,?)", v2)

        tkmsg.showinfo("REGISTRATION"," Student Registered Successfully")

        #c.execute("insert into login values(?,?,?,?)", v2)

    except db.IntegrityError:
        tkmsg.showinfo("REGISTRATION", "You are a registered User")
    except Exception,e:
        tkmsg.showinfo("REGISTRATION", e)
    finally:
        conn.commit()
        conn.close()


def add_book(bname,s,au):
    try:
        getConnection()
        c = conn.cursor()
        stat="available"
        v1 = (bname,s,au,stat,)
        c.execute("insert into books(title,subject,author,status) values(?,?,?,?)", v1)
        if c.rowcount > 0:
            tkmsg.showinfo("Book Addition", "New Book Added in the record")

        else:
            tkmsg.showinfo("Book Addition error", "New Book cant be added")

    except Exception,e:
        print "ERROR",e

    finally:
        conn.commit()
        conn.close()

def delete_books(bk_id):
    try:
        getConnection()
        c = conn.cursor()
        v1 = (bk_id,)
        c.execute("delete from books where bid=?", v1)
        if c.rowcount > 0:
            tkmsg.showinfo("delete","deletion of record done")
        else:
            tkmsg.showinfo("error", "deletion error")
    except Exception,e:
        print e
    finally:
        conn.commit()
        conn.close()

def issue_books(id,isto,isby):
    try:
        getConnection()
        c = conn.cursor()

        v1 = (id, isto, isby,)
        v2 = (id,)
        rec = c.execute("Select count(*) from books where bid=? and status='available'", v2)
        if rec.fetchone()[0] == 1:
            c.execute("insert into issuedetail values(?,?,?)", v1)
            if c.rowcount > 0:
                tkmsg.showinfo("issued","book is issued")

            else:
                tkmsg.showinfo("error","book issue error")
        else:
           tkmsg.showinfo("error","book is already issued")

    except Exception, e:
        print e
    finally:
        conn.commit()
        conn.close()



'''def search_books(text):
    getConnection()
    try:
        c = conn.cursor()

        v = "%"+text+"%"
        v1 = (v,)
        c.execute("Select * from books where title or subject or author like ?",v1)
        # rec.fetchone()[0]== 1:
        row = c.fetchall()
        return row

        row = q.fetchall()
        for r in row:
            self.Scrolledtreeview1.insert("", 'end', text='', values=r)

    except Exception, e:
        print e
    finally:
        conn.close()'''
