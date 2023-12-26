print("<<<<<<<<<Welcome>>>>>>>>>>\n")  # This line welcome's the patient


def patientRegistration():
    registrations = []
    for i in range(1):  # In this line we can change how many patients we want to register
        reg = []

        vc = input(
            "\nChoose between the two available centres (VC1 and VC2): ")  # Patients choose their preferred VC here
        vc = vc.upper()
        while ((vc != 'VC1') and (vc != 'VC2')):  # This function asks for VC's
            print('Invalid Choice')
            vc = input("\nChoose between the two available centres (VC1 and VC2): ")
            vc = vc.upper()
        reg.append(vc)
        file_handler2 = open('vaccination.txt', 'a')
        file_handler2.write(str(vc))
        file_handler2.write('\t')
        file_handler2.close()
        while True:  # This functions asks for patient age and checks if they are eligible for the vaccines
            try:
                age = int(input("Enter your age and vaccines will be displayed accordingly: "))
                break
            except:
                print("Please enter your age")
        if age >= 12:
            print("You are eligible for the vaccines shown below, please enter your credentials and proceed")
        if age >= 12 and age <= 45:
            print("-CZ")
        if age >= 12:
            print("-DM\n-AF")
        if age >= 18:
            print("-BV\n-EC")
        elif age <= 11:
            print("You are not eligible for any of the vaccines.")
            exit()
        reg.append(age)

        patientName = input('Enter Patient Name: ')  # This function asks for patient's name
        reg.append(patientName)
        file_handler2 = open('vaccination.txt', 'a')
        file_handler2.write(str(patientName))
        file_handler2.write('\t')
        file_handler2.close()

        phoneNum = input('Please enter your Patient phone number: ')  # This function asks for patient's phone number
        reg.append(phoneNum)
        file_handler2 = open('vacinationtxt', 'a')
        file_handler2.write(str(phoneNum))
        file_handler2.write('\t')
        file_handler2.close()



        uniqueId = input('Enter Patient UID: ')  # This function gives patients a unique ID
        reg.append(uniqueId)
        file_handler2 = open('vaccination.txt', 'a')
        file_handler2.write(str(uniqueId))
        file_handler2.write('\t')
        file_handler2.close()
        # The functions below deals with patient's vaccine/vaccine status, and their vaccine first and second dose
        vaccine = str(input("Please select your vaccine: "))
        dose_num = str(input("Please enter your dose either (D1 as in 1st dose or D2 as in 2nd dose): "))
        vaccine = vaccine.upper()
        dose_num = dose_num.upper()
        if vaccine == 'AF' and dose_num == 'D1':
            print(
                "Your first dose is now completed and the second dose will be administered after 2 weeks (or 14 days)")
        elif vaccine == 'AF' and dose_num == 'D2':
            print("You have successfully completed both doses.")
        elif vaccine == 'BV' and dose_num == 'D1':
            print(
                "Your first dose is now completed and the second dose will be administered after 3 weeks (or 21 days)")
        elif vaccine == 'BV' and dose_num == 'D2':
            print("You have successfully completed both doses.")
        elif vaccine == 'CZ' and dose_num == 'D1':
            print(
                "Your first dose is now completed and the second dose will be administered after 3 weeks (or 21 days)")
        elif vaccine == 'CZ' and dose_num == 'D2':
            print("You have successfully completed both doses.")
        elif vaccine == 'DM' and dose_num == 'D1':
            print(
                "Your first dose is now completed and the second dose will be administered after 4 weeks (or 28 days)")
        elif vaccine == 'DM' and dose_num == 'D2':
            print("You have successfully completed both doses.")
        elif vaccine == 'EC' and dose_num == 'D1':
            print("You have successfully completed dose.")
        while ((vaccine != 'AF') and (vaccine != 'BV') and (vaccine != 'CZ') and (vaccine != 'DM') and (
                vaccine != 'EC')):
            print("Please enter a valid choice")
            vaccine = str(input("Please select your vaccine: "))
            vaccine = vaccine.upper()
        while ((dose_num != 'D1') and (dose_num != 'D2')):
            print("Please enter a valid choice")
            dose_num = str(input("Please enter your dose either (D1 as in 1st dose or D2 as in 2nd dose)"))
            dose_num = dose_num.upper()
        reg.append(vaccine)
        file_handler2 = open('vaccination.txt', 'a')
        file_handler2.write(str(vaccine))
        file_handler2.write('\t')
        file_handler2.write('\n')
        file_handler2.close()# This line saves patients vaccine status
        reg.append(dose_num)  # This line saves patients dose status

        registrations.append(reg)  # This line appends all of the functions above
    return registrations  # This line returns registration


def savePatientRegistrations():  # This function saves patient registration in text file
    fileHandler = open('patients.txt', 'a')
    registration = patientRegistration()

    for reg in registration:
        for pr in reg:
            fileHandler.write(str(pr))
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()
def printPatientRegistrations():  # This function prints patient registration in text file
    fileHandler = open('patients.txt', 'r')

    for line in fileHandler:
        line = line.rstrip()
        print(line)
    file_handler2 = open('vaccination.txt', 'r')
    for line in file_handler2:
        fileHandler.read()
    fileHandler.close()
    file_handler2.close()

def searchPatientRegistrations():  # With this function we can search for patients details
    try:
        fileHandler = open('patients.txt', 'r')
    except:
        print('File cannot be opened:')
        exit()
    search_key = input('Type what you want to search: ')

    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower():
            continue
        print(line)

def patientsStatistics():
    vaccine = open('patients.txt', 'r')
    total_count_VC1 = 0
    total_count_VC2 = 0
    for content in vaccine:
        if (content[2] == '1') and (content[9] == '1' or content[2] == '1'):
            total_count_VC1 = total_count_VC1 + 1
        elif (content[2] == '2') and (content[9] == '2' or content[2] == '2'):
            total_count_VC2 = total_count_VC2 + 1

        print(total_count_VC1, 'Pateients enrolled in VC1')
        print(total_count_VC2, 'Pateients enrolled in VC2')
        total_centres = [total_count_VC1 + total_count_VC2]
        total_patients = sum(total_centres)
        print('\nUpdated report of total patirnts\n', total_patients, 'total patients registerd in VC1 and VC2\n')
        
def menu():  # This is the menu function that will be shown at the start of the program
    print('Select the operation that you want to perform:')
    print('1.save patient registration')
    print('2.print patient registration')
    print('3.search patient registration')
    print('4.statistics')
    print('5.exit')

    choice = int(input('Enter selection: '))
    if (choice==1):
        savePatientRegistrations()
    elif (choice==2):
        printPatientRegistrations()
    elif (choice==3):
        searchPatientRegistrations()
    elif choice==4:
        patientsStatistics()
    elif choice==5:
        print('Have a nice day')
    else:
        print('Invalid input')

    print()
    print()

menu()
