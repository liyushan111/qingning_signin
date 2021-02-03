with open("data.json", "r+") as f:
            data = f.read()
            data = json.loads(data)
            print(data)
      
