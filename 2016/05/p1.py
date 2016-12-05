import hashlib

def main():
    door_id = 'abbhdwsy'
    password = ''

    inc = 0
    while len(password) < 8:
        check = door_id + str(inc)
        out = hashlib.md5(check).hexdigest()
        if out.startswith('00000'):
            password += out[5]
        inc += 1
    print password
if __name__ == "__main__":
    main()
