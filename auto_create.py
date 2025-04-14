from solders.keypair import Keypair
from solders.pubkey import Pubkey
import base58
import pandas as pd

def create_solana_wallet():
    keypair = Keypair()
    private_key_bytes = keypair.to_bytes()
    private_key_base58 = base58.b58encode(private_key_bytes).decode("utf-8")
    public_key_str = str(keypair.pubkey())

    return {
        "public_key": public_key_str,
        "private_key": private_key_base58
    }

def generate_wallets_to_excel(count):
    wallets = [create_solana_wallet() for _ in range(count)]
    df = pd.DataFrame(wallets)
    df.to_excel("solana_wallets.xlsx", index=False)
    print(f"✅ Đã tạo {count} ví và lưu vào solana_wallets.xlsx")

if __name__ == "__main__":
    num = int(input("🔢 Nhập số lượng ví Solana cần tạo: "))
    generate_wallets_to_excel(num)
