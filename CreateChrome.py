import os
import shutil
import win32com.client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 源文件夹路径（包含快捷方式文件）
source_folder = r"C:\Users\zng20\Desktop\Google"  # 替换为你的源文件夹路径

# 目标文件夹路径（将快捷方式复制到此文件夹）
destination_folder = r"C:\Users\zng20\Desktop\Google"  # 替换为你的目标文件夹路径

# MetaMask 和 OKX 扩展的本地文件路径
metamask_extension = r"D:\MetaMask"  # 替换为 MetaMask 解压的文件夹路径
okx_extension = r"D:\OKX"  # 替换为 OKX 解压的文件夹路径

# 助记词文件路径
mnemonic_file = r"C:\Users\zng20\Desktop\助记词.txt"  # 替换为存储助记词的文件路径

# MetaMask 扩展 ID
metamask_extension_id = "nkbihfbeogaeaoehlefnkodbefgpgknn" 

okx_extension_id ="pbpjkcldjiffchgbbndmhojiacbgflha"

# 批量复制并重命名快捷方式并修改目标
def copy_and_rename_shortcuts():
    # 获取源文件夹中的所有文件
    try:
        files = os.listdir(source_folder)
    except FileNotFoundError:
        print(f"错误：源文件夹路径 {source_folder} 无效或找不到。")
        return
    
    # 过滤出所有快捷方式文件（.lnk文件）
    lnk_files = [file for file in files if file.endswith('.lnk')]

    if len(lnk_files) == 0:
        print("错误：源文件夹中没有找到快捷方式文件 (.lnk)。")
        return
    
    # 假设源文件夹中只有一个快捷方式文件
    source_file = os.path.join(source_folder, lnk_files[0])  # 获取源文件中的第一个快捷方式文件

    # 需要复制并重命名的快捷方式数量
    max_files = 100

    # 循环复制快捷方式文件，并重命名
    for i in range(max_files):
        # 目标文件名修改为从1.lnk到100.lnk
        destination_file = os.path.join(destination_folder, f"{i+1}.lnk")

        try:
            # 复制快捷方式文件到目标文件夹，并重命名
            shutil.copy(source_file, destination_file)
            print(f"快捷方式已复制并重命名为 {i+1}.lnk")

            # 使用 win32com 修改快捷方式的目标属性
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(destination_file)
            
            # 根据当前文件名设置目标路径中的 user-data-dir
            user_data_dir = f"D:\\谷歌多开\\钱包{i+1}"  # 根据文件名调整 user-data-dir
            target_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            
            # 修改后的命令行参数，确保多个扩展通过逗号分隔
            arguments = f'--user-data-dir="{user_data_dir}" ' \
                        f'--load-extension="{metamask_extension},{okx_extension}"'
            
            # 设置目标路径和参数
            shortcut.TargetPath = target_path  # 设置目标程序路径
            shortcut.Arguments = arguments  # 设置附加参数
            
            shortcut.Save()  # 保存修改后的快捷方式

            print(f"快捷方式 {i+1}.lnk 的目标已修改，user-data-dir 设置为 {user_data_dir}。")
        except Exception as e:
            print(f"复制或修改快捷方式时发生错误: {e}")

# 执行复制和重命名操作
copy_and_rename_shortcuts()
