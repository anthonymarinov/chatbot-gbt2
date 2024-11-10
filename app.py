from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Variables
maxLength = 100
numReturnSequences = 1

app = Flask( __name__ )
CORS( app )

tokenizer = GPT2Tokenizer.from_pretrained( 'openai-community/gpt2' )
model = TFGPT2LMHeadModel.from_pretrained( 'openai-community/gpt2-large' )

@app.route( '/chatbot', methods=[ 'POST' ] )
def chatbot():
    message = request.json[ 'message' ]
    inputIDs = tokenizer.encode( message, return_tensors='tf' )
    outputIDs = model.generate( inputIDs, 
                                max_length=maxLength, 
                                num_return_sequences=numReturnSequences,
                                eos_token_id=tokenizer.eos_token_id,
                                temperature=0.7,
                                no_repeat_ngram_size=2,
                                pad_token_id=tokenizer.eos_token_id )
    response = tokenizer.decode( outputIDs[ 0 ] )

    if response.startswith(message):
        response = response[len(message):].strip()

    return jsonify( {'response': response} )

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)