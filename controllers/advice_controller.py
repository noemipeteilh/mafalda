from models.advice_model import AdviceModel

class AdviceController:
    @staticmethod
    def create_advice_from_json(data):
        for item in data:
            genero = item["genero"]
            edad = item["edad"]
            conducta = item["conducta"]
            consejo = item["consejo"]
            AdviceModel.create_advice(genero, edad, conducta, consejo)

    @staticmethod
    def get_advice(id):  # ASEGÚRATE DE QUE ESTE MÉTODO LLAME CORRECTAMENTE A AdviceModel
        return AdviceModel.get_advice(id)


    @staticmethod
    def update_advice(id):
        AdviceModel.update_advice(id,genero,edad,conducta,consejo)

    @staticmethod
    def delete_advice(id):
        AdviceModel.delete_advice(id)