from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'model2.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/index.html')#binds to an url
def index():
    return render_template("index.html")

@app.route('/team.html')#binds to an url
def team():
   return render_template("team.html")

@app.route('/about.html')#binds to an url
def about():
   return render_template("about.html")

@app.route('/contact.html')#binds to an url
def contact():
   return render_template("contact.html")

@app.route('/services.html')#binds to an url
def services():
   return render_template("services.html")

@app.route('/result.html', methods=['POST'])#binds to an url
def result():
    gender = request.form["gender"]
    if(gender=="Boy"):
        g1,g2 = 1,0
    if(gender=="Girl"):
        g1,g2 = 0,1

    age = request.form["age"]
    if (age=="1-5"):
        a1,a2,a3,a4,a5,a6=1,0,0,0,0,0
    if (age=="11-15"):
        a1,a2,a3,a4,a5,a6=0,1,0,0,0,0
    if (age=="16-20"):
        a1,a2,a3,a4,a5,a6=0,0,1,0,0,0
    if (age=="21-25"):
        a1,a2,a3,a4,a5,a6=0,0,0,1,0,0
    if (age=="26-30"):
        a1,a2,a3,a4,a5,a6=0,0,0,0,1,0
    if (age=="6-10"):
        a1,a2,a3,a4,a5,a6=0,0,0,0,0,1
        
    education_level = request.form["Education"]
    if (education_level=="College"):
        ed1,ed2,ed3=1,0,0
    if (education_level=="School"):
        ed1,ed2,ed3=0,1,0
    if (education_level=="University"):
        ed1,ed2,ed3=0,0,1
    
    institution = request.form["Institution"]
    if(institution=="Government"):
        i1,i2 = 1,0
    if(institution=="Non Government"):
        i1,i2 = 0,1

    it_student = request.form["IT Student"]
    if(it_student=="Non-IT"):
        it1,it2 = 1,0
    if(it_student=="IT"):
        it1,it2 = 0,1
        
    location = request.form["Location"]
    if(location=="Out-town"):
        l1,l2 = 1,0
    if(location=="In-town"):
        l1,l2 = 0,1
        
    load_shedding = request.form["Load-shedding"]
    if(load_shedding=="High"):
        ls1,ls2 = 1,0
    if(load_shedding=="Low"):
        ls1,ls2 = 0,1
        
    financial_condition = request.form["Financial Condition"]
    if (financial_condition=="Mid"):
        fc1,fc2,fc3=1,0,0
    if (financial_condition=="Poor"):
        fc1,fc2,fc3=0,1,0
    if (financial_condition=="Rich"):
        fc1,fc2,fc3=0,0,1
  
    internet = request.form["Internet Type"]
    if(internet=="Mobile Data"):
        inter1,inter2 = 1,0
    if(internet=="Wifi"):
        inter1,inter2 = 0,1

    network = request.form["Network Type"]
    if (network=="2G"):
        n1,n2,n3=1,0,0
    if (network=="3G"):
        n1,n2,n3=0,1,0
    if (network=="4G"):
        n1,n2,n3=0,0,1
        
    class_duration = request.form["Class Duration"]
    if (class_duration=="0"):
        cd1,cd2,cd3=1,0,0
    if (class_duration=="1-3"):
        cd1,cd2,cd3=0,1,0
    if (class_duration=="3-6"):
        cd1,cd2,cd3=0,0,1
        
    self_lms = request.form["Self Lms"]
    if(self_lms=="No"):
        lms1,lms2 = 1,0
    if(self_lms=="Yes"):
        lms1,lms2 = 0,1        

    device_type = request.form["Device"]
    if (device_type=="Computer"):
        d1,d2,d3=1,0,0
    if (device_type=="Mobile"):
        d1,d2,d3=0,1,0
    if (device_type=="Tab"):
        d1,d2,d3=0,0,1
    
    test_input = [[int(g1),int(g2),int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(ed1),
                   int(ed2),int(ed3),int(i1),int(i2),int(it1),int(it2),int(l1),int(l2),int(ls1),
                   int(ls2),int(fc1),int(fc2),int(fc3),int(inter1),int(inter2),int(n1),int(n2),int(n3),
                   int(cd1),int(cd2),int(cd3),int(lms1),int(lms2),int(d1),int(d2),int(d3)]]

    output= model.predict(test_input)
    print(output)
    
    return render_template("result.html",gender=gender,age=age,education=education_level,
                           institution=institution,IT_student=it_student,location=location,load_shedding=load_shedding,
                           financial_condition=financial_condition,internet=internet,network_type=network,class_duration=class_duration,self_lms=self_lms,
                           device=device_type,y =str(output[0]))

if __name__ == '__main__' :
    app.run(debug= True)
    
