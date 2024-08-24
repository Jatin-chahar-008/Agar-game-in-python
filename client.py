import socket
import _pickle as pickle
import ssl
import os
class Network:
    """
    class to connect, send and recieve information from the server

    need to hardcode the host attirbute to be the server's ip
    """
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.settimeout(10.0)
        self.host = "10.30.202.12"
        self.port = 5555
        self.addr = (self.host, self.port)

    # if not os.path.exists(CLIENT_FILES_DIR):
    #     os.makedirs(CLIENT_FILES_DIR)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ssl_context=ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    # ssl_context.load_verify_locations("server-cert.pem")
                                  
    def connect(self, name):
        """
        connects to server and returns the id of the client that connected
        :param name: str
        :return: int reprsenting id
        """
        self.client.connect(self.addr)
        self.client.send(str.encode(name))
        val = self.client.recv(8)
        return int(val.decode()) # can be int because will be an int id

    def disconnect(self):
        """
        disconnects from the server
        :return: None
        """
        self.client.close()

    def send(self, data, pick=False):
        """
        sends information to the server

        :param data: str
        :param pick: boolean if should pickle or not
        :return: str
        """
        try:
            if pick:
                self.client.send(pickle.dumps(data))
            else:
                self.client.send(str.encode(data))
            reply = self.client.recv(8192)
            try:
                reply = pickle.loads(reply)
            except Exception as e:
                print(e)

            return reply
        except socket.error as e:
            print(e)



