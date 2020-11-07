from flask import Flask, jsonify
import timeit
import Blockchain

app = Flask(__name__)

blockchain = bc.Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    Blockchain.write_chain_to_txt(block)
    Blockchain.write_block_to_json(block)
    response = {'message': f'Parabens voce acabou de minerar um bloco!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def show_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': ' Valid blockchain!'}
    else:
        response = {'message': ' Invalid blockchain!'}
    return jsonify(response), 200


@app.route('/write_chain', methods=['GET'])
def write_chain():
    if blockchain.write_all_csv() == 1:
        response = {'message': ' Blockchain written on files!'}
    else:
        response = {'message': ' Fail in written!'}
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)
