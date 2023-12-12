# Cellphone Price Prediction Project 📱

🚀 **Welcome to the Cellphone Price Prediction project!** 

## Data Preprocessing 🛠️

In the data preprocessing phase, we tackled corrupted values by replacing them with 0 using the median. Outliers in the front camera (fc) feature were handled using the IQR method. Skewness in the front camera feature was observed during data distribution analysis but deemed not impactful on the target variable.

## Feature Selection 🔍

Feature selection involved using a heatmap to check correlations among features. Notably, the correlation between pc vs fc and three_g vs four_g was found to be below the threshold (85-90%), hence these features were retained.

## Multiclass Classification 🎯

As the output feature column involves multiclass classification, various machine learning algorithms were employed and their performances evaluated using F1 scores. The algorithms considered include:
- Logistic Regression
- RandomForest Classifier
- SVM Classifier
- Decision Tree Classifier
- AdaBoost Classifier
- GradientBoosting Classifier
- XGB Classifier
- Naive Bayes Classifier
- KNeighbors Classifier

## Model Performance 📊

RandomForest Classifier, SVM Classifier, GradientBoosting Classifier, and XGB Classifier exhibited better performance than other models.

## Hyperparameter Tuning 🔧

After hyperparameter tuning, RandomForest Classifier continued to outperform other models, demonstrating its robustness and suitability for the task.

## Model Selection 🏆

RandomForest Classifier was chosen as the final model for predicting cellphone prices due to its consistent high accuracy.

## Deployment 🚀

The project has been deployed on [PythonAnywhere](http://praveenbharti.pythonanywhere.com/), enabling real-time predictions based on the selected model.

## Conclusion 🔮

The Cellphone Price Prediction project showcases the effectiveness of the RandomForest Classifier in predicting cellphone prices based on given features. This model is poised to provide valuable insights into market trends and consumer preferences.

Feel free to explore the deployed project and dive into the fascinating world of cellphone price prediction! 🌐