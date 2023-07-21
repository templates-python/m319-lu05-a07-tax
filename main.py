def main():
    tax = 0
    TAX_EXEMPTION_LIMIT = 325000

    inheritance = int(input('Inheritance:\n'))
    taxable_amount = inheritance - TAX_EXEMPTION_LIMIT
    years = int(input('Years since death:\n'))

    if taxable_amount > 0:
        if years < 3:
            tax = taxable_amount * 0.40
        elif years < 4:
            tax = taxable_amount * 0.32
        elif years < 5:
            tax = taxable_amount * 0.24
        elif years < 6:
            tax = taxable_amount * 0.16
        elif years < 7:
            tax = taxable_amount * 0.08

    print(f'Tax: {tax}')


if __name__ == '__main__':
    main()
