# Use a Pre-trained Image Classifier to Identify Dog Breeds

This repository contains the project "Use a Pre-trained Image Classifier to Identify Dog Breeds" as part of the "Programming in Python for AI" Nanodegree at Udacity.

## Project Goal

The primary objective of this project is to improve my programming skills using Python. The focus is on implementing the logic and functionality of the project rather than creating the image classifier itself.

## Languages and tools

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></p>

## Program Outline

The capstone project required us to do the following:

1. Time the program
   - Use Time Module to compute program runtime
2. Get program Inputs from the user
   - Use command line arguments to get user inputs
3. Create Pet Images Labels
   - Use the pet images filenames to create labels
   - Store the pet image labels in a data structure (e.g., a dictionary)
4. Create Classifier Labels and Compare Labels
   - Use the Classifier function to classify the images and create the classifier labels
   - Compare Classifier Labels to Pet Image Labels
   - Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
5. Classifying Labels as 'dogs' or 'not Dogs'
   - Classify all Labels as 'dogs' or 'not dogs' using a dognames.txt file
   - Store new classifications in the complex data structure (e.g. dictionary of lists)
6. Calculate the Results
   - Use Labels and their classifications to determine how well the algorithm worked on classifying images
7. Print the Results
  
## Forecasted Difficulties

While working on this project, you may encounter the following difficulties:

- Handling hidden files: Ensure that files starting with '.' are ignored when processing the images.
- Correctly matching the classifier's labels with the pet image labels: Validate the matches and non-matches between the two to accurately classify the labels as "dogs" or "not dogs."
- Evaluating and comparing the performance of different CNN model architectures: Analyze the results obtained from ResNet, AlexNet, and VGG to determine which architecture performs the best in terms of classifying dog breeds.
  
  
## Results for the Project

After analyzing the results, I found that the "best" model architecture for this project is VGG. It outperformed both ResNet and AlexNet when considering both objectives 1 and 2. Although ResNet had better accuracy in classifying dog breeds, only VGG and AlexNet achieved 100% accuracy in classifying "dogs" and "not-a-dog." VGG exhibited the best overall performance, with a breed classification accuracy of 93.3%.
  
