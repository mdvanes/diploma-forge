with open("assets/template.pdf", "rb") as f:
    content = f.read()
start = content.find(b"stream\n") + 7
end = content.find(b"endstream")
stream = content[start:end].strip()
def ascii85_decode(data):
    result = []
    i = 0
    while i < len(data):
        if data[i:i+2] == b"~>": break
        if data[i] == ord("z"):
            result.extend([0,0,0,0]); i+=1; continue
        chunk = data[i:i+5]; i+=5; n=0
        for b in chunk: n=n*85+(b-33)
        for j in range(3,-1,-1): result.append((n>>(8*j))&0xFF)
    return bytes(result)
import zlib
a85=ascii85_decode(stream)
decoded=zlib.decompress(a85)
print(decoded.decode("latin-1"))
