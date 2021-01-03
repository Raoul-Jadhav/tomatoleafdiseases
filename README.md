# Tomato Leaf Disease Classification

# Transfer Learning:
  <h3>What Is Transfer Learning ?</h3>
  <p>Training a CNN from scratch is possible for small projects, most applications require the training of very large CNN’s and this as you guessed, takes extremely huge amounts of processed data and computational power. And both of these are not found so easily these days.That’s where transfer learning comes into play. In transfer learning, we take the pre-trained weights of an already trained model(one that has been trained on millions of images belonging to 1000’s of classes, on several high power GPU’s for several days) and use these already learned features to predict new classes.</p>
  
<h4>The advantages of transfer learning are that:</h4>
<ul><li>There is no need of an extremely large training dataset.</li>
<li>Not much computational power is required. As we are using pre-trained weights and only have to learn the weights of the last few layers.</li></ul>

There are several models that have been trained on the image net dataset and have been open sourced. For example, VGG-16, VGG-19, Inception-V3 etc.

 <h3>The model used for classification is InceptionV3 </h3>
  <p>The InceptionV3 is the third iteration of the inception architecture, first developed for the GoogLeNet model.</p>
  <p>This model was developed by researchers at Google and described in the 2015 paper titled “Rethinking the Inception Architecture for Computer Vision.”</p>
The model can be loaded as follows:

<p>import tensorflow as tf</p>
<p>from tensorflow.keras.layers import Input, Dense, Flatten, Lambda</p>
<p>from tensorflow.keras.models import Model</p>
<p>from tensorflow.keras.applications.inception_v3 import InceptionV3</p>
<p>from tensorflow.keras.applications.inception_v3 import preprocess_input</p>
