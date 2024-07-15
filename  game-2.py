import random  # Importing the random module for shuffling flashcards.

class Flashcard:
    '''
    This class represents a flashcard with a term and its definition.

    Attributes:
        term (str): The term for the flashcard.
        definition (str): The definition for the flashcard.
    '''

    def __init__(self, term, definition):
        '''
        Initializes the Flashcard object with the given term and it's correct definition.

        Args:
            term (str): The term for the flashcard.
            definition (str): The definition for the flashcard.
        '''
        self.term = term
        self.definition = definition


class StudyQuestzGame:
    '''
    This class represents the StudyQuestz flashcard game, gamifying learning.

    Attributes:
        flashcards(list): List to hold flashcard objects for the game.
        points (int): User's points in the game collected by correct to wrong results.
    '''

    def __init__(self):
        '''
        Initializes the StudyQuestzGame object with an empty list of flashcards and zero points.
        '''
        self.flashcards = []
        self.points = 0

    def add_flashcard(self, card, definition):
        '''
        Adds a new flashcard to the game.

        Args:
            card (str): The term for the flashcard.
            definition (str): The definition for the flashcard.
        '''
        flashcard = Flashcard(card, definition)
        self.flashcards.append(flashcard)

    def input_flashcard(self):
        '''
        Takes user input to create a new flashcard and adds it to the game.
        '''
        card = input("Enter the term: ")
        definition = input("Enter the definition: ")
        self.add_flashcard(card, definition)

    def create_quiz(self, shuffle=False):
        '''
        Create a personalized quiz by shuffling flashcards if specified.

        Args:
            shuffle (bool): To randomize order in the pattern flashcards are presented by using function shuffle.
        '''
        if shuffle:
            random.shuffle(self.flashcards)

    def play_game(self):
        '''
        Initiates the quiz and tracks user points.
        '''
        print("\nWelcome to StudyQuestz! Accomplish learning in game form, Let's kick off the quest.\n")

        # Allow the user to input their own flashcards they wish to learn
        while True:
            add_more = input("Do you want to add a flashcard? (yes/no): ").lower()
            if add_more != 'yes':
                break
            self.input_flashcard()

        # Shuffle flashcards at random
        shuffle_option = input("Do you want to shuffle the flashcards before the quiz? (yes/no): ").lower()
        self.create_quiz(shuffle=shuffle_option == 'yes')

        # Quiz: Assessment for testing users knowledge on each flashcard
        for flashcard in self.flashcards:
            user_answer = input(f"What is the definition of '{flashcard.term}'? ")
            if user_answer.lower() == flashcard.definition.lower():
                print("Correct!")
                self.points += 1
            else:
                print(f"Wrong! The correct definition is: {flashcard.definition}")

        # Display user's points
        print(f"\nQuiz completed! You scored {self.points} points.")

# Example usage
if __name__ == "__main__":
    study_questz_game = StudyQuestzGame()
    study_questz_game.play_game()