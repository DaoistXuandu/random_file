from pwn import *  # type: ignore
import time

def interactive_local(binary_path):
    print(f"Running {binary_path} locally. You can now interact with the process.")

    cur = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=}{"
    pos = ['N', 'E', 'T', 'S', 'O', 'S', '{', 'L']
    cnt = 0

    try:
        while True:  # Keep running until solved
            conn = process([binary_path])  # Run ./challpub instead of remote connection
            print(f"[+] Trying character: {cur[cnt]}")
            
            while True:
                data = conn.recv(timeout=2).decode('utf-8', errors='ignore')  # Prevent blocking
                if not data:
                    continue
                
                datas = data.replace("\n", " ").split(" ")

                if datas[0] == "False":  # Wrong character → try next
                    print(f"[-] Incorrect: {cur[cnt]}")
                    conn.close()
                    cnt = (cnt + 1) % len(cur)  # Try next character
                    break  # Restart loop with new process

                elif datas[0] == "Masukkan":
                    conn.sendline("eA2e".encode())  # Send password
                    print("[+] Sent password")

                elif datas[0] == "What's":
                    index = int(datas[3][0]) if datas[3][0].isdigit() else 0

                    if index >= len(pos):  # If index is not in pos, try new character
                        if index > len(pos):
                            pos.append(cur[cnt])
                            cnt = (cnt + 1) % len(cur)  # Move to next character

                        time.sleep(1)
                        conn.sendline(cur[cnt].encode()) 
                    else:
                        print(f"[+] Resending pos[{index}]: {pos[index]}")
                        conn.sendline(pos[index].encode()) 
                else:
                    continue 

            conn.close()                
            print("[*] Current Pos:", pos)
    
    except EOFError:
        print("Process exited.")
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        conn.close()
        print("Process closed.")

if __name__ == "__main__":
    binary_path = "./challpub"  # Path to local binary
    interactive_local(binary_path)

