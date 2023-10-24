from production import IF, AND, THEN, OR, DELETE, NOT, FAIL


# TODO: implement your own rules according to the defined goal tree
# HINT: see an example in the file rules_example_zookeeper.py
RULES = (

    IF(OR('(?x) has blue skin',
          '(?x) has 4 eyes'),  # R1
       THEN('(?x) is celestial')),

    IF(AND('(?x) is celestial'),  # R1
       THEN('(?x) is a Mooney')),

    IF(AND('(?x) is celestial',
           '(?x) has high body temperature'),  # R1
       THEN('(?x) is a Sunny')),


    IF(OR('(?x) has low body temperature',
          '(?x) is sad'),  # Z3
       THEN('(?x) is part of the Kuiper Belt')),

    IF(AND('(?x) is part of the Kuiper Belt',  # Z4
           '(?x) is very short'),
        THEN('(?x) is a Plutonian')),

    IF(AND('(?x) has 2 eyes'),
       THEN('(?x) is an Earthy')),

    IF(AND('(?x) is part of the Kuiper Belt',  # Z6
           '(?x) does not speak Solarian'),
       THEN('(?x) is a Make Maker')),

)

DATA = (
    'Mark has low body temperature',
    'Mark is sad',
    'Mark does not speak Solarian',
    )