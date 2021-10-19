from dojos_ninjas_app import app
from dojos_ninjas_app.controllers.dojos import *
from dojos_ninjas_app.controllers.ninjas import *

if __name__ == "__main__":
    app.run(debug=True)