from internal.server.server import server

def main():
    err = server()
    if err != None:
        print("Server Error:", err)
        exit(1)
        
if __name__ == "__main__":
    main()