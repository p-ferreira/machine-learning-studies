# Machine learning studies

- Models of machine learning
    - Supervised learning
        - Binary classification
        Validation:
            - Cross validation (KFold)
            - Shuffle KFold
            - Stratified KFold
            - GroupKFold
            - Pipeline
            - GridSearchCV and RandomizedSearchCV for optimization of hyper-parameters

        Scikit:
        - Linear Support Vector Classification (Linear SVC)
        - Support Vector Classification (SVC)
        - Decision tree Classsifier
        - Dummy Classifier
        - Multinomial Naive Bayes
        - AdaBoost Classifier
        Multidimensional data:
            - Random Forest Classifier
            - Random Forest with SelectKBest
            - Evaluate results with Confusion Matrix
            - Random Forest with RFE (Recursive feature elimination)
            - Random Forest with RFECV (Cross-validation estimator)
            - Random Forest with PCA
            - Random Forest with TSNE
    - Unsupervised learning
        - K-Means
        - DBSCAN
        - Meanshift
        - Silhouette coefficient
        - Davies bouldin index calculation
        - Calinski Harabasz index calculation
        Validation:
            - Relative validation
            - Cluster structure validation
            - Cluster stability validation
    - Deep Learning
        Keras with Tensorflow
            - ReLu
            - Softmax
            - Export model to .h5 file
        PyTorch
            - ReLU
            - Perceptron
            - MLP (Multi-layer perceptron)
    - MLOps
        Create a web api to use a ml model using Flask and pickle
