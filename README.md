# Xray Classifier
Classify different disease based on Xrays! It currently classifies Covid 19, pneumonia and normal lungs with an accurracy of 93.3%


<h1> User Guide </h1>

<b><i> Please read this guide before using this repository. Otherwis errors might occurr! </i></b>

<ol>

<li>
<h2> Installing the Model </h2>
<p> The trained model was too big to be uploaded on Github. So, I decided to upload in on Google Drive from where you can acccess it </p>
<p> In future when the new/updated models will be trained, the link to them will be included in this file along with the instructions on how to use it </p>
<hr>
<p> So first of all download the model from  <a href="https://drive.google.com/file/d/1KBKUyLmSb7fHo5_uhpFZvi9661hEF4f8/view?usp=sharing"> this link </a></p>
<p> After downloading the <code>LossOptimized.zip</code> file extrat its content to <code>Classifier\trained_models</code> in the project's directory.</p>
<p> Your model should now be available at the following location </p>
<code> xray-classifier\Classifier\trained_models\LossOptimized </code>

<b>Don't rename the <code> LossOptimized </code> to anything else otherwise the webapp will give errors!</b>

</li>
<li>
<h2>Add Django SECRET_KEY </h2>
<p>
Every django app needs a security key to work & when you create a django app by using command line interface it ccomes up with a security key!
But because this project is public. So, to prevent you guys from hacking (incase you deployed the app using the same security key) I removed the SECRET_KEY!
Here is how to generate a security key for your app!
<ol>
<li>
In the shell type <code> django-admin shell </code>
</li>
<li>
Now enter the following code <code>
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
</code><br><br>
It will give an output like this 
<code>
'h9&0svk92@fl&=&^)&)02j!#3zqzset%#)e)w9hbarwzvmdapy'
</code>

In django's settings.py specify it as follow:
<code>
SECRET_KEY = "Your random key here"
</code>
</li>
</ol>
</p>
</li>
</ol>

