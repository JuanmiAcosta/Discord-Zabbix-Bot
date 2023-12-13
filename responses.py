import random

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
    
    """
    if p_message == '!eventos':
        return eventos()
    """
    
    return "Lo siento no te entiendo. Escribe !help para ver los comandos disponibles."