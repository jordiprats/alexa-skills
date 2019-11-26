import alexandra

app = alexandra.Application()
name_map = {}

@app.launch
def launch_handler(item):
    return alexandra.respond(ssml="<speak><audio src='https://alexa.systemadmin.es/octoalert48.mp3'/></speak>")

@app.intent('octoalert')
def octoalert_intent():
    return alexandra.respond(ssml="<speak><audio src='https://alexa.systemadmin.es/octoalert48.mp3'/></speak>")

if __name__ == '__main__':
    app.run('0.0.0.0', 9999, debug=True)

