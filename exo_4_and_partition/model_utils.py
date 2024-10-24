import joblib


def load_model():
    model_loaded = joblib.load("regression.joblib")
    return model_loaded


def make_prediction(size, nb_rooms, garden, model):
    return model.predict([[size, nb_rooms, garden]])
