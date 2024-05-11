import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Загрузка данных
data_path = './users_behavior.csv'
users_data = pd.read_csv(data_path)

# Разделение данных на признаки и цель
features = users_data.drop(['Unnamed: 0', 'is_ultra'], axis=1)
target = users_data['is_ultra']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Обучение модели логистической регрессии
logistic_model = LogisticRegression(random_state=42, max_iter=1000)
logistic_model.fit(X_train, y_train)
y_pred_logistic = logistic_model.predict(X_test)
accuracy_logistic = accuracy_score(y_test, y_pred_logistic)

# Обучение модели дерева решений
decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)
y_pred_tree = decision_tree_model.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_pred_tree)

# Обучение модели случайного леса
random_forest_model = RandomForestClassifier(random_state=42)
random_forest_model.fit(X_train, y_train)
y_pred_forest = random_forest_model.predict(X_test)
accuracy_forest = accuracy_score(y_test, y_pred_forest)

# Вывод результатов
print("Accuracy of Logistic Regression:", accuracy_logistic)
print("Accuracy of Decision Tree:", accuracy_tree)
print("Accuracy of Random Forest:", accuracy_forest)
