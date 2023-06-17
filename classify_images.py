#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Ola Omar Abu Shab
# DATE CREATED:6/6/2023                     
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):

#     with open('imagenet1000_clsid_to_human.txt','r') as file:
#         file_contents = file.read()
#         new = file_contents.lower()
#         data_dict = eval(new)
#         classifier_list = list(data_dict.values())                
    
   
    
    for key in results_dic:    
        
        
        img_path = images_dir + key
        classfier_label = classifier(img_path, model)
        classfier_label = classfier_label.lower().strip()
        pet_label = results_dic[key][0]
       # pet_label_1 = pet_label.strip()
        results_dic[key].append(classfier_label)
#         print("classfier_label" + classfier_label)
#         print("pet_label" + pet_label)
        
        if pet_label in classfier_label:
            print(type(classfier_label))
            print("true")
            #new_list = [classfier_label,1]
            #results_dic[key].extend(new_list)
            results_dic[key].append(1)
            
        else:
            print("false")
            #new_list = [classfier_label,0]
            #results_dic[key].extend(new_list)
            results_dic[key].append(0)
           
            
        
        
        
        
#     for idx in range (0, len(filename_list), 1):
#         if filename_list[idx] not in results_dic:
#             print("done")
#             results_dic[filename_list[idx]] = [ petlable_list[idx], classifier_list[idx] ]
#         print(petlable_list[idx]) 
#         print("done2")
#         if petlable_list[idx] in classifier_list:
#             print("done")
#             new_list = [classifier_list[idx],1]
#             results_dic[filename_list[idx]].extend(new_list)
#         else:
#             new_list = [classifier_list[idx],0]
#             results_dic[filename_list[idx]].extend(new_list)            
        

            

    None 