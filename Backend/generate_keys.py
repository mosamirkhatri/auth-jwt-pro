from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("./private_key.pem", "wb") as file:
    file.write(private_key)

with open("./public_key.pem", "wb") as file:
    file.write(public_key)
