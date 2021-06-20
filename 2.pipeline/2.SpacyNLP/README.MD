Step 1: For run the bot, first train 
        rasa train

step 2: To check the confidence value of message
        rasa shell nlu

Step 3: Provide input as "hi","good" and "find"
        check the intent had highest confident score
        Note that "hi" is mapped to greet intent with high confidence
        Note that "good" is mapped to mood_happy intent with high confidence
        Note that "fine" is mapped to mood_happy intent with high confidence
 