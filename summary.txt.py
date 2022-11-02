def mileagecharge(end, start, classification):
    calc_mileage = end - start
    if classification == 'b':
        base_charge = 40
        mileage_charge = float((base_charge * 0.25 * calc_mileage))
        return mileage_charge

    elif classification == 'd':
        base_charge1 = 60
        if calc_mileage <= 100:
            mileage_charge1 = base_charge1
            return mileage_charge1
        elif calc_mileage > 100:
            mileage_charge1 = float(base_charge1 + 0.25 * (calc_mileage - 100))
            return mileage_charge1

    elif classification == 'w':
        base_charge2 = 190
        if calc_mileage <= 900:
            mileage_charge2 = base_charge2
            return mileage_charge2
        elif (calc_mileage > 900) and (calc_mileage <= 1500):
            mileage_charge2 = base_charge2 + 200
            return mileage_charge2
        elif calc_mileage > 1500:
            mileage_charge2 = base_charge2 + 200 + 0.25 * (calc_mileage - 1500)
            return mileage_charge2


def information(users=[]):
    classification_code = str(input("What is the rental code? Please choose b, d, or w: "))
    customer_name = input("What is the customer's name? ")
    num_of_days_v_was_rented = int(input("how many days? "))
    od_read_start = int(input("What is the mileage at the beginning? "))
    od_read_end = int(input("What is the mileage at the end? "))
    users.append([classification_code.upper(), customer_name, num_of_days_v_was_rented, od_read_start, od_read_end,
                  mileagecharge(od_read_end, od_read_start, classification_code)])
    question = input("would you like to add another customer? Enter 'Y' for yes or 'Q' for quit: ")
    while True:
        if question.lower() == "y":
            information(users)
            break
        elif question.lower() == "q":
            for a, b, c, d, e, f in users:
                print("*********")
                print(f"Classification code: {a}")
                print(f"Name: {b}")
                print(f"Number of days: {c}")
                print(f"Mileage at the start: {d}")
                print(f"Mileage at the end: {e}")
                print(f"Number of miles driven: {e - d}")
                print(f"Mileage charge: {f}")
            break
        else:
            question = input("would you like to add another customer? Enter 'Y' for yes or 'Q' for quit: ")



information()