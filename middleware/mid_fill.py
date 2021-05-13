import eel
from backend.afd_helps import HelpsMetods

convet_text = HelpsMetods.convet_text_in_numbers

@eel.expose
def convert_value(text):
    return convet_text(text)
