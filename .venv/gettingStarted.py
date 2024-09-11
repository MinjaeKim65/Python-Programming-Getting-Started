
def welcome_assignment_answers(question):

    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same?":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key?":
        answer = "No"
    elif question == "Is it possible to decode a message without a key?":
        answer = "No"
    elif question == "Is a hashed message supposed to be un-hashed?":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code":
        answer = "dont know yet"
    elif question == "Is MD5 a secured hashing algorithm?":
        answer = "Yes"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to?":
        answer = "don't know yet"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to?":
        answer = "don't know yet"
    else:
        answer = "Not a valid question!"

    return(answer)

print(welcome_assignment_answers(input()))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":