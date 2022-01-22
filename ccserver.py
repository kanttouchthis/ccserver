from flask import Flask, request
app = Flask("ccserver")
datadict = dict()

def log(text:str, filename="log.txt"):
    with open(filename, "a") as f:
        f.write("\n" + text)

@app.route("/up", methods=["GET"])
def up():
    source = request.args.get("source")
    target = request.args.get("target")
    data = request.args.get("data")
    log(data, "up.txt")
    if target in list(datadict.keys()):
        datadict[target].append({source:data})
    else:
        datadict[target] = [{source:data}]
    log(str(datadict), "log.txt")
    return "" 

@app.route("/down", methods=["GET"])
def down():
    source = request.args.get("source")
    target = request.args.get("target")
    try:
        for i, source_data in enumerate(datadict[target]):
            if list(source_data.keys())[0] == source:
                requested_data = datadict[target].pop(i)
                return source_data[source]
    except Exception as e:
        log(str(e), "down.txt")
        return ""

app.run("0.0.0.0", port=1234, debug=True)
