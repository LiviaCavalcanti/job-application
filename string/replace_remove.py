def replace_remove(word):
    write_idx, word_count=0, 0
    for i in range(len(word)):
        if word[i] != 'b':
            word[write_idx]= word[i]
            write_idx += 1
        if word[i] == 'a':
            word_count += 1
    
    current_idx = write_idx -1
    write_idx += word_count -1
    final_size = write_idx + 1
    # current_idx = word_count
    print(f"Print word before adding the d: {word}")
    while current_idx >= 0:
        if word[current_idx] == 'a':
            word[write_idx -1 : write_idx +1] = 'dd'
            print(f"Print word after addind: {word} (current index: {current_idx}, write index: {write_idx})")
        else:
            word[write_idx] = word[current_idx]
            write_idx -=1
        current_idx -=1

    return final_size

print(replace_remove(['a', 'a', 'a']))

print(replace_remove(['a', 'b','a', 'c','a']))
