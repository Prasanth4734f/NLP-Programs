import spacy

nlp = spacy.load("en_core_web_sm")
sentence = "The smart doctor prescribed new medicine for the sick child."

doc = nlp(sentence)
print("Noun Phrases and their meanings (descriptions):")
for np in doc.noun_chunks:
    # Get adjectives or modifiers for each noun phrase
    token = np.root
    modifiers = [w.text for w in token.lefts if w.pos_ == 'ADJ']
    description = " ".join(modifiers)
    if description:
        print(f"- {np.text}: describes as '{description}'")
    else:
        print(f"- {np.text}: no explicit description")

----------------------------------------OUTPUT----------------------------------------

Noun Phrases and their meanings (descriptions):
- The smart doctor: describes as 'smart'
- new medicine: describes as 'new'
- the sick child: describes as 'sick'