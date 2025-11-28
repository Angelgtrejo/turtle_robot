#!/usr/bin/env python3
"""
Proyecto: Toggle LED desde ROS hacia Arduino Uno
Autor: Jesús López
Fecha: 25/11/2025

Descripción:
Este script en Python actúa como publisher en ROS. Envía mensajes
std_msgs/Bool al tópico /toggle_led, que son recibidos por el Arduino Uno
a través de rosserial. El LED conectado al pin 13 se enciende o apaga
según el valor publicado.

Entorno:
- Ubuntu 20.04
- ROS Noetic
- Arduino Uno con rosserial_arduino
- Submódulo turtle_robot_sketchbook en branch feature/arduino_uno

Flujo ROS:
1. Este nodo Python publica mensajes Bool en el tópico /toggle_led.
2. El puente rosserial (rosrun rosserial_python serial_node.py /dev/ttyUSB0)
   transmite los mensajes al Arduino Uno por USB.
3. El Arduino, como subscriber, recibe el mensaje y enciende/apaga el LED.
4. Se puede alternar automáticamente o controlar manualmente el estado.

Ejemplo de ejecución:
    chmod +x scripts/toggle_led.py
    rosrun COYOTE_ROBOT toggle_led.py

Ejemplo de publicación manual:
    rostopic pub /toggle_led std_msgs/Bool "data: true"
    rostopic pub /toggle_led std_msgs/Bool "data: false"

Objetivo didáctico:
- Mostrar cómo un nodo Python en ROS puede controlar hardware real.
- Practicar la comunicación publisher → subscriber entre ROS y Arduino.
- Documentar claramente el entorno y flujo para reproducibilidad.
"""

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool

def remote_led():
    # Inicializa el nodo ROS
    rospy.init_node('remote_led_publisher', anonymous=True)

    # Publisher en el tópico correcto → Arduino escucha aquí
    pub = rospy.Publisher('/toggle_led', Bool, queue_size=10)

    rospy.loginfo("Control del LED listo.")
    
    rospy.loginfo("Presiona 'o' (True)")
    
    rospy.loginfo("Presiona 's' (False)")
    
    rospy.loginfo("Ctrl+C para salir.\n")

    while not rospy.is_shutdown():
        tecla = input("Ingresa tecla (o/s): ")

        msg = Bool()

        if tecla.lower() == "o":
            msg.data = True
            pub.publish(msg)
            rospy.loginfo("(True enviado)")

        elif tecla.lower() == "s":
            msg.data = False
            pub.publish(msg)
            rospy.loginfo("(False enviado)")

        else:
            rospy.logwarn("Tecla no válida. Usa 'o' o 's'.")
     
        rospy.sleep(0.1)   # Pequeña pausa para estabilidad ROS

if __name__ == '__main__':
    try:
        remote_led()
    except rospy.ROSInterruptException:
        pass
