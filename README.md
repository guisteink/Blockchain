# Blockchain
just an attempt to implement in python a blockchain structure

# Definição 
    ->  CRIPTOGRAFIA HASH 256:
        *   ALGORITMO QUE NÃO É INVERSÍVEL
        *   DETERMÍNISTICO, OU SEJA, DE ACORDO COM OS PARAMETROS DE ENTRADA NO ALGORITMO RETORNA A MESMA SAÍDA
        *   PROCESSAMENTO RÁPIDO
        *   SUPORTA COLISÕES
    ->  REGISTROS IMUTÁVEIS (EFEITO AVALANCHE):
        *   INFRAUDÁVEL (CONFIABILIDADE)
    ->  REDE P2P DESCENTRALIZADA
        *   LIGAÇAÕ POR HASH
    ->  MINERAÇÃO DE BLOCOS
        *   RECOMPENSA POR TEMPO E GASTO DE PROCESSAMENTO
    ->  PROTOCOLO DE CONSENSO
        *   SEGURANÇA
     
     Noonce: definição da dificuldade de uma rede blockchain, é a quantidade de zeros que existem nos primeiros digitos
    de um HASH 256 de um determinado bloco. Ex: Noonce = 2. Hash: '00ASOI2OPI2342340ASDJPO12WKER'

# Smart contracts
    Em base, são uma forma genérica de tratar de aplicações que usam  a tecnologia blockchain. Esses contratos tem regras
    e protocolos que governam as relações entre as partes, e eles são em suma as cadeias de códigos que definem essas regras.

    Ethereum -> Solidity -> Turing completo: Linguagem em que se pode codificar qualquer lógica de programação, autonomia.

    Dapps (aplicação descentralizada) -> Interface para as pessoas interagirem com os contatos inteligentes

    Exemplos:
        -> steemit.com (site que funciona em blockchain)
        -> ethgasstation.info (sistema de compra de gás em ethereum)
        -> hackernoon/ether-purchase-power (cálculos e conteúdos que provam eficácia no sistema)

# Tecnologias
- Python
- Flask
- PyCharm
