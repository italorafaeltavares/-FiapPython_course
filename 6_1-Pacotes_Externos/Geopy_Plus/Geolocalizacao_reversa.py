from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

latitude  = float(input("Latitude...: "))
longitude = float(input("Longitude...: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")

if resultado[0] != "None":
    print("Endereco completo.: ", resultado)
    print("Bairro.............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Regiao............: ", resultado[3])
    
# Exemplos: Latitude...: -23.6740406 | Longitude...: -46.62340890000015    
