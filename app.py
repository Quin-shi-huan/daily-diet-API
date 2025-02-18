from flask import Flask, request, jsonify
from models.meal import Meal
from database import db
from sqlalchemy import text


app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:1234@127.0.0.1:3306/daily-diet"
)
db.init_app(app)


@app.route("/diet", methods=["POST"])
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    in_diet = data.get("in_diet")

    if not name or not description:
        return jsonify({"message": "Name and Description is required!"}), 400

    meal = Meal(name=name, description=description, in_diet=in_diet)
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "User Registred meal with success!"})


@app.route("/diet", methods=["GET"])
def read_meals():
    meals = Meal.query.all()

    meals_list = []

    for meal in meals:
        meals_list.append(
            {
                "id": meal.id,
                "name": meal.name,
                "description": meal.description,
                "date_hour": meal.date_hour,
                "in_diet": meal.in_diet,
            }
        )

    return jsonify({"Meals": meals_list})


@app.route("/diet/<int:id>", methods=["GET"])
def read_meal(id):
    meal = Meal.query.get(id)

    if meal:
        return jsonify(
            {
                "id": meal.id,
                "name": meal.name,
                "description": meal.description,
                "date_hour": meal.date_hour,
                "in_diet": meal.in_diet,
            })

    return jsonify({"message": "Meal not found"}), 404


# Reseta o AUTO_INCREMENT para que a cada inicialização o primeiro meal criado seja de id = 1
# @app.route("/reset_ids", methods=['GET'])
# def reset_ids():a
#     # Limpa todos os registros da tabela
#     db.session.execute(text("DELETE FROM meal"))

#     # Reseta o valor do AUTO_INCREMENT para 1
#     db.session.execute(text("ALTER TABLE meal AUTO_INCREMENT = 1"))

#     db.session.commit()
#     return jsonify({"message": "IDs resetados"})


@app.route("/diet/<int:id>", methods=['PUT'])
def update_meal(id):
    meal = Meal.query.get(id)
    data = request.json
    name = data.get("name")
    description = data.get("description")
    in_diet = data.get("in_diet")

    if meal is None:
        return jsonify({"message": "Meal not found!"}), 404

    if not name or not description:
        return jsonify({"message": "Name or description cannot be empty!"}), 400

    if not in_diet:
        return jsonify({"message": "diet cannot be empty!"}), 400

    meal.name = data.get('name', meal.name)
    meal.description = data.get('description', meal.description)
    meal.in_diet = data.get('in_diet', meal.in_diet)

    db.session.commit()

    return jsonify({"message": "Meal updated with success!"})


@app.route("/diet/<int:id>", methods=["DELETE"])
def delete_meal(id):
    meal = Meal.query.get(id)

    if meal is None:
        return jsonify({"message": "Meal not found!"}), 404

    db.session.delete(meal)
    db.session.commit()

    return jsonify({"message": "Meal deleted with success!"})


if __name__ == "__main__":
    app.run(debug=True)
