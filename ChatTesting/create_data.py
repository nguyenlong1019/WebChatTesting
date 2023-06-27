import random
import string
import csv

def generate_password(existing_passwords=[], length=9, num_passwords=1):
    common_passwords = ["password", "123456", "qwerty", "abc123"]  # Các mật khẩu phổ biến
    generated_passwords = []
    while len(generated_passwords) < num_passwords:
        password = ''
        while not password or password in existing_passwords or password in common_passwords or not password[0].isalpha():
            password = random.choice(string.ascii_letters)  # Chọn một chữ cái đầu tiên
            password += ''.join(random.choices(string.ascii_letters + string.digits, k=length - 1))  # Thêm các chữ cái và chữ số còn lại
            password = ''.join(random.sample(password, len(password)))  # Trộn ngẫu nhiên các ký tự
        existing_passwords.append(password)
        generated_passwords.append(password)
    return generated_passwords

# Sử dụng hàm để tạo danh sách mật khẩu
passwords = generate_password(num_passwords=5)
print(passwords)

username_list = ['trieutung', 'nhatminh', 'nguyenlong', 'Jennifer', 'Brian']


def combine_credentials(usernames, passwords):
    combined_credentials = []
    combined_pairs = list(zip(usernames, passwords))
    random.shuffle(combined_pairs)
    for pair in combined_pairs:
        credentials = pair[0] + ':' + pair[1]
        combined_credentials.append(credentials)
    return combined_credentials

# Ghép ngẫu nhiên username và password
combined_creds = combine_credentials(username_list, passwords)
print(combined_creds)


def write_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['STT', 'Username', 'Password'])  # Ghi dòng tiêu đề
        for i, item in enumerate(data, start=1):
            username, password = item.split(':')
            writer.writerow([i, username, password])

# Gọi hàm để ghi danh sách username và password vào file CSV
write_to_csv(combined_creds, 'credentials1.csv')