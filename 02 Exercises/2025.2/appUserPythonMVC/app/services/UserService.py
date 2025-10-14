from app.repositories.UserRepository import UserRepository
from app.models.User import User

class UserService:

    @staticmethod
    def list_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def create_user(nome, idade):
        user = User(nome=nome, idade=idade)
        UserRepository.add(user)
        return user

    @staticmethod
    def update_user(user_id, nome, idade):
        user = UserRepository.get_by_id(user_id)
        if user:
            user.nome = nome
            user.idade = idade
            UserRepository.update()
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete(user)
        return user