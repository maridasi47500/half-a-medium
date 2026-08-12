
mkdir templates 
python3 scaffold.py user username phone country_id:references email password
python3 scaffold.py country name
python3 scaffold.py city country_id:references name daypic:file nightpic:file
python3 scaffold.py person city_id:references username phone country_id:references fullname dateofbirth pic:file  address
python3 scaffold.py cityhassql query description user_id:references
python3 scaffold.py cityhassqlhaspeople person_id:references cityhassql_id:references
