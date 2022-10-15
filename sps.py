#simple plot server
#here is the bussiness logic
import json
import socket
import matplotlib.pyplot as plt
import pyformulas as pf
#easy global config 
HOST, PORT = "localhost", 31300

## request parsing
#common
def handle_connection(request_str : str):
    req = json.loads(request_str)
    if req.get("req_type") == "plot&data":
        handle_plot(req)
#plot
def handle_plot(request):
    fig = plt.figure(1)
    plt.plot(
        request.get("plot_spe").get("data"),
        figure = fig
    )
    plt.draw()
    plt.pause(0.001)

## plot utility
#simple plot
def plot(data,title='',x_axis_label='',y_axis_label=''):
    dataOut = {
        "req_type" : "plot&data",
        "plot_spe" : {
            "data" : data,
        }
    }
    #TODO : refactor this fleche vers le bas
    if title != '':
        dataOut["plot_spe"]["title"] = title
    if x_axis_label != '':
        dataOut["plot_spe"]["x_axis_label"] = x_axis_label
    if y_axis_label != '':
        dataOut["plot_spe"]["y_axis_label"] = y_axis_label

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(json.dumps(dataOut) + "\n", "utf-8")) 
    
#plot numpy array

if __name__ == '__main__':
    plot([1,2,3,2,1,2,3,5,3,5,5,5]) # for test purpose