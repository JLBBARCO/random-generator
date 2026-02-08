from faker import Faker

# Armazenamento em nível de módulo para que chamadores possam ler `randomNames.names`
names = []

def randomNames(quantity):
    """Gera `quantity` nomes aleatórios usando Faker e armazena em
    `randomNames.names` e na variável de módulo `names`.
    Retorna a lista gerada.
    """
    global names
    try:
        qty = int(quantity)
    except (TypeError, ValueError):
        qty = 0

    fake = Faker()
    generated = []
    for i in range(qty):
        generated.append((i, fake.name()))

    names = generated
    # Também expõe no objeto função para compatibilidade
    randomNames.names = names
    return names