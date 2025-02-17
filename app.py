from flask import Flask, request, jsonify
from models.meal import Meal
from database import db
from sqlalchemy import text


app = Flask(__name__)
app.config['SECRET_KEY'] = "my_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/daily-diet'
db.init_app(app)


@app.route("/diet", methods=['POST'])
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    in_diet = data.get("in_diet")

    if not name:
        return jsonify({"message": "Name required"}), 400

    meal = Meal(name=name, description=description, in_diet=in_diet)
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "User {meal.id} Registred meal with success!"})


@app.route("/diet", methods=['GET'])
def read_meals():
    meals = Meal.query.all()

    meals_list = []

    for meal in meals:
        meals_list.append({
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_hour": meal.date_hour,
            "in_diet": meal.in_diet
        })

    return jsonify({"Tasks": meals_list})


# Reseta o AUTO_INCREMENT para que a cada inicialização o primeiro meal criado seja de id = 1
# @app.route("/reset_ids", methods=['GET'])
# def reset_ids():
#     # Limpa todos os registros da tabela
#     db.session.execute(text("DELETE FROM meal"))

#     # Reseta o valor do AUTO_INCREMENT para 1
#     db.session.execute(text("ALTER TABLE meal AUTO_INCREMENT = 1"))

#     db.session.commit()
#     return jsonify({"message": "IDs resetados"})


if __name__ == '__main__':
    app.run(debug=True)
