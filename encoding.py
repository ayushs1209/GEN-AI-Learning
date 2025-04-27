import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size = ",encoder.n_vocab)

text = "as the cat sat on the mat"
text2 = "as the mat sat on the cat"
encoded = encoder.encode(text)
encoded2 = encoder.encode(text2)
print((encoded))
print((encoded2))

decoder = [288, 290, 9059, 10139, 402, 290, 2450]

print(encoder.decode(decoder))