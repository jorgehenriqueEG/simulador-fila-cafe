clientes = [
    {"nome": "Ana", "bebida": "espresso"},
    {"nome": "Bruno", "bebida": "latte"},
    {"nome": "Carla", "bebida": "mocha"}
]

tempos_base = {
    "espresso": 1.0,
    "latte": 2.5,
    "mocha": 3.0
}

tempo_total = 0

for cliente in clientes:
    tipo_bebida = cliente["bebida"]
    if tipo_bebida in tempos_base:
        tempo_atual = tempos_base[tipo_bebida]
        if tipo_bebida == "espresso":
            tempo_atual *= 1.5
            tempo_total += tempo_atual
        else:
            tempo_total += tempo_atual

print(f"O tempo total de espera da fila é de {tempo_total} minutos.")