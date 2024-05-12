from flask import Flask 


#factory 
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, this is PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    #register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    #return the app
    return app
    
    

   
    