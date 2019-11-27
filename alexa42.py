import alexandra

@app.launch
def launch_handler(item):
    return alexandra.respond(ssml="<speak>42</speak>")

@app.intent('rajoy')
def octoalert_intent():
    return alexandra.respond(ssml="<speak>42</speak>")

if __name__ == '__main__':
    app.run('0.0.0.0', 9998, debug=True)
