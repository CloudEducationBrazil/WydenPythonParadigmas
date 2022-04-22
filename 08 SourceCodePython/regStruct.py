import struct
client = ('6s i i 8s f i')
umClient = struct.pack(client, b"heleno", 0, 1, b"123456", 500.00, 0)
umClient = struct.pack(client, b"paulo", 3, 5, b"123456", 800.00, 1)
print (struct.unpack(client, umClient))