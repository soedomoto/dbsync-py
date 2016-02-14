from dbsync.api.ring import Ring
from tornado import ioloop

from thrift import TTornado
from thrift.protocol import TBinaryProtocol

from dbsync.api.dbms import DBMS
from dbsync.provider.MySQL import MySQL
from dbsync.ring.RingHandler import RingHandler
from dbsync.thrift.ThriftServer import ThriftServer

__author__ = 'soedomoto'
__project__ = 'dbsync'

listenAddr = '0.0.0.0'
listenPort = 9090


def main():
    dbmsP = DBMS.Processor(MySQL())
    ringP = Ring.Processor(RingHandler())

    server = ThriftServer(listenAddr, listenPort, [dbmsP, ringP])
    server.start()

if __name__ == "__main__":
    main()