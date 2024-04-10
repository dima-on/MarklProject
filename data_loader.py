import pandas as pd



def main():
    df = pd.read_csv("RAW_recipes.csv")


    #########################
    # id #     # desciption #
    #########################
    with open("recepts.txt", "w") as file:
        for el in df['description']:
            file.write(el)


if __name__ == "__main__":
    main()
