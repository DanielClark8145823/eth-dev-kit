from eth_account import Account
from mnemonic import Mnemonic
import secrets

# 开启助记词功能
Account.enable_unaudited_hdwallet_features()

def generate_eth_wallet():
    # 生成12位助记词
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate(strength=128)
    
    # 从助记词生成钱包
    account = Account.from_mnemonic(mnemonic)
    
    print("="*50)
    print("🔥 以太坊离线钱包生成成功")
    print(f"助记词: {mnemonic}")
    print(f"地址: {account.address}")
    print(f"私钥: {account.key.hex()}")
    print("="*50)
    return account

if __name__ == "__main__":
    generate_eth_wallet()
