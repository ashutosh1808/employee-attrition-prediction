from flask import Flask,render_template,request,redirect,url_for,session
from sqlite3 import *
import pickle

app=Flask(__name__)
app.secret_key="ashutoshrocks"

with open("ea.model","rb") as f:
	model=pickle.load(f)

@app.route("/",methods=["GET","POST"])
def home():
	if "username" in session:
		return render_template("home.html",name=session["username"])
	else:
		return redirect(url_for('login'))

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('login'))

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method=="POST":
		un=request.form["username"]
		pw=request.form["password"]
		con=None
		try:
			con=connect("auth.db")
			cursor=con.cursor()
			sql="select * from users where username='%s' and password='%s'"
			cursor.execute(sql%(un,pw))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("login.html",msg="Invalid Login")
			else:
				session["username"]=un
				return redirect(url_for("home"))
		except Exception as e:
			return render_template("login.html",msg=e)
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
	if request.method=="POST":
		username=request.form["username"]
		pw1=request.form["pw1"]
		pw2=request.form["pw2"]
		if pw1==pw2:
			con=None
			try:
				con=connect("auth.db")
				cursor=con.cursor()
				sql="insert into users values('%s','%s')"
				cursor.execute(sql%(username,pw1))
				con.commit()
				return redirect(url_for('login'))
			except IntegrityError:
				con.rollback()
				return render_template("signup.html",msg="User already exists")
			except Exception as e:
				con.rollback()
				return render_template("signup.html",msg=e)
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html",msg="Passwords did not match")
	else:
		return render_template("signup.html")

@app.route("/pred",methods=["POST"])
def pred():
	mi=float(request.form["mi"])
	age=int(request.form["age"])
	daily_rate=int(request.form["daily_rate"])
	yslp=int(request.form["yslp"])
	ywcm=int(request.form["ywcm"])
	yic=int(request.form["yic"])
	ji=int(request.form["ji"])
	ot=int(request.form["ot"])
	d=[[mi,age,daily_rate,yslp,ywcm,yic,ji,ot]]	
	res=model.predict(d)[0]
	prob_no=float(model.predict_proba(d)[0][0])
	prob_yes=float(model.predict_proba(d)[0][1])
	prob_max=round(max(prob_yes,prob_no)*100,2)
	return render_template("home.html",msg=str(res)+" with a "+str(prob_max)+"% chance")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)