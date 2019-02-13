import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_addr =('localhost',10000)
print(f"start up on {server_addr}")
server.bind(server_addr)

server.listen(5)

inputs=[server]
outputs=[]
# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:
    print("wait for the next event")
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    for s in readable:
        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            print('new connection from ', client_address)
            connection.setblocking(0)
            inputs.append(connection)
            # Give the connection a queue for data we want to send
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print(f'received {data} from {s.getpeername()}')
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print('closing ', client_address, ' after reading no data')
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                Remove message queue
                message_queues.pop(s, None)

    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
            next_msg = "send back:".encode()+next_msg
            print('sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)
        except queue.Empty:
            # No messages waiting so stop checking for writability.
            print('output queue for ', s.getpeername(), ' is empty')
            outputs.remove(s)

    # Handle "exceptional conditions"
    for s in exceptional:
        print('handling exceptional condition for', s.getpeername())
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        # Remove message queue
        message_queues.pop(s, None)

print("end. input is empty.")