from flask import Flask, render_template

app = Flask(__name__)

@app.route('/register_page')
def register():
    return render_template("/serverwebpl.html")

if __name__ == "__main__":
    ip = "172.31.31.121"
    port = "80"
    app.run(ip, port)