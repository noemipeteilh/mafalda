from models.advice_model import AdviceModel


class AdviceController:
    @staticmethod
    def create_advice(genero, edad, conducta, consejo):
        # Aquí podrías agregar validaciones de negocio, como verificar si el consejo ya existe
        AdviceModel.create_advice(genero, edad, conducta, consejo)

    @staticmethod
    def get_advice(id):
        return AdviceModel.get_advice(id)

    @staticmethod
    def update_advice(id, new_advice):
        AdviceModel.update_advice(id, new_advice)

    @staticmethod
    def delete_advice(id):
        AdviceModel.delete_advice(id)
