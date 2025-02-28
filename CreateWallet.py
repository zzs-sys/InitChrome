import os
from eth_account import Account
from mnemonic import Mnemonic

Account.enable_unaudited_hdwallet_features()
mnemonic = Mnemonic("english").generate(strength=128)

# 使用助记词生成钱包
seed = Mnemonic.to_seed(mnemonic)  # 将助记词转换为种子
account = Account.from_mnemonic(mnemonic)

wallet_address = account.address
private_key = account.key.hex()

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

#创建文件路径
file_path = os.path.join("E:","wallet.txt")

# 判断文件是否存在，如果不存在就创建并写入数据，否则追加数据
file_exists = os.path.exists(file_path)

# 打开文件，使用 'a' 模式来追加数据
with open(file_path, "a") as file:
    if not file_exists:
        # 如果文件不存在，写入标题或其他必要的信息
        file.write("Wallet Address, Private Key and Mnemonic:\n\n")

    # 追加钱包地址、私钥和助记词
    file.write(f"Wallet Address: {wallet_address}\n")
    file.write(f"Private Key: {private_key}\n")
    file.write(f"Mnemonic: {mnemonic}\n")
    file.write("\n")  # 每条记录后添加一个换行符

print(f"Wallet address, private key, and mnemonic have been saved to: {file_path}")

