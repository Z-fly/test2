import code
import sys
import os

def main():

    print(__compiled__.containing_dir,1111,'\n')
    print(os.path.dirname(sys.argv[0]),2222,'\n')
    print(__file__,3333,'\n')
    
    
    banner = "模拟 Python 控制台，输入 exit() 退出"
    console = code.InteractiveConsole()
    console.interact(banner=banner)

if __name__ == '__main__':
    main()

