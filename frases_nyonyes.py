#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import alexandra

app = alexandra.Application()
name_map = {}

frases = {
    "Si no tardas mucho, te espero toda la vida.",
    "Quiero vivir eternamente en tu sonrisa.",
    "Cualquiera en su sano juicio se habría vuelto loco por ti.",
    "Cualquier lugar es mi casa si eres tú quien abre la puerta.",
    "Sería capaz de reconocer tu cara entre un millón de sueños.",
    "Te miraba reír y ahí estaban mis futuros.",
    "Te quiero. Creo que solo te lo he dicho un millón de veces.",
    "Hoy he descubierto que eres más dulce que la miel.",
    "Me hipnotizas y me hechizas a todas horas.",
    "Me perdería a todas horas en tus ojos.",
    "Tus ojos son el conjuro contra mi mal día.",
    "Y una cosa puedo jurar: yo que me enamoraré de tus alas, jamás te las voy a querer cortar.",
    "Viajar a Marte o al cuarto de la plancha. Pero contigo.",
    "Mirar es una cosa, que me mires tú es otro verbo diferente.",
    "Eres la excepción a todo eso que dije que nunca haría",
    "Te quiero libre, y me quiero libre contigo",
    "¿Y tú que sabes del amor? Yo te sé a ti de memoria",
    "Soy feliz cuando me miras.",
    "Comenzaste robándome una sonrisa y ahora te has quedado mi corazón",
    "Aún en la oscuridad puedo sentir la luz de tu sonrisa",
    "Te veo y se me va el sueño",
    "Me gustas, me gustas, me gustas, me gustas... ¿sabes que me gustas?",
    "Me haces sentir mis instintos más salvajes: te devoraría a besos.",
    "Quiero hacer contigo lo que la primavera hace con los cerezos.",
    "Quédate con quien te bese el alma, la piel te la besa cualquiera.",
}

def getRandom():
    global frases
    return random.choice(list(frases))

@app.launch
def launch_handler(item):
    return alexandra.respond(ssml="<speak>"+getRandom()+"</speak>")

@app.intent('amor')
def octoalert_intent():
    return alexandra.respond(ssml="<speak>"+getRandom()+"</speak>")

if __name__ == '__main__':
    app.run('0.0.0.0', 9997, debug=True)
