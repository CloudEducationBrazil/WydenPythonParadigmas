from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.User import User  # CORREÇÃO: importa a classe User diretamente

user_bp = Blueprint('user_bp', __name__)

# -------------------------
# Listar usuários (com busca opcional)
# -------------------------
@user_bp.route('/', methods=['GET'])
def list_users():
    query = request.args.get('q', '').strip()  # parâmetro de busca
    if query:
        if query.isdigit():  # busca por ID ou nome
            users = User.query.filter(
                (User.nome.ilike(f'%{query}%')) | (User.id == int(query))
            ).all()
        else:
            users = User.query.filter(User.nome.ilike(f'%{query}%')).all()
    else:
        users = User.query.all()
    return render_template('UserView.html', users=users, search=query)

# -------------------------
# Adicionar usuário
# -------------------------
@user_bp.route('/add', methods=['POST'])
def add_user():
    nome = request.form['nome']
    idade = int(request.form['idade'])  # converte para inteiro
    new_user = User(nome=nome, idade=idade)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('user_bp.list_users'))

# -------------------------
# Excluir usuário
# -------------------------
@user_bp.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_bp.list_users'))

# -------------------------
# Alterar usuário
# -------------------------
@user_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.nome = request.form['nome']
        user.idade = int(request.form['idade'])  # converte para inteiro
        db.session.commit()
        return redirect(url_for('user_bp.list_users'))
    return render_template('UserEdit.html', user=user)