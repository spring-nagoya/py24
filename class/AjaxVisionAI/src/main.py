from internal.server.server import  Server

def main():
    err = Server().run()
    if err != None:
        print("Server Error:", err)
        exit(1)
        
if __name__ == "__main__":
    main()