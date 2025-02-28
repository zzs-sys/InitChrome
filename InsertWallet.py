import os
import shutil
import win32com.client
from selenium import webdriver
from eth_account import Account
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mnemonic import Mnemonic
import pyautogui
import pyperclip
import time

okx_extension_id ="pbpjkcldjiffchgbbndmhojiacbgflha"

metamask_extension = r"D:\MetaMask"  # 替换为 MetaMask 解压的文件夹路径
okx_extension = r"D:\OKX"  # 替换为 OKX 解压的文件夹路径

#读取助记词
def extract_mnemonics(file_path):
    mnemonics = []  # 存储所有助记词
    with open(file_path, 'r', encoding='utf-8') as file:
        # 按行读取文件内容
        for line in file:
            # 检查当前行是否包含 'Mnemonic:'
            if 'Mnemonic:' in line:
                # 提取 'Mnemonic:' 后面的内容并去掉多余的空格
                mnemonic = line.split('Mnemonic:')[1].strip()
                mnemonics.append(mnemonic)  # 将助记词添加到列表中
    return mnemonics  # 返回助记词列表
def import_metamask_mnemonic(user_data_dir, mnemonic):
    print(user_data_dir)
    
    # 打开带有扩展的 Chrome 浏览器
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={user_data_dir}")  # 使用独立的用户数据目录
    options.add_argument(f'--load-extension={okx_extension}')  # 加载扩展

    # 构建 MetaMask 扩展的 URL
    metamask_url = f"chrome-extension://pbpjkcldjiffchgbbndmhojiacbgflha/popup.html"

    # 创建 WebDriver 实例
    driver = webdriver.Chrome(options=options)
    time.sleep(3)

    # 模拟点击
    pyautogui.click(1179, 34)
    pyautogui.click(981, 73)
    pyperclip.copy(metamask_url) # 复制助记词到剪贴板
    pyautogui.hotkey('ctrl', 'v') # 粘贴助记词
    # 模拟按下回车键
    pyautogui.press('enter') #打开欧意钱包网站
    time.sleep(0.5)
    pyautogui.click(1335, 1240) #点击导入已有钱包
    time.sleep(0.5)
    pyautogui.click(1105, 413) #点击助记词导入
    time.sleep(0.5)
    pyautogui.click(2053, 356) # 点击助记词第一个选框
    pyperclip.copy(mnemonic) # 复制助记词到剪贴板
    pyautogui.hotkey('ctrl', 'v') # 粘贴助记词
    pyautogui.click(2165, 808) # 点击确认
    time.sleep(0.5)
    pyautogui.click(2069, 466) # 密码验证
    time.sleep(0.3)
    pyautogui.click(2196, 798) # 下一步
    time.sleep(0.3)
    pyautogui.click(2011, 384) # 点击助记词第一个选框
    pyautogui.typewrite("183267..",interval=0.1)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.typewrite("183267..",interval=0.05)
    pyautogui.click(2129, 813)# 点击确认
    time.sleep(3) #等待加载 
    pyautogui.click(2165, 800)# 点击确认
    time.sleep(0.5)
    driver.close()  # 只关闭当前窗口
    pyautogui.click(2379, 15)
    time.sleep(3.5)
    pyautogui.click(1085, 28)
    time.sleep(1.5)

# 指定文件路径
file_path = 'E:/wallet.txt'  # 替换为你实际的文件路径

# 调用函数提取所有的 Mnemonic
mnemonics = extract_mnemonics(file_path)    

#创建文件路径
file_path = os.path.join("E:","Create.txt")
# annual kidney asthma until beauty draw that globe mesh cram unveil gun
file_exists = os.path.exists(file_path)

# 输出提取的所有助记词
if mnemonics:
    print(f"Found {len(mnemonics)} mnemonics:")
    for i, mnemonic in enumerate(mnemonics, start=1):
        if i > 100:
            break  # 当 i 大于 100 时，结束循环
        user_data_dir = f"D:\\谷歌多开\\钱包{i}"
        import_metamask_mnemonic(user_data_dir,mnemonic) 
        print(f"Mnemonic {i}: {mnemonic},{user_data_dir}")
else:
    print("Mnemonic not found.")

