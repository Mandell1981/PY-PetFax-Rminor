from flask import Flask 

#factory 
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    from petfax.pet import bp as pet_bp
    app.register_blueprint(pet_bp, url_prefix='/pets')
    

    #return the app
    return app
    
    