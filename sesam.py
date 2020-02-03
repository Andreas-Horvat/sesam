from hashlib import pbkdf2_hmac


class PasswordGenerator():
    def __init__(self):
        self.small_letters = list('abcdefghijklmnopqrstuvwxyz')
        self.big_letters = list('ABCDEFGHJKLMNPQRTUVWXYZ')
        self.numbers = list('0123456789')
        self.special_characters = list('#!"§$%&/()[]{}=-_+*<>;:.')
        self.password_characters = self.small_letters + self.big_letters + self.numbers + self.special_characters
        self.salt = 'sehhhrrrlaanngeessssselbstgewähltesSaltverwenden'

    def get_password(self, domain, master_password, passord_length):
        hashed_bytes = self.get_hashed_bytes(domain, master_password)
        number = int.from_bytes(hashed_bytes, byteorder='big')
        password = ''
        while number > 0 and len(password) < passord_length:
            password = password + self.password_characters[number % len(self.password_characters)]
            number = number // len(self.password_characters)
        return password

    def get_hash_string(self, domain, master_password):
        return domain + master_password

    def get_hashed_bytes(self, domain, master_password):
        hash_string = self.get_hash_string(domain, master_password)
        return pbkdf2_hmac('sha512', hash_string.encode('utf-8'), self.salt.encode('utf-8'), 4096)

