# py .\utils_example.py

from utils import to_mx, clean_str

#Nesting (Lista de diccionarios)
raw=[
    {"Name":"     ANa ", "active":True, "cash": "120.50"},
    {"Name":"    Luis ", "active":False, "cash": "0"},
    {"Name":"  mara   ", "active":True, "cash": "99.99"}
]

def clean(row: dict) -> dict:
    """
       This function returns a formated dictionary
    """
    return {
        "name": clean_str(row["name"]),
        "activate": bool(row["activate"]),
        "cash_MXN": to_mx(row["cash"])
    }

# dale caña
# list comprenhesion
cleandata=[clean(r) for r in raw]
print("\nLista Original\n", raw)
print("\nLista Formateada\n", cleandata)