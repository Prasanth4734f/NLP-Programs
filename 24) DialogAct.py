utterances = [
    "Hello!",
    "Can you help me?",
    "Thank you!",
    "Goodbye."
]

acts = {
    'greeting': ['hello', 'hi'],
    'request': ['help', 'can you'],
    'thanks': ['thank'],
    'goodbye': ['bye', 'goodbye']
}

for u in utterances:
    u_low = u.lower()
    detected = 'other'
    for act, keywords in acts.items():
        if any(k in u_low for k in keywords):
            detected = act
            break
    print(f"{u} --> {detected}")

    -----------------------------------OUTPUT-----------------------------------

    Hello! --> greeting
Can you help me? --> request
Thank you! --> thanks
Goodbye. --> goodbye

