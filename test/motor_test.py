from gpiozero import PhaseEnableMotor

motor = PhaseEnableMotor(35, 37)
motor.forward()
