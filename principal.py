from funcoes import relatorio, variaveis, calcular, cadastrar_recursos
while True:
    print("======SISTEMA DE CONTROLE DE RECURSOS======")
    print("1 - Adicionar recursos")
    print("2 - Calcular autonomia")
    print("3 - Aplicar evento")
    print("4 - Ver relatorio")
    print("5 - Sair")
    print("===========================================")
    opcao = input("ESCOLHA UMA OPÇÃO (1,2,3,4,5)")
    match opcao:
        case "1":
            cadastrar_recursos()
        case "2":
            calcular()
        case "3":
            variaveis()
        case "4":
            relatorio()
        case "5":
            break