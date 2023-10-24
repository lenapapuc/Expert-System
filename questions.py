from production import *
from rules import RULES

#dictionary that unites statements with questions
dictionary = {}

#Method to check if there are any statements that could become multiple questions in the
#list, it returns a set of values that are not the subject or the verb of a sentence, and have more than 2 words
#i called them complements, they will help determine whether some sentences are similar in meaning
def check_for_multiple_choice():

    set_of_complements = []
    dict = {}
    for r in RULES:
        for statement in r.antecedent():
            words = statement.split()
            complement = ' '.join(words[2:])
            dict[complement] = statement

            if len(complement.split()) >= 2:
                set_of_complements.append(complement)

    return set_of_complements,dict
#taking the resulting complements and the dictionary, this function generates sentences that are multiple choice
#it takes the similar complements and unites them with 'or'. It then sends them to the question generator
def generate_multiple_choice():

    comp = check_for_multiple_choice()[0]

    similar_elements = find_similar_elements(comp)
    dict = check_for_multiple_choice()[1]

    intermediary_list = []
    for pair in similar_elements:
        sentence = dict[pair[0]]
        words = sentence.split()
        new_sentence = words[0] + ' ' + words[1] + ' '+' or '.join(pair) + ' or other'
        intermediary_list.append(new_sentence)
        for i in pair:
            dictionary[dict[i]] = new_sentence
    statement_to_question(intermediary_list)
    print(dictionary)

    return intermediary_list

#Method that takes complements and checks if they are similar in any way, this will help sort the sentences that can become
#multiple choice
def find_similar_elements(elements):
    similar_pairs = []


    # Iterate through the elements
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            # Split the elements into words and compare
            words1 = set(elements[i].split())
            words2 = set(elements[j].split())
            differing = words1.symmetric_difference(words2)


            # Check if the elements differ by only one word
            if len(differing) == 2:
                similar_pairs.append((elements[i], elements[j]))
            # Find and print similar pairs
    return similar_pairs




#The question generator takes sentences and generates questions,
#it also adds them to the dictionary of questions, each statement has a corresponding question
def statement_to_question(statement_list):

    questions = set()
    for statement in statement_list:
        words = statement.split()
        subject = words[0].capitalize()
        verb = words[1]
        complement = ' '.join(words[2:])
        if verb.lower() in ['is', 'am', 'are', 'was', 'were']:

            question = f" {verb.capitalize()} {subject} {complement}?"
        else:
            if verb == 'has':
                verb = 'have'
                question = f"Does {subject} {verb} {complement}?"
            elif verb == 'does':
                question = f"Does {subject} {complement}?"
            else:
                question = f"Does {subject} {verb[:-1]} {complement}?"

        if statement in dictionary:
            dictionary.update({statement: question})
        for key in dictionary:
            if dictionary[key] == statement:

                dictionary.update({key : question})

    
    return questions

def create_questions():
    generate_multiple_choice()
    list_of_statements = []
    for rule in RULES:
        for a in rule.antecedent():
            if a not in dictionary:
                dictionary[a] = 'None'
                list_of_statements.append(a)
    statement_to_question(list_of_statements)
    return dictionary








