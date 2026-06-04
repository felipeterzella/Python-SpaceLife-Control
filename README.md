Sistema de Controle de Recursos de uma Missão Espacial

Sistema que simula o controle de recursos de uma nave espacial permitindo verificar automnomia e se os suprimentos são suficientes para o restante da missão.

Funcionalidades

O usuário (astronauta) insere:

Dias estimados da missão
Número de astronautas
Quantidade de:
Água
Comida
Oxigênio
Energia
Combustível
Consumo diário de energia e combustível
Cálculo de autonomia

O sistema calcula quantos dias cada recurso suporta com base no consumo diário informado.

Relatório classificando os recursos em:

NORMAL → recurso suficiente
ATENÇÃO → recurso no limite
ALERTA!!! → recurso insuficiente
Eventos do sistema

O sistema simula problemas como:

Vazamento de água
Vazamento de oxigênio
Falha elétrica
Vazamento de combustível
Perda de refeições
Correção de rota com consumo extra de recursos
Modo econômico

O sistema permite reduzir o consumo de energia, aumentando a autonomia da missão

Atualização do sistema:

Após os problemas ou ativação do modo econômico os valores são atualizados e o sistema pode recalcular autonomias e gerar novos relatórios

Como executar
python principal.py