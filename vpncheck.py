import subprocess
import time

def main():
    process = subprocess.Popen(["nordvpn", "-c"], stdout=subprocess.PIPE)
    process.wait()
if __name__ == "__main__":
    main()