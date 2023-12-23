import random
import string

class EmailAndPasswordGenerator:
    def __init__(self, domains, password_length=12):
        self.domains = domains
        self.password_length = password_length

    def generate_email(self, username_length=8):
        username = self._generate_random_string(username_length)
        domain = random.choice(self.domains)
        return f'{username}@{domain}'

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return self._generate_random_string(self.password_length, characters)

    def _generate_random_string(self, length, char_set=string.ascii_lowercase):
        return ''.join(random.choice(char_set) for _ in range(length))

if __name__ == "__main__":
    email_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']

    generator = EmailAndPasswordGenerator(email_domains)

    for _ in range(5):
        email = generator.generate_email()
        password = generator.generate_password()
        print(f'Email: {email}\nPassword: {password}\n')
