text = "Mary met John. She told him a secret."
sentences = text.split('. ')
names = set()
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word.istitle():
            names.add(word)
    if 'She' in words:
        print(f"'She' probably refers to: {', '.join([n for n in names if n in ['Mary', 'Susan', 'Rita']])}")
    if 'him' in words:
        print(f"'him' probably refers to: {', '.join([n for n in names if n in ['John', 'Tom', 'Mike']])}")


---------------------------------------------OUTPUT-----------------------------------

'She' probably refers to: Mary
'him' probably refers to: John
