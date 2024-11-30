def decode_message(shift, message):
    keyboard = ["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"]
    
    original_message = []
    shift_amount = 1 if shift == 'L' else -1
    for char in message:
        for row in keyboard:
            if char in row:
                idx = row.index(char)
                original_message.append(row[idx + shift_amount])
                break
    return ''.join(original_message)


shift = input().strip()
message = input().strip()

print(decode_message(shift, message))
