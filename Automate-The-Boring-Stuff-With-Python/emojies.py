messages = input(">")
words = messages.split(" ")
emojis = {
    ":)":"😀",
    ":(":"😔"
}
output = ""
for word in words:
    output += emojis.get(word,word) + " "