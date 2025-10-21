import os

def create_flask_project(project_name):
    base_dir = os.path.join(os.getcwd(), project_name)
    app_dir = os.path.join(base_dir, 'app')

    os.makedirs(app_dir, exist_ok=True)

    # run.py
    run_content = """from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
"""
    with open(os.path.join(base_dir, 'run.py'), 'w', encoding='utf-8') as f:
        f.write(run_content)

    # app/__init__.py
    init_content = """from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app
"""
    with open(os.path.join(app_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(init_content)

    # app/routes.py
    routes_content = """from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "App Flask rodando com sucesso!"
"""
    with open(os.path.join(app_dir, 'routes.py'), 'w', encoding='utf-8') as f:
        f.write(routes_content)

    print(f"✅ Projeto Flask '{project_name}' criado com sucesso em {base_dir}")
    print("\nPróximos passos:")
    print(f"1. cd {project_name}")
    print("2. python -m venv venv")
    print("3. venv\\Scripts\\activate")
    print("4. pip install flask")
    print("5. python run.py")

if __name__ == "__main__":
    name = input("Digite o nome do novo projeto Flask: ")
    create_flask_project(name)