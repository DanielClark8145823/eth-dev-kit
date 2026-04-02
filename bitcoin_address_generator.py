import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

def sha256(data):
    return hashlib.sha256(data).digest()

def ripemd160(data):
    h = hashlib.new('ripemd160')
    h.update(data)
    return h.digest()

def generate_btc_address():
    # 生成私钥
    private_key = SigningKey.generate(curve=SECP256k1)
    private_key_hex = private_key.to_string().hex()
    
    # 生成公钥
    public_key = private_key.get_verifying_key().to_string()
    public_key_full = b'\x04' + public_key
    
    # 生成比特币地址
    pub_sha = sha256(public_key_full)
    pub_rip = ripemd160(pub_sha)
    versioned = b'\x00' + pub_rip
    checksum = sha256(sha256(versioned))[:4]
    address_bytes = versioned + checksum
    btc_address = base58.b58encode(address_bytes).decode()

    print("="*50)
    print("🔥 比特币离线地址生成成功")
    print(f"私钥: {private_key_hex}")
    print(f"地址: {btc_address}")
    print("="*50)
    return btc_address, private_key_hex

if __name__ == "__main__":
    generate_btc_address()
