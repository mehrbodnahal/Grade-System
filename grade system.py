print("Grade ranges from 0 to 20")
print("20 = A ")
print("0 = F")
grade = float(input("enter your grade: "))


if (grade > 18) and (grade <= 20):
    print(
        grade,
        """
Grade: A""",
    )

elif (grade > 16) and (grade <= 18):
    print(
        grade,
        """
Grade: B""",
    )


elif (grade > 14) and (grade <= 16):
    print(
        grade,
        """
Grade: C""",
    )


elif (grade > 12) and (grade <= 14):
    print(
        grade,
        """
Grade: D""",
    )

elif (grade > 10) and (grade <= 12):
    print(
        grade,
        """
Grade: E""",
    )

elif (grade > 0) and (grade <= 10):
    print(
        grade,
        """
Grade: F""",
    )

else:
    print("error")
