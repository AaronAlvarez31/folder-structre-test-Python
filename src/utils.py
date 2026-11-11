"""
   Utileria de limpieza y conversion
"""
def to_mx(value, rate = 18.58): #Value significa valor, Rate significa tasa(en impuestos o de comida)
    """
       This function converts a value (USD)
       to MXN via rate
    """
    return float(value)*float(rate)

def clean_str(name: str) -> str:
    """
       This fuctions clean name
    """
    return " ".join.strip().title().split()

"""
   name: "      AAroN   AntoNiO    alvAreZ EscobeDO  "

   name.strip() -> "AAroN   AntoNiO    alvAreZ EscobeDO"

   name.title() -> "Aaron   Antonio    Alvarez Escobedo"

   name.split() -> ["Aaron","Antonio","Alvarez","Escobedo"]

"""

