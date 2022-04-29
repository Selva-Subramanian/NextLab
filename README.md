# NextLab
# Deployment of Streamlit WebApp via Streamlit share 

* Deployed the app in streamlit share.
* It need two files app.py which contains the code required for building the app and requirements.txt which has all the necessary python packages.

streamlit link: https://share.streamlit.io/selva-subramanian/nextlab/main/app.py

![Screenshot (673)](https://user-images.githubusercontent.com/81951194/165764491-cf8c7aa8-0e13-489e-992b-3dc80f0f9e63.png)

# difficult problem that I solved.
While clustering restaurants based on the cuisines offered, I had to convert the cuisines which was a lists of texts into numbers such that restaurants that offered the same cuisines were to be closer to each other compared to the restaurants that offered a different cuisines. Clustering needs numerical values to compare distances, even gower distance didn't work as the values were not categorical data so I had to come up with a custom function to quantify the cuisines. The following image contains the code for the solution.

![Screenshot (680)](https://user-images.githubusercontent.com/81951194/165889667-fc9ca978-f3a4-4db8-a613-ae5f52876212.png)
