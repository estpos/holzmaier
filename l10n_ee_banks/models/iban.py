from functools import reduce
# -*- coding: utf-8 -*-


class Country:
    """Class for country specific iban data."""

    def __init__(self, name, code, bank_form, acc_form):
        """Constructor for Country objects.

        Arguments:
            name      - Name of the country
            code      - Country Code from ISO 3166
            bank_form - Format of bank/branch code part (e.g. "0 4a 0 ")
            acc_form  - Format of account number part (e.g. "0  11  2n")
        """
        self.name = name
        self.code = code
        self.bank = self._decode_format(bank_form)
        self.acc = self._decode_format(acc_form)

    def bank_lng(self):
        return reduce(lambda sum, part: sum + part[0], self.bank, 0)

    def acc_lng(self):
        return reduce(lambda sum, part: sum + part[0], self.acc, 0)

    def total_lng(self):
        return 4 + self.bank_lng() + self.acc_lng()

    def _decode_format(self, form):
        form_list = []
        for part in form.split(" "):
            if part:
                typ = part[-1]
                if typ in ("a", "n"):
                    part = part[:-1]
                else:
                    typ = "c"
                lng = int(part)
                form_list.append((lng, typ))
        return tuple(form_list)


# BBAN data from ISO 13616, Country codes from ISO 3166 (www.iso.org).
iban_data = (
    Country("Andorra", "AD", "0  4n 4n", "0  12   0 "),
    Country("Albania", "AL", "0  8n 0 ", "0  16   0 "),
    Country("Austria", "AT", "0  5n 0 ", "0  11n  0 "),
    Country("Bosnia and Herzegovina", "BA", "0  3n 3n", "0   8n  2n"),
    Country("Belgium", "BE", "0  3n 0 ", "0   7n  2n"),
    Country("Bulgaria", "BG", "0  4a 4n", "2n  8   0 "),
    Country("Switzerland", "CH", "0  5n 0 ", "0  12   0 "),
    Country("Cyprus", "CY", "0  3n 5n", "0  16   0 "),
    Country("Czech Republic", "CZ", "0  4n 0 ", "0  16n  0 "),
    Country("Germany", "DE", "0  8n 0 ", "0  10n  0 "),
    Country("Denmark", "DK", "0  4n 0 ", "0   9n  1n"),
    Country("Estonia", "EE", "0  2n 0 ", "2n 11n  1n"),
    Country("Spain", "ES", "0  4n 4n", "2n 10n  0 "),
    Country("Finland", "FI", "0  6n 0 ", "0   7n  1n"),
    Country("Faroe Islands", "FO", "0  4n 0 ", "0   9n  1n"),
    Country("France", "FR", "0  5n 5n", "0  11   2n"),
    Country("United Kingdom", "GB", "0  4a 6n", "0   8n  0 "),
    Country("Georgia", "GE", "0  2a 0 ", "0  16n  0 "),
    Country("Gibraltar", "GI", "0  4a 0 ", "0  15   0 "),
    Country("Greenland", "GL", "0  4n 0 ", "0   9n  1n"),
    Country("Greece", "GR", "0  3n 4n", "0  16   0 "),
    Country("Croatia", "HR", "0  7n 0 ", "0  10n  0 "),
    Country("Hungary", "HU", "0  3n 4n", "1n 15n  1n"),
    Country("Ireland", "IE", "0  4a 6n", "0   8n  0 "),
    Country("Israel", "IL", "0  3n 3n", "0  13n  0 "),
    Country("Iceland", "IS", "0  4n 0 ", "2n 16n  0 "),
    Country("Italy", "IT", "1a 5n 5n", "0  12   0 "),
    Country("Kuwait", "KW", "0  4a 0 ", "0  22   0 "),
    Country("Kazakhstan", "KZ", "0  3n 0 ", "0  13   0 "),
    Country("Lebanon", "LB", "0  4n 0 ", "0  20   0 "),
    Country("Liechtenstein", "LI", "0  5n 0 ", "0  12   0 "),
    Country("Lithuania", "LT", "0  5n 0 ", "0  11n  0 "),
    Country("Luxembourg", "LU", "0  3n 0 ", "0  13   0 "),
    Country("Latvia", "LV", "0  4a 0 ", "0  13   0 "),
    Country("Monaco", "MC", "0  5n 5n", "0  11   2n"),
    Country("Montenegro", "ME", "0  3n 0 ", "0  13n  2n"),
    Country("Macedonia, Former Yugoslav Republic of", 
        "MK", "0  3n 0 ", "0  10   2n"),
    Country("Mauritania", "MR", "0  5n 5n", "0  11n  2n"),
    Country("Malta", "MT", "0  4a 5n", "0  18   0 "),
    Country("Mauritius", "MU", "0  4a 4n", "0  15n  3a"),
    Country("Netherlands", "NL", "0  4a 0 ", "0  10n  0 "),
    Country("Norway", "NO", "0  4n 0 ", "0   6n  1n"),
    Country("Poland", "PL", "0  8n 0 ", "0  16n  0 "),
    Country("Portugal", "PT", "0  4n 4n", "0  11n  2n"),
    Country("Romania", "RO", "0  4a 0 ", "0  16   0 "),
    Country("Serbia", "RS", "0  3n 0 ", "0  13n  2n"),
    Country("Saudi Arabia", "SA", "0  2n 0 ", "0  18   0 "),
    Country("Sweden", "SE", "0  3n 0 ", "0  16n  1n"),
    Country("Slovenia", "SI", "0  5n 0 ", "0   8n  2n"),
    Country("Slovak Republic", "SK", "0  4n 0 ", "0  16n  0 "),
    Country("San Marino", "SM", "1a 5n 5n", "0  12   0 "),
    Country("Tunisia", "TN", "0  2n 3n", "0  13n  2n"),
    Country("Turkey", "TR", "0  5n 0 ", "1  16   0 ")
)


def country_data(code):
    """Search the country code in the iban_data list."""
    for country in iban_data:
        if country.code == code:
            return country
    return None


def mod97(digit_string):
    """Modulo 97 for huge numbers given as digit strings.

    This function is a prototype for a JavaScript implementation.
    In Python this can be done much easier: long(digit_string) % 97.
    """
    m = 0
    for d in digit_string:
        m = (m * 10 + int(d)) % 97
    return m


def fill0(s, l):
    """Fill the string with leading zeros until length is reached."""
    import string
    return string.zfill(s, l)


def strcmp(s1, s2):
    """Compare two strings respecting german umlauts."""
    chars = "AaÄäBbCcDdEeFfGgHhIiJjKkLlMmNnOoÖöPpQqRrSsßTtUuÜüVvWwXxYyZz"
    lng = min(len(s1), len(s2))
    for i in range(lng):
        d = chars.find(s1[i]) - chars.find(s2[i])
        if d != 0:
            return d
    return len(s1) - len(s2)


def country_index_table():
    """Create an index table of the iban_data list sorted by country names."""
    tab = range(len(iban_data))
    for i in range(len(tab) - 1, 0, -1):
        for j in range(i):
            if strcmp(iban_data[tab[j]].name, iban_data[tab[j + 1]].name) > 0:
                t = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1] = t
    return tab


def checksum_iban(iban):
    """Calculate 2-digit checksum of an IBAN."""
    code = iban[:2]
    checksum = iban[2:4]
    bban = iban[4:]

    # Assemble digit string
    digits = ""
    for ch in bban.upper():
        if ch.isdigit():
            digits += ch
        else:
            digits += str(ord(ch) - ord("A") + 10)
    for ch in code:
        digits += str(ord(ch) - ord("A") + 10)
    digits += checksum

    # Calculate checksum
    checksum = 98 - mod97(digits)
    return fill0(str(checksum), 2)


def fill_account(country, account):
    """Fill the account number part of IBAN with leading zeros."""
    return fill0(account, country.acc_lng())


def invalid_part(form_list, iban_part):
    """Check if syntax of the part of IBAN is invalid."""
    for lng, typ in form_list:
        if lng > len(iban_part):
            lng = len(iban_part)
        for ch in iban_part[:lng]:
            a = ("A" <= ch <= "Z")
            n = ch.isdigit()
            c = n or a or ("a" <= ch <= "z")
            if (not c and typ == "c") or \
               (not a and typ == "a") or \
               (not n and typ == "n"):
                return 1
        iban_part = iban_part[lng:]
    return 0


def invalid_bank(country, bank):
    """Check if syntax of the bank/branch code part of IBAN is invalid."""
    return len(bank) != country.bank_lng() or \
        invalid_part(country.bank, bank)


def invalid_account(country, account):
    """Check if syntax of the account number part of IBAN is invalid."""
    return len(account) > country.acc_lng() or \
        invalid_part(country.acc, fill_account(country, account))


def calc_iban(country, bank, account, alternative=0):
    """Calculate the checksum and assemble the IBAN."""
    account = fill_account(country, account)
    checksum = checksum_iban(country.code + "00" + bank + account)
    if alternative:
        checksum = fill0(str(mod97(checksum)), 2)
    return country.code + checksum + bank + account


class IBANError(Exception):

    def __init__(self, errmsg):
        Exception.__init__(self, errmsg)


def create_iban(code, bank, account, alternative=0):
    """Check the input, calculate the checksum and assemble the IBAN.

    Return the calculated IBAN.
    Return the alternative IBAN if alternative is true.
    Raise an IBANError exception if the input is not correct.
    """
    err = None
    country = country_data(code)
    if not country:
        err = "Unknown Country Code: %s" % code
    elif len(bank) != country.bank_lng():
        err = "Bank/Branch Code length %s is not correct for %s (%s)" % \
              (len(bank), country.name, country.bank_lng())
    elif invalid_bank(country, bank):
        err = "Bank/Branch Code %s is not correct for %s" % \
              (bank, country.name)
    elif len(account) > country.acc_lng():
        err = "Account Number length %s is not correct for %s (%s)" % \
              (len(account), country.name, country.acc_lng())
    elif invalid_account(country, account):
        err = "Account Number %s is not correct for %s" % \
              (account, country.name)
    if err:
        raise IBANError(err)
    return calc_iban(country, bank, account, alternative)

