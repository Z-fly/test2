import code

def main():
    
    banner = "模拟 Python 控制台，输入 exit() 退出"
    console = code.InteractiveConsole()
    console.interact(banner=banner)

if __name__ == '__main__':
    main()
