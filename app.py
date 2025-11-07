from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, This response is from ECS and CodePipeline! This is written and deployed by Jayanta Chatterjee.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)