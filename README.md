### SER (Speech emotion recognition) research 

This repo consists of main source code files, used for diploma research.

#### Bucket setup
Let's start from data setup. First of all, I created a bucket on the project in the Google Cloud. This was made because of the size of dataset. It's too large to load it on the Google Colab, where I use GPU/TPU engines to make model learning faster.
So, firstly I installed Google Cloud CLI on my desktop.
Then I logged in and chose my project with created bucket. Then I run in the terminal the following command:
```PowerShell
gsutil -m cp -r D:\Diploma\data\MC-EIU-audio gs://mc-eiu-dataset/
```

After 