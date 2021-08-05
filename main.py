from flask import Flask, render_template, request
import thoai;
app = Flask(__name__)


@app.route("/lamthov1",methods=["POST","GET"])
def danhdau():
    if request.method == 'POST':
        ip = request.form["inputdt"]
        if ip == "":
            return render_template("lamtho.html")
        else:
            ip = thoai.xoadau(ip)
            inp = thoai.inracautho(ip)
            return render_template("lamtho.html",inp=inp)
    else:
        return render_template("lamtho.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

