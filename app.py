from base import app

port_number = 1111

if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=port_number)
