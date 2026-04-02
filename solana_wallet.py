from solders.keypair import Keypair
from base58 import b58encode

def generate_solana_wallet():
    # 生成Solana密钥对
    keypair = Keypair()
    private_key = b58encode(keypair.secret()).decode()
    public_key = str(keypair.pubkey())

    print("="*50)
    print("⚡ Solana钱包生成成功")
    print(f"私钥: {private_key}")
    print(f"公钥(地址): {public_key}")
    print("="*50)
    return private_key, public_key

if __name__ == "__main__":
    generate_solana_wallet()
