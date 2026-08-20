Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

1. You should have a function named create_character.
2. When create_character is called with a first argument that is not a string it should return The character name should be a string.
3. When create_character is called with a first argument that is a string it should not return The character name should be a string.
4. When create_character is called with a first argument that is an empty string, it should return The character should have a name.
5. When create_character is called with a first argument that is not an empty string, it should not return The character should have a name.
6. When create_character is called with a first argument that is longer than 10 characters it should return The character name is too long.
7. The create_character function should not say that the character is too long when it's not longer than 10 characters.
8. When create_character is called with a first argument that contains a space it should return The character name should not contain spaces.
9. When create_character is called with a first argument that does not contain a space it should not return The character name should not contain spaces.
10. When create_character is called with a second, third or fourth argument that is not an integer it should return All stats should be integers.
11. When create_character is called with a second, third and fourth argument that are all integers it should not return All stats should be integers.
12. When create_character is called with a second, third or fourth argument that is lower than 1 it should return All stats should be no less than 1.
13. When create_character is called with a second, third and fourth argument that are all no less than 1 it should not return All stats should be no less than 1.
14. When create_character is called with a second, third or fourth argument that is higher than 4 it should return All stats should be no more than 4.
15. When create_character is called with a second, third and fourth argument that are all no more than 4 it should not return All stats should be no more than 4.
16. When create_character is called with a second, third or fourth argument that do not sum to 7 it should return The character should start with 7 points.
17. When create_character is called with a second, third and fourth argument that sum to 7 it should not return The character should start with 7 points.
18. create_character('ren', 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.
19. When create_character is called with valid values it should output the character stats as required.