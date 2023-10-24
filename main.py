from rules import RULES, DATA
from production import forward_chain, backward_chain
from questions import  *
# from rules import my_rules
def starts_with_vowel(word):
    # Convert the word to lowercase to handle both cases
    lower_word = word.lower()

    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Check if the first letter is a vowel
    return lower_word[0] in vowels


if __name__=='__main__':

    create_questions()
    for rule, pair in dictionary.items():
        print(f'{rule} : {pair}')
    print("         ")

    result_data = forward_chain(RULES, DATA)
    # Print the result of forward chaining
    print("Result of forward chaining:")
    for item in result_data:
        print(item)
    rule_set = []
    for i in RULES:
        for a in i.antecedent():
            rule_set.append(a)

    tourist_name = input("What is the name of the tourist you are trying to find more information about?\n")
    tourist_species = input("What species is the tourist?\n1.Earthy\n2.Mooney\n3.Sunny\n4.Make Maker\n5.Plutonian\n")
    print("         ")


    if starts_with_vowel(tourist_species):
        attribute = "an"
    else:
        attribute = "a"

    hypothesis = f"{tourist_name} is {attribute} {tourist_species}"
    print(f'Result of backward chaining: ')
    backward_chain_data = backward_chain(RULES, hypothesis)

    for data in backward_chain_data:
        print(data)


