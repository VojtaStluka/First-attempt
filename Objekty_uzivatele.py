from __future__ import annotations


class AccountApi:
    def __init__(self, jmeno: str, email: str, heslo: str) -> None:
        self.jmeno = jmeno
        self.email = email
        self.heslo = heslo
        self.seznam_uzivatelu = []
        
    def register_user(self) -> None:
        if self not in self.seznam_uzivatelu:
            self.seznam_uzivatelu.append(self)
        print(f"Uživatel {self.jmeno} byl úspěšně zaregistrován s e-mailem {self.email}.")

    def remove_user(self) -> None:
        if self in self.seznam_uzivatelu:
            self.seznam_uzivatelu.remove(self)
            print(f"Uživatel {self.jmeno} byl úspěšně odstraněn.")
            return
        print(f"Uživatel {self.jmeno} není registrován.")

    def verify_password(self, zkousene_heslo: str) -> bool:
        is_valid = self.heslo == zkousene_heslo
        print("Heslo je správné." if is_valid else "Heslo je nesprávné.")
        return is_valid

    def update_email(self, new_email: str) -> None:
        self.email = new_email
        print(f"E-mail pro uživatele {self.jmeno} byl aktualizován na {self.email}.")

    def list_users_emails(self) -> None:
        print("Seznam e-mailů registrovaných uživatelů:")
        for email in (user.email for user in self.seznam_uzivatelu):
            print(email)

    def find_user_by_email(self, hledany_email: str) -> None:
        user = next((u for u in self.seznam_uzivatelu if u.email == hledany_email), None)
        if user:
            print(f"Uživatel s e-mailem {hledany_email} nalezen: {user.jmeno}")
            return
        print(f"Uživatel s e-mailem {hledany_email} nebyl nalezen.")
