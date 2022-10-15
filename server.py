import socketserver
import sps

class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        print(f"size of mesg : {len(self.data)}")
        #       DO SMTHG WITH DATA
        sps.handle_connection(self.data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 31300

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
