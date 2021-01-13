from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/read',methods=['GET','POST'])
def getname():
    if(request.method=='POST'):
        name=str(request.form.get('name'))
        rollno=str(request.form.get('rollno'))
        admissionno=str(request.form.get('admissionno'))
        college=str(request.form.get('college'))
        return "name="+name+"rollno ="+rollno+"admissionno ="+admissionno+"college ="+college                                                                                                                                                                            
@app.route('/')
def login():    
    return render_template("college.html")


if(__name__=='__main__'):
    app.run()