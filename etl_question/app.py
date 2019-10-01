from flask import Flask
import numpy as np
from datetime import datetime
import json

app = Flask(__name__)
    
@app.route("/", methods=["GET"])
def index():
    center = 3
    spread = 5
    return json.dumps({
        "A": np.random.normal(loc=center, scale=spread),
        "B": np.random.normal(loc=center, scale=spread),
        "C": np.random.normal(loc=center, scale=spread),
        "timestamp_one": str(datetime.now()),
        "timestamp_two": str(datetime.utcnow())
    })

if __name__ == '__main__':
    app.run()
