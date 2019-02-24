# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg acceptanceletter

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

 #   show eileen happy

    # These display lines of dialogue.

    e "Congratulations!"
    e "Based on your application, you have been selected to be a summer intern at the Erstwhile House!"
    e "The experience you will gain from an internship  experience is a valuable addition to your academic course work."
    e "The materials provided will be helpful to you as you begin your internship. Please read this packet in its entirety to ensure preparedness for you arrival."
    e "We look forward to working with you!"

    # This ends the game.

    return
