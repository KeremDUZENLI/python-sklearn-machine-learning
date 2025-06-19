import pandas as pd
import time

from sklearn.model_selection   import train_test_split
from sklearn.preprocessing     import LabelEncoder, StandardScaler
from sklearn.pipeline          import Pipeline
from sklearn.naive_bayes       import GaussianNB
from sklearn.linear_model      import LogisticRegression
from sklearn.tree              import DecisionTreeClassifier
from sklearn.ensemble          import RandomForestClassifier
from sklearn.svm               import SVC
from sklearn.neighbors         import KNeighborsClassifier
from sklearn.neural_network    import MLPClassifier


models = [
    ('Naive Bayes (Gaussian)'                  , GaussianNB()),
    ('Logistic Regression (ridge)'             , LogisticRegression(penalty='l2', solver='lbfgs', max_iter=1000, random_state=42)),
    ('Deep Neural Network (two hidden layers)' , MLPClassifier(hidden_layer_sizes=(64,32), max_iter=500, random_state=42)),
    ('Decision Tree (CART)'                    , DecisionTreeClassifier(random_state=42)),
    ('Random Forest (100 trees)'               , RandomForestClassifier(n_estimators=100, random_state=42)),
    ('Support Vector Machine (RBF Kernel)'     , SVC(kernel='rbf', random_state=42)),
    ('k-Nearest Neighbors'                     , KNeighborsClassifier()),
]

def evaluate_model(X_tr, X_te, y_tr, y_te, name, model):
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf',    model),
    ])
    start = time.time()
    pipe.fit(X_tr, y_tr)
    accuracy = pipe.score(X_te, y_te) * 100
    elapsed  = time.time() - start
    return name, accuracy, elapsed


for filepath in files:
    print(f"\n=== Results for {filepath} ===")
    df = pd.read_csv(filepath)
    
    X = df.drop(['elo', 'cluster'], axis=1)
    y = LabelEncoder().fit_transform(df['cluster'])
    
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    results = []
    for name, model in models:
        results.append(evaluate_model(X_tr, X_te, y_tr, y_te, name, model))

    results.sort(key=lambda x: x[1], reverse=True)
        
    print(f"{'Model':<40} │ {'Accuracy (%)':<20} │ {'Time (s)':<10}")
    print('─' * 100)

    for name, acc, elapsed in results:
        print(f"{name:<40} │ {acc:<20.3f} │ {elapsed:<10.3f}")
