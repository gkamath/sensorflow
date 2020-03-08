import zmq
import socket

class Publisher:
    def __init__(self, connection_params):

        self.cpars = connection_params
        self._mbus_host = connection_params['MESSAGE_BUS_HOST']
        try:
            self._mbus_host = socket.gethostbyname(self._mbus_host)
        except Exception:
            pass
        self._mbus_pub_port = int(connection_params['MESSAGE_BUS_PUB_PORT'])
        self._context = zmq.Context()
        try:
            self._publisher = self._context.socket(zmq.PUB)
            mbus_pub_host = "tcp://" + self._mbus_host + ":" + str(self._mbus_pub_port)
            self._publisher.connect(mbus_pub_host)
        except Exception as e:
            print(e)

    def to_topic(self, topic):
        def fn(x):
            self._publisher.send_multipart([topic.encode('ascii', 'replace'), bytes(str(x), 'utf-8')])
            #self._publisher.send_multipart([topic.encode('ascii', 'replace'), x[0]])
            #self._publisher.send_multipart([zmq.Frame(bytes(topic, 'utf-8')), zmq.Frame(bytearray(str(x), 'utf-8'))])

        return fn
