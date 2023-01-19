import socket, cv2, pickle, struct, imutils
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ledPin = 12
buttonPin = 16

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 2001
host_ip = '192.168.172.249'
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(3)
print("LISTENING AT:",socket_address)

def capture_and_send(vid):
	for _ in range(5):
		_, frame = vid.read()
		# frame = imutils.resize(frame, width=320)
		a = pickle.dumps(frame)
		message = struct.pack("Q",len(a))+a
		client_socket.sendall(message)

# Socket Accept
while True:
	client_socket, addr = server_socket.accept()
	print('GOT CONNECTION FROM:', addr)
	if client_socket:
		while True:
			buttonState = GPIO.input(buttonPin)
			if buttonState == False:
				GPIO.output(ledPin, GPIO.HIGH)
				print(True)
				vid = cv2.VideoCapture(0)
				capture_and_send(vid)
				vid.release()
			else:
				GPIO.output(ledPin, GPIO.LOW)

client_socket.close()