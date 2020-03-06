from flask import Flask

app = Flask("Demo")

@app.route('/hello/')
@app.route('/hello/<name>')
def begruessung(name=False):
    if name:
         return "Hallo " + name + "!"
    else:
        return "Notnot Hallo World again…"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
