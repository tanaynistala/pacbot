from gpiozero import PhaseEnableMotor

motor = PhaseEnableMotor(19, 26)
motor.forward()
