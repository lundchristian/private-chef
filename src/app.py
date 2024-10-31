# pylint: skip-file

# standard libraries
import os

# third-party dependencies
import flask
import flask_cors

# local dependencies
import chef
import const
from embedded import RaspberryPi

# use `export UIT_KEY="sk-..."` to set the key or the like
uit_key = os.getenv("UIT_KEY")
if not uit_key:
    raise ValueError("UIT_KEY environment variable not set")

rpi = RaspberryPi()

open_ai_chef = chef.OpenAiChef(
    api_key=uit_key,  # openai api key
    system_role=const.STRONG_SYSTEM_ROLE,  # json format
)

phi_ai_chef = chef.Gpt4AllChef(
    model_name=const.PHI,
    model_path=const.MODEL_PATH,
    system_role=const.WEAK_SYSTEM_ROLE,
    device="cpu",
)

app = flask.Flask(__name__)
flask_cors.CORS(app)


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/health")
def health():
    return "<html><body><p>OK</p></body></html>"


@app.route("/recipe", methods=["POST"])
def recipe():
    request = flask.request.get_json(force=True)
    spicy = request.get("spicy")
    model = request.get("model")
    region = request.get("region")
    ingredients = rpi.get_fridge_contents()

    if model == "local":
        try:
            generated_recipe = phi_ai_chef.generate_recipe(region, ingredients)
            return flask.jsonify(generated_recipe)
        except Exception as e:
            return flask.jsonify({"error": str(e)}), 500
    else:  # use external model
        try:
            generated_recipe = open_ai_chef.generate_recipe(model, region, ingredients)
            return flask.jsonify(generated_recipe)
        except Exception as e:
            return flask.jsonify({"error": str(e)}), 500


def main():
    app.run(port=const.PORT, host=const.HOST, debug=True)


if __name__ == "__main__":
    main()
