import tweepy
import wget
import tensorflow as tf
import numpy as np
from keras.preprocessing import image




consumer_key         = "#####################" # Fill with your consumer key
consumer_secret      = "###################" # fill with your consumer secret key
access_token  = "#########################" # Fill with your access token
access_token_secret  = "#############################" # Fill with access token secret

x = [] # initializing an empty list to store tweet ids


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


model = tf.keras.models.load_model('Classifier\\trained_models\\LossOptimized')  # loading model

def predict_label(img, model=model):

    """
        This function returns the LABEL of the given image by using MODEL
        If the function is not working then check if you have installed the
        LossOptimized model at the right direction..
    """


    img = image.load_img(img, target_size=(250, 250))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images)

    label = tf.keras.backend.argmax(classes)
    print(label[0])
    print(classes)
    encode_label = np.argmax(classes,axis=1)
    lb = {}
    for key,value in enumerate({'Covid': 0, 'Normal': 1, 'Pneumonia': 2}):
        lb[key] = value

    chances = str(max(classes.flatten().tolist())*100)[:4] + '%'

    encoded = lb[encode_label[0]]
    if encoded == 'Covid':
        statement = """Doctor Robo suggests that you might have COVID 19!\n 
        Currently DOCTOR ROBO is for research purposes only!  So seek advice from your doctor :)
        
        """
    elif encoded == 'Pneumonia':
        statement = """Doctor Robo suggests that you might have Viral Pneumonia in your lungs!
        Currently DOCTOR ROBO is for research purposes only!  So seek advice from your doctor :)
        
        """
    else:
        statement =  'As per DOCTOR ROBO\'s assessment your lungs are Normal but actually DOCTOR ROBO is based on AI and is prone to error!   So seek advice from your doctor :)'

    
    return statement,chances,encoded

while True:
    for results in tweepy.Cursor(api.search_tweets, q="@XrayBotML checkxray").items(20):   #You can replace @XrayBotML with your twitter Username
        print((results.text).encode('utf-8').strip())
        if 'media' in results.entities:
            if results.id not in x:
            
                for imgs in  results.entities['media']:

                    filename = wget.download(imgs['media_url'])

                    statement,chances,encoded = predict_label(filename)
                    tweet = 'Detected Disease: {} \n\nChances:{}\n\nOur Statement:{}'.format(encoded,chances,statement)[:260] +'\n Credit: @iPythonista'

                    print("Here is the generated tweet .........." )
                    print()
                    print(tweet)

                    st = api.update_status(status=tweet, in_reply_to_status_id=results.id, auto_populate_reply_metadata=True)

                    print('Replied Successfully')
                    x.append(results.id)
            else:
                print('Already replied to this tweet!')

        else:
            api.update_status(status='You didn\'t uploaded your Xray file!', in_reply_to_status_id=results.id, auto_populate_reply_metadata=True)
            
