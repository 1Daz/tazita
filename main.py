from src.click import runClick

if __name__ == "__main__":
    data = [
        {
            "ID": 1, 
            "Description": "Hacer comida", 
            "Completed": True
        },
        {
            "ID": 2,
            "Description": "Ir a clase",
            "Completed": False
        }
        
        ]
    print(data["Description"])
    print(data["ID"])
    print(data["Completed"])
    