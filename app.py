from flask import Flask

app = Flask(__name__)

@app.route('/')
def stack_trace_error():
    number = "one"
    try:
        int(number)
    except Exception as e:
        response = {
            "message": e
        }
    print(response)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
