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
    zapi.user.logout()

    events = result['result'] # Lista de eventos

    #inicializar listas de name, severity y triggerid

    name = [None] * num_events
    severity = [None] * num_events
    triggerid = [None] * num_events

    type = [None] * num_events

    # Obtener name, severity y el relatedObject -> triggerid , de los 5 eventos recogidos
    cont=0

    for event in events:

        name[cont] = event['name'] 
        severity[cont] = int(event['severity'])
        triggerid[cont] = event['relatedObject']['triggerid']

        # rellenar el type según severity : 0-Not clasified, 1-Information, 2-Warning, 3-Average, 4-High, 5-Disaster

        if severity[cont] == 0:
            type[cont] = 'Not clasified'
        elif severity[cont] == 1:
            type[cont] = 'Information'
        elif severity[cont] == 2:
            type[cont] = 'Warning'
        elif severity[cont] == 3:
            type[cont] = 'Average'
        elif severity[cont] == 4:
            type[cont] = 'High'
        elif severity[cont] == 5:
            type[cont] = 'Disaster'
        
        cont += 1

    # Crear un string con los eventos recogidos

    eventos = ""
    eventos += '\n Eventos del servidor más recientes: \n'
    triggerids_conocidos = [None] * num_events

    for i in range(num_events):
        # si el trigerid ya está en triggerids conocidos no añadimos el evento
        if triggerid[i] not in triggerids_conocidos:
            triggerids_conocidos[i] = triggerid[i]
            eventos += f'{name[i]}: Tipo de evento:{type[i]} relacionado con el trigger {triggerid[i]} \n'

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