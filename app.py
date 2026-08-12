from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,phone,country_id,email,password) values (:username,:phone,:country_id,:email,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','phone','country_id','email','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','phone','country_id','email','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','phone','country_id','email','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['daypic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["daypic"]=uploaded_file.filename

        uploaded_file = request.files['nightpic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["nightpic"]=uploaded_file.filename


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (country_id,name,daypic,nightpic) values (:country_id,:name,:daypic,:nightpic)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_person", methods=["GET","POST"])
def add_one_person():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslescity= query_db("select * from city")

        touslescountry= query_db("select * from country")

        one_user = query_db("insert into person (city_id,username,phone,country_id,fullname,dateofbirth,pic,address) values (:city_id,:username,:phone,:country_id,:fullname,:dateofbirth,:pic,:address)",hey)
        user = query_db('select * from person')

        return render_template("personform.html", persons=user, one_user=one_user, the_title="add new person", touslescity=touslescity, touslescountry=touslescountry)


    touslescity= query_db("select * from city")

    touslescountry= query_db("select * from country")

    user = query_db('select * from person')
    one_user = query_db("select * from person limit 1", one=True)
    return render_template("personform.html", persons=user, one_user=one_user, the_title="add new person", touslescity=touslescity, touslescountry=touslescountry)

@app.route("/add_one_cityhassql", methods=["GET","POST"])
def add_one_cityhassql():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into cityhassql (query,description,user_id) values (:query,:description,:user_id)",hey)
        user = query_db('select * from cityhassql')

        return render_template("cityhassqlform.html", cityhassqls=user, one_user=one_user, the_title="add new cityhassql", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from cityhassql')
    one_user = query_db("select * from cityhassql limit 1", one=True)
    return render_template("cityhassqlform.html", cityhassqls=user, one_user=one_user, the_title="add new cityhassql", touslesuser=touslesuser)

@app.route("/add_one_cityhassqlhaspeople", methods=["GET","POST"])
def add_one_cityhassqlhaspeople():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesperson= query_db("select * from person")

        touslescityhassql= query_db("select * from cityhassql")

        one_user = query_db("insert into cityhassqlhaspeople (person_id,cityhassql_id) values (:person_id,:cityhassql_id)",hey)
        user = query_db('select * from cityhassqlhaspeople')

        return render_template("cityhassqlhaspeopleform.html", cityhassqlhaspeoples=user, one_user=one_user, the_title="add new cityhassqlhaspeople", touslesperson=touslesperson, touslescityhassql=touslescityhassql)


    touslesperson= query_db("select * from person")

    touslescityhassql= query_db("select * from cityhassql")

    user = query_db('select * from cityhassqlhaspeople')
    one_user = query_db("select * from cityhassqlhaspeople limit 1", one=True)
    return render_template("cityhassqlhaspeopleform.html", cityhassqlhaspeoples=user, one_user=one_user, the_title="add new cityhassqlhaspeople", touslesperson=touslesperson, touslescityhassql=touslescityhassql)

