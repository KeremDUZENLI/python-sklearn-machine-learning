from sklearn.pipeline          import Pipeline
from sklearn.preprocessing     import StandardScaler

from sklearn.naive_bayes       import GaussianNB
from sklearn.linear_model      import LogisticRegression
from sklearn.neural_network    import MLPClassifier
from sklearn.tree              import DecisionTreeClassifier
from sklearn.ensemble          import RandomForestClassifier
from sklearn.svm               import SVC
from sklearn.neighbors         import KNeighborsClassifier

import time


MODELS = [
    ('Naive Bayes (Gaussian)'                  , GaussianNB()),
    ('Logistic Regression (ridge)'             , LogisticRegression(penalty='l2', solver='lbfgs', max_iter=1000, random_state=42)),
    ('Deep Neural Network (two hidden layers)' , MLPClassifier(hidden_layer_sizes=(64,32), max_iter=500, random_state=42)),
    ('Decision Tree (CART)'                    , DecisionTreeClassifier(random_state=42)),
    ('Random Forest (100 trees)'               , RandomForestClassifier(n_estimators=100, random_state=42)),
    ('Support Vector Machine (RBF Kernel)'     , SVC(kernel='rbf', random_state=42)),
    ('k-Nearest Neighbors'                     , KNeighborsClassifier()),
]


def evaluate_models(X_train, X_test, y_train, y_test):
    results = []
    for name, model in MODELS:
        pipe = Pipeline([
            ('scaler', StandardScaler()),
            ('clf',    model),
        ])
        start = time.time()
        pipe.fit(X_train, y_train)
        accuracy = pipe.score(X_test, y_test) * 100
        elapsed  = time.time() - start
        results.append((name, accuracy, elapsed))

    return results
