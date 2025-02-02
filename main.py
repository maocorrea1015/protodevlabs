from flask import Flask, request, render_template, redirect, url_for
from config import Config
from models import db, Usuario
from db import create_db
from dotenv import load_dotenv

def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Crear tablas al iniciar la aplicación
    create_db(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('notfound.html'), 404

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            nombre = request.form['nombre']
            telefono = request.form['telefono']
            correo = request.form['correo']
            descripcion_del_proyecto = request.form['descripcion_del_proyecto']

            nuevo_usuario = Usuario(
                nombre=nombre,
                telefono=telefono,
                correo=correo,
                descripcion_del_proyecto=descripcion_del_proyecto
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            return redirect(url_for('index'))

        return render_template('index.html')

    @app.route('/abaut')
    def abaut():
        return render_template('abaut.html')

    @app.route('/apolo')
    def admin():
        usuarios = Usuario.query.order_by(Usuario.id.desc()).all()
        return render_template('admin.html', usuarios=usuarios)

    return app


if __name__ == '__main__':
        app = crear_app()
        app.run(debug=True)
