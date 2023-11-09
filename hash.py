import hashlib

def find_password(start, stop, num_of_letters, md5_password):
    all_characters = [chr(i) for i in range(ord('a'), ord('z')+1)]
#[chr(i) for i in range(ord('A'), ord('Z')+1)]
#[chr(i) for i in range(ord('0'), ord('9')+1)]



# maybe make num of letters a tupple for range


    def generate_combinations(code, num_of_letters):
        if len(code) == num_of_letters:
            md5_hash = hashlib.md5(code.encode()).hexdigest()
            if md5_hash == md5_password:
                return code
        elif len(code) < num_of_letters:
            for char in all_characters:
                new_code = code + char
                result = generate_combinations(new_code, num_of_letters)
                if result:
                    return result

    for char in all_characters[all_characters.index(start):all_characters.index(stop)+1]:
        result = generate_combinations(char, num_of_letters)
        if result:
            return result

    return None

start = 'a'
stop = 'b'
num_of_letters = 3
md5_password = '45a944c4b06807c66113939489658873'
result = find_password(start, stop, num_of_letters, md5_password)
if result:
    print(result)
else:
    print("Password not found.")
