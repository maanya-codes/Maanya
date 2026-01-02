while True:
    word = input("Enter a word: ")
    chr = input("Enter character to check how many times it is repeated: ")

    count = 0

    for i in word:
        if i == chr :
            count += 1
    
    print(chr, "was used", count, "times")