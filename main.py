
# Array to store the words for one and Two digits, only goes up to nineteen because from twenty onwards
# You can use the same numbers in this array and just need the tens, hundreds,thousands,millions and billions
oneAndTwoDigits = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ",
                   "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ",
                   "nineteen "];

# This arrays stores the words for the tens
tens = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "];


# This function converts a number to words
def numbersToWords(num):
    output = "";
    counter = 0;  # counter to check if the number is bigger than 99. this is to help with the "and" that is added to certain output

    if num == 0:
        output = "Zero";
    elif num < 20:
        output += oneAndTwoDigits[num];
    else:
        if num // 1000000000 > 0 or num // 10000000000 > 0:  # checks for billion and ten billion
            tempNum = num // 1000000000;  # temporary variable that stores the result of the division by 1 billion.
            if tempNum < 20:  # checks if the Temporary number is less than 20, if it is then u only have to get the word at that position in first array
                output += oneAndTwoDigits[tempNum];
            else:
                # if tempNum is greater than or equal to 20, we have to make use of the tens array as well. the appropriate calculations are done to get the correct positions.
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];
            output += "billion, ";  # adds the word billion to the output after the numbers have been converted to their correspondng word.
            num = num - (1000000000 * tempNum);  # we remove the billion or ten billion part of the number.
            counter = 1;  # if counter =1 then we can add an "and" when neccessary later on in the algorithm

        if num // 100000000 > 0:  # checks for hundred million
            tempNum = num // 100000000;  # temporary variable that stores the result of the division by 100 million.
            if tempNum < 20:
                output += oneAndTwoDigits[tempNum];
            else:
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];
            if num < 101000000:  # if the number is less than 101 million then we add "hundred million" otherwise we add "hundred and"
                output += "hundred million, ";
            else:
                output += "hundred and ";
            num = num - (100000000 * tempNum);  # we remove the hundred million part of the number.
            counter = 1;

        if num // 1000000 > 0 or num // 10000000:  # checks for million and 10 million
            tempNum = num // 1000000;  # temporary variable that stores the result of the division by 1 million.
            if tempNum < 20:
                output += oneAndTwoDigits[tempNum];
            else:
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];
            output += "million, ";
            num = num - (1000000 * tempNum);  # we remove the million or ten million part of the number.
            counter = 1;

        if num // 100000 > 0:  # checks for 100 thousands
            tempNum = num // 100000;  # temporary variable that stores the result of the division by 100 thousand.
            if tempNum < 20:
                output += oneAndTwoDigits[tempNum];
            else:
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];
            if num < (
                    tempNum * 100000) + 1000:  # if the number is less than x hundred and one thousand then we add "hundred thousand" otherwise we add "hundred and"
                output += "hundred thousand, ";
            else:
                output += "hundred and ";
            num = num - (100000 * tempNum);  # we remove the hundred thousand part of the number.
            counter = 1;

        if num // 1000 > 0 or num // 10000 > 0:  # checks for 1 thousands or ten thousands
            tempNum = num // 1000;  # temporary variable that stores the result of the division by 1 thousand.
            if tempNum < 20:
                output += oneAndTwoDigits[tempNum];
            else:
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];
            output += "thousand, ";
            num = num - (1000 * tempNum);  # we remove the thousands part of the number.
            counter = 1;

        if num // 100 > 0:  # checks for hundreds
            tempNum = num // 100;  # temporary variable that stores the result of the division by 100.
            if tempNum < 20:
                output += oneAndTwoDigits[tempNum];
            else:
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];
            output += "hundred ";
            counter = 1;

        if ((num > 0 and num % 100) and counter == 1):  # for adding the word "and" after or before a number
            output += "and ";

        if num % 100 > 0:
            tempNum = num % 100;
            if tempNum < 20:
                output += oneAndTwoDigits[tempNum];
            else:
                output += tens[tempNum // 10] + oneAndTwoDigits[tempNum % 10];

    return output;


if __name__ == "__main__":
    with open('input.txt') as file:  # opening the text file
        for line in file:  # checking for each line in the file
            break_flag = False  # to check if a loop has been broken out of. initial value is false
            specialChar = ["#", "$", "@", "!", "&",","]  # this array stores all the special characters that is not accepted with a number
            integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8","9"]  # this array stores all the single digit integers and is used to check if a number is valid

            for i in line.split():  # now we check each word or number on a line

                for integer in integers:  # traverses through the numbers array
                    for char in specialChar:  # traverses through the special Characters array
                        if (i.__contains__(char) and i.__contains__(integer)):  # checks if the word/number chosen has a special character and a number together
                            print("number invalid");  # if it meets the above condition, the number is invalid
                            break_flag = True
                            break  # we break out of the loop because once the number is invalid we dont have to check other integers part of this number
                    if break_flag:  # checks if the special char loop has been broken out of, if true it breaks out of the numbers loop
                        break

                if i.isdigit():  # checks if a number is found on the line
                    print(int(i), ":", (numbersToWords(int(i))));# prints the number and converts the number to words and prints out the words