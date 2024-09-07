from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random",methods=['GET'])
def random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)
    return jsonify(cafe=cafe.to_dict())

@app.route('/all',methods=['GET'])
def all():
    cafes = db.session.query(Cafe).all()
    # cafe_list = []
    # for cafe in cafes:
    #     cafe = cafe.to_dict()
    #     cafe_list.append(cafe)
    # all_cafes = {"cafes":cafe_list}
    # return jsonify(all_cafes["cafes"])
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route('/search')
def get_cafe_at_location():
    query_location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location = query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found":"Sorry,there is no cafe in that location"})

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route('/update-price/<int:cafe_id>',methods=["PATCH","GET"])
def update_price(cafe_id):
    update_cafe = Cafe.query.get(cafe_id)
    new_price = request.args.get('new_price')
    if update_cafe:
        update_cafe.coffe_price = new_price
        db.session.commit()
        return jsonify(response={"success":"Successfully updated the price"})
    else:
        return jsonify(error={"Not Found":"Sorry,there is no cafe with such ID"})

@app.route('/report-closed/<int:cafe_id>',methods=['GET','DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    API_KEY = '12345'
    if api_key == API_KEY:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"})
    else:
        return jsonify(error={"Forbidden": "Sorry that is not allowed. Make sure you have the correct api_key."})

if __name__ == '__main__':
    app.run(debug=True)
