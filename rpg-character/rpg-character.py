full_dot = '●'
empty_dot = '○'
def create_character(character, strength, intelligence, charisma):
    if type(character) != str:
        return "The character name should be a string"
    if character == "":
        return "The character should have a name"
    if len(character) > 10:
        return "The character name is too long"
    if " " in character:
        return "The character name should not contain spaces"
    
    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"

    if len(character) < 1 and len(strength) < 1 and len(charisma) < 1:
        return "All stats should be no less than 1"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    str_line = full_dot * strength + empty_dot * (10 - strength)
    int_line = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = full_dot * charisma + empty_dot * (10 - charisma)
    result = f"{character}\nSTR {str_line}\nINT {int_line}\nCHA {cha_line}"
    return result

user_name = input("Enter character name: ")
user_str = int(input("Enter Strength (1-4): "))
user_int = int(input("Enter Intelligence (1-4): "))
user_cha = int(input("Enter Charisma (1-4): "))

result = create_character(user_name, user_str, user_int, user_cha)

print("\n--- Your Character Sheet ---")
print(result)