dados= {}
def cadastrar_recursos():
    dias = int(input("Digite quantos dias estimados para o final da missão"))
    astronautas = int(input("Quantidade de astronautas:"))
    comida = int(input("Quantidade de comida (refeições):"))
    agua = float(input("Quantidade de água (L):"))
    oxigenio = float(input("Quantidade de oxigênio (kg):"))
    energia = float(input("Quantidade de energia (kWh):"))
    combustivel = float(input("Quantidade de combustível (L): "))
    consumo_energia = float(input("Quantidade de energia (kWh) consumida por dia:"))
    consumo_combustivel = float(input("Quantidade de combustível (L) consumido por dia:"))
    dados["dias"] = dias
    dados["astronautas"] = astronautas
    dados["comida"] = comida
    dados["agua"] = agua
    dados["oxigênio"] = oxigenio
    dados["energia"] = energia
    dados["combustivel"] = combustivel
    dados["consumo_energia"] = consumo_energia
    dados["consumo_combustivel"] = consumo_combustivel
def agua():
    astronautas = dados["astronautas"]
    agua = dados["agua"]
    consumo_agua = astronautas * 4
    dias_agua = agua / consumo_agua
    return dias_agua
def comida():
    astronautas = dados["astronautas"]
    comida = dados["comida"]
    consumo_comida = astronautas * 3
    dias_comida = comida / consumo_comida
    return dias_comida
def oxigenio():
    astronautas = dados["astronautas"]
    oxigenio = dados["oxigênio"]
    consumo_oxigenio = astronautas * 0.84
    dias_oxigenio = oxigenio / consumo_oxigenio
    return dias_oxigenio
def energia():
    energia = dados["energia"]
    consumo_energia = dados["consumo_energia"]
    dias_energia = energia / consumo_energia
    return dias_energia
def combustivel():
    combustivel = dados["combustivel"]
    consumo_combustivel = dados["consumo_combustivel"]
    dias_combustivel = combustivel / consumo_combustivel
    return dias_combustivel
def calcular():
    print("1-Calcular autonomia de água")
    print("2-Calcular autonomia de comida")
    print("3-Calcular autonomia de oxigênio")
    print("4-Calcular autonomia de energia")
    print("5-Calcular autonomia de combustivel")
    print("6-Calcular autonomia de todos os recursos")
    escolha = input("ESCOLHA UMA OPÇÃO (1,2,3,4,5,6)")
    match escolha:
        case "1":
            print(f"Água suficiente para {agua():.2f} dias")
        case "2":
            print(f"Comida suficiente para {comida():.2f} dias")
        case "3":
            print(f"Oxigênio suficiente para {oxigenio():.2f} dias")
        case "4":
            print(f"Energia suficiente para {energia():.2f} dias")
        case "5":
            print(f"Combustivel suficiente para {combustivel():.2f} dias")
        case "6":
            print(f"Água suficiente para {agua():.2f} dias")
            print(f"Comida suficiente para {comida():.2f} dias")
            print(f"Oxigênio suficiente para {oxigenio():.2f} dias")
            print(f"Energia suficiente para {energia():.2f} dias")
            print(f"Combustivel suficiente para {combustivel():.2f} dias")
def relatorio_agua(dias_agua):
    dias = dados["dias"]
    if dias < dias_agua:
        print("USO PADRÃO - Água suficiente para o restante da missão")
    elif dias > dias_agua:
        print("ALERTA!!! - Água insuficiente para o restante da missão")
    elif dias == dias_agua:
        print("ATENCÃO! - Quantidade de Água corresponde exatamente ao mínimo necesário para o restante da missão")
def relatorio_comida(dias_comida):
    dias = dados["dias"]
    if dias < dias_comida:
        print("USO PADRÃO - Comida suficiente para o restante da missão")
    elif dias > dias_comida:
        print("ALERTA!!! - Comida insuficiente para o restante da missão")
    elif dias == dias_comida:
        print("ATENCÃO! - Quantidade de Comida corresponde exatamente ao mínimo necesário para o restante da missão")
def relatorio_oxigenio(dias_oxigenio):
    dias = dados["dias"]
    if dias < dias_oxigenio:
        print("USO PADRÃO - Oxigênio suficiente para o restante da missão")
    elif dias > dias_oxigenio:
        print("ALERTA!!! - Oxigênio insuficiente para o restante da missão")
    elif dias == dias_oxigenio:
        print("ATENCÃO! - Quantidade de oxigênio corresponde exatamente ao mínimo necesário para o restante da missão")
def relatorio_combustivel(dias_combustivel):
    dias = dados["dias"]
    if dias < dias_combustivel:
        print("USO PADRÃO - Combustivel suficiente para o restante da missão")
    elif dias > dias_combustivel:
        print("ALERTA!!! - Combustivel insuficiente para o restante da missão")
    elif dias == dias_combustivel:
        print("ATENCÃO! - Quantidade de combustivel corresponde exatamente ao mínimo necesário para o restante da missão")
def relatorio_energia(dias_energia):
    dias = dados["dias"]
    if dias < dias_energia:
        print("USO PADRÃO - Energia suficiente para o restante da missão")
    elif dias > dias_energia:
        print("ALERTA!!! - Energia insuficiente para o restante da missão")
    elif dias == dias_energia:
        print("ATENCÃO! - Quantidade de energia corresponde exatamente ao mínimo necesário para o restante da missão")
def relatorio():
    print("1-Relatório da água")
    print("2-Relatório da comida")
    print("3-Relatório do oxigênio")
    print("4-Relatório da energia")
    print("5-Relatório do combustivel")
    print("6-Relatório  da todos os recursos")
    escolha = input("ESCOLHA UMA OPÇÃO (1,2,3,4,5,6)")
    match escolha:
        case "1":
            dias_agua = agua()
            relatorio_agua(dias_agua)
        case "2":
            dias_comida = comida()
            relatorio_comida(dias_comida)
        case "3":
            dias_oxigenio = oxigenio()
            relatorio_oxigenio(dias_oxigenio)
        case "4":
            dias_energia = energia()
            relatorio_energia(dias_energia)
        case "5":
            dias_combustivel = combustivel()
            relatorio_combustivel(dias_combustivel)
        case "6":
            dias_agua = agua()
            dias_comida = comida()
            dias_oxigenio = oxigenio()
            dias_energia = energia()
            dias_combustivel = combustivel()
            relatorio_agua(dias_agua)
            relatorio_comida(dias_comida)
            relatorio_oxigenio(dias_oxigenio)
            relatorio_energia(dias_energia)
            relatorio_combustivel(dias_combustivel)
def variaveis():
    print("1 - Vazamento de água")
    print("2 - Vazamento de oxigênio")
    print("3 - Falha elétrica")
    print("4 - Vazamento de combustivel")
    print("5 - Refeicões perdidas")
    print("6 - Correção de rota")
    print("7 - Modo econômico")
    print("8 - Desativar Modo econômico")
    escolha = input("ESCOLHA UMA OPÇÃO: (1,2,3,4,5,6,7,8")
    dados["modo_economico"] = False
    match escolha:
        case "1":
            perda = float(input("Litros perdidos:"))
            dados["agua"] -= perda
        case "2":
            perda = float(input("Kg perdidos:"))
            dados["oxigênio"] -= perda
        case "3":
            perda = float(input("perda de energia:"))
            dados["energia"] -= perda
        case "4":
            perda = float(input("Litros perdidos:"))
            dados["combustivel"] -= perda
        case "5":
            perda = float(input("Quantidade de refeicões perdidas:"))
            dados["comida"] -= perda
        case "6":
            combustivel_gasto =  float(input("Quantidade de combustivel (L) gasto na mmanobra"))
            energia_gasto = float(input("Quantidade de energia (kWh) gasto na mmanobra"))
            dados["combustivel"] -= combustivel_gasto
            dados["energia"] -= energia_gasto
        case "7":
            dados["modo_economico"] = True
            reducao = float(input("Redução (%) do consumo de energia: "))
            dados["consumo_energia"] = dados["consumo_energia"] - (dados["consumo_energia"] * reducao/100)
        case "8":
            dados["modo_economico"] = False
