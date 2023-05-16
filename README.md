# MORANTEL
This is a resource for students in the Levandoski Lab, working with MD Simulations. I will add all the codes I created for running the simulations and its analysis.

#Finding Missing Residues.ipynb
Because of the transmembrane characteristic of nAChR, microscopy and methods of modeling its structure haven’t reached full resolution yet. Then, the .pdb files miss residues from the structure that need to be acknowledged before running molecular dynamics simulations. In this jupiter notebook, you can get a spreadsheet that will tell you what are the residues. Although sometimes Chimera may be faster for you to find them out, this can serve as an alternative in extreme cases.

#RMS.MDAnalysis.ipynb
This is a fully annotated MDAnalysis notebook for you to get the basics of RMSD and RMSF analysis. They will be very helpful when creating plots for your poster/paper.

#prepfiles.py
You will need to run this in the commandline of the cluster server. For that, I usually make a folder inside the folder where the simulation is being computed and paste this document through the Moab viewpoint interface. You may need to give it permission once you paste it in there. Then, I enter the cluster through my computer's Terminal app (as it is in Mac), and through the commandline I run this document by typing 'python3 prepfiles.py'. If you need to make any alteration in the code, the easiest way is to run the code 'vi prepfiles.py' in the commandline and change them there. NOTE: you will want to run this command before trjcat.bash

#trjcat.bash
You will need to run this in the commandline of the cluster server. For that, I usually make a folder inside the folder where the simulation is being computed and paste this document through the Moab viewpoint interface. You may need to give it permission once you paste it in there. Then, I enter the cluster through my computer's Terminal app (as it is in Mac), and through the commandline I run this document by typing './trjcat.bash'. NOTE: You need to run prepfiles.py before you run this one.
