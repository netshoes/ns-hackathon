from datetime import date

def parse_date(date_str):
    date_parts = date_str.split("/")
    ano = int(date_parts[2])
    if ano > 20:
        ano = 1900 + ano
    else:
        ano = 2000 + ano
    
    mes = int(date_parts[1])
    dia = int(date_parts[0])
    return date(ano, mes, dia)
