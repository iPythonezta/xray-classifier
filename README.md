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
Now enter the following code <br> <code>
from django.core.management.utils import get_random_secret_key</code><br>
<code>
get_random_secret_key() </code>
<br><br>
It will give an output like this 
<code>
'h9&0svk92@fl&=&^)&)02j!#3zqzset%#)e)w9hbarwzvmdapy'
</code>

In django's settings.py specify it as follow:
<code>
SECRET_KEY = "Your random key here"
</code></li></ol></p></li>

<li>
<h2> RunServer </h2>
<p>
Now finally, you are all set up! And you can simply start your server by following these simple steps.
<ol>
<li>
Open your terminal and navigate to cloned repository
</li>
<li>
<p>Enter <code>python manage.py runserver</code> <b>command</b> and a local server will be started at <code>127.0.0.1:8000</code> Here you dhould see a homepage like this:</p>
<img src="https://user-images.githubusercontent.com/87518251/184303955-8cb066f7-f248-4617-987c-21a8461a8c68.png" alt="Doctor Robo X ray classifier home page">

</li>
<li>
<p>To check xray click on the <b> Check X ray button </b> and you will see a page like this!</p> <br>
<img src="https://user-images.githubusercontent.com/87518251/184304628-d28f57a5-a373-46f6-945c-8b654555cd5e.png" alt="Doctor robo check x ray">
</li>

<li>
<p>
Give your image file a name and <b> upload the file </b> using the <b>choose file</b> button then <b>click upload</b> </p>
<p><b><i> If you only want to test there are some sample x ray files in the media folder, you can use one of them </i></b><p><br>
<img src="https://user-images.githubusercontent.com/87518251/184305338-904115e2-08fd-4013-b9d2-32e46277ba00.png" alt="choose a file">
</li>

<li>
<p>After choosing the file <b><i>Click the upload button</i></b> The file will then be passed to the ML model you downloaded earlier. The Model will then process the file and will present you with a result of Xray! </p><br>
<p>
The result will look like this: <br> </p>
<img src="https://user-images.githubusercontent.com/87518251/184306352-c3fa93bc-8991-4e00-b257-e75fd44b0c4c.png">

</li>

</ol>
</p>
</li>
</ol>

<h1>Contributor's Guide</h1>
<p>Incase you want to contribute to this project. Read this guide!</p>

<h2> How Can I contribute! </h2>
<ol>
<li> 
<h2>Documentation</h2> 
<p>You can contribute to the projects documentation by simply writing documentation <b><i> e.g how a function in views.py, urls.py or templates works ...</b></i></p>
</li>
<li>
<h2>Improving ML models </h2>
<p>You can also contribute by improving the existing ML models in the following ways </p>
<ul>
<li>Improve it's accuracy by training on more data or by using a different technique</li>
<li>You can add more classes to the model. So, it will be able to predict more diseases (e.g If model is currently predicting Pneumonia, Covid and normal classes you can add a class for TB)</li>
</ul>
<b><i> If you want to contribute in this way follow the following rules before creating a pull request </b></i>
<ol>
<li> Update the link to old model to the link to new model in README.md </li>
<li> In the commit/pull request description define how the new model is better </li>
<li>Provide a link to the notebook you used to create the updated model or simply upload the notebook to the repository as well </li>
<li> Make necessary changes to templates  & views.py for the <b>Updated mode</b></li>
<li> Provide references to data you used to create the updated model in commit/pull request description or in README.md file! </li>
</ol>
</li>

<li>
<h2> Creating a new model </h2>
<p> You can also contribute to the project by creating entirely new models (<b><i> e.g You can create a model to discover tumors in brain using MRIs or a model to find certain internal injuries </i></b>)</p>
<p><b><i> If you want to contribute in this way follow the following rules before creating a pull request </b></i></p>
<ol>
<li> Add a link t the new model in README.md while also wxplaining how to use it </li>
<li> In the commit/pull request description of the new model like what it does! </li>
<li>Provide a link to the notebook you used to create the updated model or simply upload the notebook to the repository </li>
<li> Create a new <b>Django App</b> inside the existing project for your model. You can use this command in the project's root directory <code> django-admin startapp 'app Name here' </code> </li>
<li> Add a reference to the new django app in the project's settings.py and urls.py </li>
<li> Provide references to data you used to create the model in commit/pull request description or in README.md file! </li>
</ol>
</li>
</ol>
