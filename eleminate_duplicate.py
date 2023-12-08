# Function to eliminate duplicate words and write each unique word on a new line in a text file
#this code helps us find duplicate words in the list of somali stop-words
def eliminate_and_format(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the contents of the file and split it into words
            words = file.read().split()

            # Create an empty set to store unique words
            unique_words = set()

            # Iterate through the words and add them to the set
            for word in words:
                unique_words.add(word)

        # Open the file in write mode to write unique words back with each on a new line
        with open(filename, 'w') as file:
            # Write the unique words on separate lines
            file.write('\n'.join(unique_words))

        # Display confirmation message
        print(f"Duplicates eliminated and words formatted in '{filename}'.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the filename you want to process
filename = "stopwords.txt"

# Call the function to eliminate duplicates and format the words in the file
eliminate_and_format(filename)
#UESTC