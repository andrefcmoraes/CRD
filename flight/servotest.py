import RPi.GPIO as GPIO
import time

# Configura o modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Define o pino GPIO 18 como saída de PWM
SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configura o PWM no pino 18 com frequência de 50 Hz (ideal para a maioria dos servos)
pwm = GPIO.PWM(SERVO_PIN, 50)

# Inicia o PWM com ciclo de trabalho de 0 (servo parado)
pwm.start(0)

# Função para mover o servo para um ângulo
def set_angle(angle):
    # Calcula o ciclo de trabalho (duty cycle) para o ângulo
    # A fórmula básica é: (ângulo / 18) + 2.5
    duty = (angle / 18) + 2.5
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1) # Dá um tempo para o servo se mover
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Mover para 0 graus
        set_angle(0)
        time.sleep(2)

        # Mover para 90 graus
        set_angle(90)
        time.sleep(2)

        # Mover para 180 graus
        set_angle(180)
        time.sleep(2)

except KeyboardInterrupt:
    # Se o usuário pressionar Ctrl+C, limpa o PWM e os pinos
    pwm.stop()
    GPIO.cleanup()
    print("Programa finalizado.")
