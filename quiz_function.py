def std_weight(height, gender):  # height is meter (integer), sex = "male" / "female"
    if gender == "male":
        return height * height * 22
    else:
        return height * height * 21


height = 175  # cm
gender = "male"
weight = round(std_weight(height / 100, gender), 2)
print("a standard weight of a {1} who has height of {0} is {2}". format(
    height, gender, weight))
