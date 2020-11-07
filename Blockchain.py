import datetime, hashlib, json, jsonpickle, csv

# classe do bloco
class Blockchain:
    Noonce = 2  # QUANTO MAIOR, MAIS DIFICIL SERA MINERAR UM BLOCO

    # NOTA-SE DIFERENÇA NO TEMPO DE PROCESSAMENTO COM NOONCES ACIMA DE 5

    # construtor, só serve pra criar o bloco genesis
    def __init__(self):
        self.__chain = []
        self.create_block(proof=1, previous_hash='0')

    @staticmethod
    def noonce() -> int:
        return Blockchain.Noonce

    @property
    def chain(self) -> []:
        return self.__chain

    def write_all_csv(self):
        try:
            i = 0
            with open('CVS-BLOCKCHAIN.csv', 'w') as arq:
                cabecalho = [f"\nBLOCKCHAIN'.{center(80, '-')}\n"]
                escritacsv = DictWriter(arq, fieldnames=cabecalho)
                escritacsv.writeheader()
                while i < len(self.chain):
                    escritacsv.writerow(
                        {
                            "\tBloco #", self.chain['index'],
                            "\tTimestamp: ", self.chain['timestamp'],
                            "\tPOW: ", self.chain['proof'],
                            "\tPrevious Hash: ", self.chain['previous_hash']

                        }

                    )

                return 1

        except:
            print('Erro 405')
            return 0

    # escreve tudo de uma vez em um arquivo txt e um json (que pode ser recuperado)
    def write_chain_to_txt(self):
        with open('blockText.txt', 'w') as arq:
            arq.write(f"\nBLOCKCHAIN {'-' * 69}")
            try:
                i = 0
                while i < len(self.chain):
                    var = self.chain[i]
                    self.write_block_to_txt(var)
                    i += 1

                return 1
            except:
                print('Erro 404')
                return 0

    # escreve o objecto para o json
    def write_block_to_json(block):
        with open('blockJavaScript.json', 'a+') as arq:
            var = jsonpickle.encode(block)
            arq.write(var)

    #  formata e escreve o bloco num txt
    def write_block_to_txt(block):
        with open('blockText.txt', 'a+') as arq:
            arq.write(
                f"\n\n{'-' * 80}\nBloco #{block['index']}"
                f"\nCriado em: {block['timestamp']}"
                f"\nProva de trabalho: {block['proof']}"
                f"\nHash anterior: {block['previous_hash']}"
                f"\n{'-' * 80}"
            )

    # criar do bloco, para quando ja se tiver minerado
    def create_block(self, proof: int, previous_hash: str) -> dict:
        block = {'index': len(self.chain) + 1,  # bloco gerado, contador soma 1
                 'timestamp': str(datetime.datetime.now().strftime('%d/%m/%y')) + ' at ' + str(
                     datetime.datetime.now().time()),  # registro do tempo exato de criação
                 'proof': proof,  # prova de trabalho (mine)
                 'previous_hash': previous_hash}  # conexao com o bloco antigo (imutabilidade)
        self.chain.append(block)  # adição do bloco a cadeia
        return block

    # classe que retorna '0' * Noonce, pra uso na prova de trabalho
    def getNonce(self) -> str:
        return '0' * self.noonce()

    # retorna o bloco anterior
    def get_previous_block(self) -> dict:
        return self.chain[-1]

    # funcao chave do processo, onde se minera a prova de trabalho com processamento bruto de memória
    def proof_of_work(self, previous_proof: int) -> int:
        new_proof = 1
        check_proof = 0
        while check_proof == 0:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:self.noonce()] == self.getNonce():
                check_proof = 1
            new_proof += 1

        return new_proof

    # codifica o block de acordom com as informacoes
    def hash(self, block: dict) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()  # transforma o objeto pyton instanciado em string
        return hashlib.sha256(encoded_block).hexdigest()

    # função de verificação de corrente valida
    def is_chain_valid(self, chain: []) -> bool:
        previous_block = chain[0]
        i = 1
        while i < len(chain):  # percorre até o fim da corrente
            block = chain[block_index]
            if block['previous_hash'] != self.hash(
                    previous_block):  # verifica se o block anterior tem o hash condizente
                return False
            previous_proof = previous_block[
                'proof']  # com o previous_proof pode se verificar o previous hash (hash deterministico)
            proof = block['proof']  # acesso ao proof
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[
               :4] != '0000':  # noonce da blockchain '0000' (dificuldade), quanto mais zeros mais dificil de minerar
                return False
            previous_block = block
            i += 1
        return True
