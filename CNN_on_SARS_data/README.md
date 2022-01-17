# port_congestion

<h1>How to run the code</h1>

<h2>Step 1: download data</h2>
<p>
  The dataset can be found
  <a href="https://github.com/TianwenZhang0825/LS-SSDD-v1.0-OPEN">here</a>
</p>
Download it and put it in the root folder

<h2>Step 2: download packages</h2>
<p>Make sure you install the packages in requirements.txt</p>

<h2>Step 3: data preprocessing</h2>
<p>Run <i>data_preprocessing1.py</i> to convert the xml to json</p>
<p>
  Run <i>data_preprocessing2.py</i> to convert images and json data to npy
  format
</p>

<h2>Step 4: train the model</h2>
<p>
  Run <i>train.py</i> to train the model. The model will be saved as
  <i>leaky_CNN.h5</i>
</p>

<h2>Step 5: start the program to predict how many ships there are</h2>
<p>
  Run <i>prediction.py</i> anh you will be prompted to enter the path to a
  image. The program will count how many ships there are for you
</p>

<h1>
  You can run <i>script.sh</i> to start the program but I recommend going steps
  by steps to keep track of the progress better
</h1>

<h1>Finally, file structure should look like <i>structure.txt</i></h1>
