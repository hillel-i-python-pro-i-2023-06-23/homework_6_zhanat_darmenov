import pandas as pd


def read_web_csv_file():
    url = (
        "https://docs.google.com/spreadsheets/d/e/2PACX"
        "-1vQjuDXLl1N63shaddToASHohoFeo4D1Mt8PClAt4n1YImnLWNjUkCJgSkby2FcwgAHhTCFFoXMFz-eN/pub?output=csv"
    )

    columns = ["Height(Inches)", "Weight(Pounds)"]

    try:
        df = pd.read_csv(url, usecols=columns)

        # Calculate the average for each column
        average_height_inches = df["Height(Inches)"].mean()
        average_weight_pounds = df["Weight(Pounds)"].mean()

        # Convert to centimeters and kilograms
        cm_per_inch = 2.54
        kg_per_pound = 0.45359237
        average_height_cm = average_height_inches * cm_per_inch
        average_weight_kg = average_weight_pounds * kg_per_pound

        # Round the results to two digits after the decimal point
        average_height_cm = round(average_height_cm, 2)
        average_weight_kg = round(average_weight_kg, 2)

        print("\nData:")

        print("\nAverage Height (centimeters):", average_height_cm)
        print("Average Weight (kilograms):", average_weight_kg)

    except Exception as e:
        print("Error:", e)
