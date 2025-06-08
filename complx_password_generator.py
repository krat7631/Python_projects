import string
import secrets

class PasswordGenerator:
    def __init__(self,
                 length=16,
                 use_upper=True,
                 use_lower=True,
                 use_digits=True,
                 use_symbols=True,
                 exclude_ambiguous=True,
                 custom_chars="",
                 num_passwords=1):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.exclude_ambiguous = exclude_ambiguous
        self.custom_chars = custom_chars
        self.num_passwords = num_passwords

        self.ambiguous_chars = 'Il1O0'
        self.symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        self.char_pool = self._build_char_pool()

    def _build_char_pool(self):
        chars = self.custom_chars

        if self.use_upper:
            chars += string.ascii_uppercase
        if self.use_lower:
            chars += string.ascii_lowercase
        if self.use_digits:
            chars += string.digits
        if self.use_symbols:
            chars += self.symbols

        if self.exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in self.ambiguous_chars)

        if not chars:
            raise ValueError("Character pool is empty. Enable at least one character type.")

        return chars

    def generate(self):
        passwords = []
        for _ in range(self.num_passwords):
            password = ''.join(secrets.choice(self.char_pool) for _ in range(self.length))
            passwords.append(password)
        return passwords

# Example usage
if __name__ == "__main__":
    generator = PasswordGenerator(
        length=20,
        use_upper=True,
        use_lower=True,
        use_digits=True,
        use_symbols=True,
        exclude_ambiguous=True,
        num_passwords=5
    )

    for i, pwd in enumerate(generator.generate(), 1):
        print(f"Password {i}: {pwd}")
