import random

from pyzabbix.api import ZabbixAPI

def eventos() -> str:
    # Create ZabbixAPI class instance
    zapi = ZabbixAPI(url='http://192.168.56.105/zabbix/', user='Admin', password='zabbix')
    num_events = 5
    result = zapi.do_request('event.get', {
        'output': 'extend',
        'limit': 5,  # Obtener solo el evento más reciente
        'sortfield': 'clock',
        'sortorder': 'DESC',
        'selectRelatedObject': ['objectid']
    })

    events = result['result'] # Lista de eventos

    #inicializar listas de name, severity y triggerid

    name = [None] * num_events
    severity = [None] * num_events
    triggerid = [None] * num_events

    type = [None] * num_events

    # Obtener name, severity y el relatedObject -> triggerid , de los 5 eventos recogidos

    for event in events:
        name[0] = event['name'] 
        severity[0] = int(event['severity'])
        triggerid[0] = event['relatedObject']['triggerid']

        # rellenar el type según severity : 0-Not clasified, 1-Information, 2-Warning, 3-Average, 4-High, 5-Disaster

        if severity[0] == 0:
            type[0] = 'Not clasified'
        elif severity[0] == 1:
            type[0] = 'Information'
        elif severity[0] == 2:
            type[0] = 'Warning'
        elif severity[0] == 3:
            type[0] = 'Average'
        elif severity[0] == 4:
            type[0] = 'High'
        elif severity[0] == 5:
            type[0] = 'Disaster'

    # Crear un string con los eventos recogidos

    eventos = ""

    for i in range(num_events):
        eventos += f'{name[i]}: {severity[i]}:{type[i]} relacionado con el trigger {triggerid[i]} \n'

    zapi.user.logout()

    return eventos

def handle_response(message) -> str:
    """Handles responses to messages from the user."""
    p_message = message.lower()

    if p_message == "hola":
        return "Hola, ¿cómo estás?"
    
    if p_message == "adios":
        return "Hasta luego, nos vemos pronto!"
    
    if p_message == "bien":
        return "Me alegro! Escribe !eventos para ver los eventos del servidor más recientes."
    
    if p_message == "mal":
        return "Oh, lo siento. Escribe !eventos para ver los eventos del servidor más recientes."
    
    if p_message == '!help':
        return 'Escribe !eventos para ver los eventos del servidor más recientes.'
    
    if p_message == '!eventos':
        return eventos()
    
    return "Lo siento no te entiendo. Escribe !help para ver los comandos disponibles."