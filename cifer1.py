alphabet="abcdefghijklmnopqrstuvwxyzæøå"

def encode(letter,secret):
    pos=alphabet.find(letter)

    newpos=(pos+secret)

    if newpos>=29:
        newpos=newpos-29

    return alphabet[newpos]

def decode(letter,secret):
    pos=alphabet.find(letter)

    newpos=(pos-secret)

    if newpos<0:
        newpos=newpos+29

    return alphabet[newpos]

secret=17
message="hello world!"

output=""

for character in message:
    if character in alphabet:
        output=output+encode(character,secret)
    else:
        output=output+character


print(output)

#secret=9
message="æxkxånwn næ bnwwnwn mrwn"
output=""

for secret in range(0,29):
    for character in message:
        if character in alphabet:
            output=output+decode(character,secret)
        else:
            output=output+character
    print(output)
    output=""

            
