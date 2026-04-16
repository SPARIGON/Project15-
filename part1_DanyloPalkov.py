#Author: Danylo Palkov

def load_data():
    names, exam1, exam2 = [], [], []

    try:
        file = open("English.txt", "r")
        for line in file:
            # strip() removes the \n, split(",") separates by the comma
            data = line.strip().split(",")

            names.append(data[0])
            exam1.append(int(data[1]))
            exam2.append(int(data[2]))

        file.close()
    except FileNotFoundError:
        print("File not found!")
    return names, exam1, exam2

def save_data(names, e1, e2):
    file = open("English.txt", "w")
    for i in range(len(names)):
        file.write(f"{names[i]},{e1[i]},{e2[i]}\n")
    file.close()
    print("Data saved successfully.")


def show_results(names, exam1, exam2):
    print("\nExam 1 Results:")
    for i in range(len(names)):
        if exam1[i] != -1: # Only show if they sat the exam
            print(f"{names[i]:<15} {exam1[i]}")
    print("\nExam 2 Results:")
    for i in range(len(names)):
        if exam2[i] != -1: # Only show if they sat the exam
            print(f"{names[i]:<15} {exam2[i]}")

def missing_students(names, exam1, exam2):
    # Exam 1
    m1 = 0
    print("\nMissing Exam 1:")
    for i in range(len(names)):
        if exam1[i] == -1:
            print(names[i])
            m1 += 1
    print(f"Total missing: {m1}")

    # Exam 2
    m2 = 0
    print("\nMissing Exam 2:")
    for i in range(len(names)):
        if exam2[i] == -1:
            print(names[i])
            m2 += 1
    print(f"Total missing: {m2}")


def main():

    names, exam1, exam2 = load_data()
    show_results(names, exam1, exam2)
    missing_students(names, exam1, exam2)


if __name__ == "__main__":
    main()