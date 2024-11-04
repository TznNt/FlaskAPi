# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers.ap2_escola_controller import school_blueprint
from models.ap2_escola_models import db

app = Flask(__name__)

# Carregar configurações
app.config.from_object(Config)

# Inicializar o banco de dados
db.init_app(app)

# Registrando o blueprint
app.register_blueprint(school_blueprint, url_prefix='/school')

@app.route('/')
def index():
    return render_template('ap2_escola_views.html', output='')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criar as tabelas no banco de dados
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])