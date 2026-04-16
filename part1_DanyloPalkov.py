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


def main():

    names, exam1, exam2 = load_data()
    

if __name__ == "__main__":
    main()