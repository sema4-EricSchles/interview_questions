from flask import Flask
import numpy as np
from datetime import datetime
import dateparser
import json

app = Flask(__name__)
    
@app.route("/", methods=["GET"])
def index():
    settings = {
        'TIMEZONE': 'UTC',
        'TO_TIMEZONE': 'US/Eastern'
    }
    center = 3
    spread = 5
    return json.dumps({
        "A": np.random.normal(loc=center, scale=spread),
        "B": np.random.normal(loc=center, scale=spread),
        "C": np.random.normal(loc=center, scale=spread),
        "timestamp_one": dateparser.parse(
            str(datetime.now()), settings=settings
        ),
        "timestamp_two": str(datetime.utcnow())
    })

if __name__ == '__main__':
    app.run()
