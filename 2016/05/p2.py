import hashlib

def main():
    door_id = 'abbhdwsy'
    password = [' '] * 8 

    inc = 0
    while ' ' in password:
        check = door_id + str(inc)
        out = hashlib.md5(check).hexdigest()
        if out.startswith('00000') and out[5] < '8':
            position = int(out[5])
            if password[position] == ' ': 
                password[int(position)] = out[6] 
        inc += 1
    print password

if __name__ == "__main__":
    main()
