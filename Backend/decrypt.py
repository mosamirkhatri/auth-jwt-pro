encrypted_request = "..."

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

from base64 import b64decode

private_key = """-----BEGIN RSA PRIVATE KEY-----...-----END RSA PRIVATE KEY-----"""


def decrypt_rsa(encrypted_data):
    key = RSA.import_key(private_key)
    cipher = PKCS1_v1_5.new(key)
    message = cipher.decrypt(encrypted_data, None)
    return message.decode("utf-8")


print(decrypt_rsa(b64decode(encrypted_request)))
