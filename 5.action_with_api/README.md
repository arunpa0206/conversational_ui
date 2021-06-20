Step 1: Create new RASA project
        rasa init

Step 2: Add covid tracker story to stories.yml 
        add  state intent to nlu.yml
        add intent, action and response to domain.yml
        create actions.py for custom action with external api

step 3: Run the action server
        rasa run actions
        
Step 4: For run sample bot, first train 
        rasa train
        rasa shell