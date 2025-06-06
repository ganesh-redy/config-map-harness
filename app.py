from flask import Flask

app = Flask(__name__)

CONFIG_FILE_PATH = "/config/data.properties"

def load_config():
    config = {}
    try:
        with open(CONFIG_FILE_PATH, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    config[key.strip()] = value.strip()
    except Exception as e:
        config["error"] = f"Failed to read config: {e}"
    return config

@app.route("/")
def index():
    config = load_config()
    if "error" in config:
        return config["error"], 500
    name = config.get("name", "Unknown")
    age = config.get("age", "Unknown")
    return f"Name: {name}, Age: {age}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

