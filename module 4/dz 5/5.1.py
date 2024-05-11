from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Настройка параметров для GridSearchCV
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [1, 2],
    'min_samples_split': range(2, 11)  # Значения от 2 до 10 включительно
}

# Создание модели дерева решений
dt = DecisionTreeClassifier()

# Создание и выполнение GridSearchCV
grid_search = GridSearchCV(estimator=dt, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Лучшие параметры и оценка точности
best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_estimator = grid_search.best_estimator_

# Оценка на тестовой выборке
y_pred = best_estimator.predict(X_test)
accuracy_test = accuracy_score(y_test, y_pred)

print(best_params, best_score, accuracy_test)
# ({'criterion': 'gini', 'max_depth': 2, 'min_samples_split': 2},
# 0.9166666666666667,
# 0.9666666666666667)
