import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

# Загрузка данных
data_path = './titanic.csv'
titanic_data = pd.read_csv(data_path)

# Удаление столбцов, которые не будем использовать
titanic_data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Заполнение пропущенных значений
imputer = SimpleImputer(strategy='mean')
titanic_data['Age'] = imputer.fit_transform(titanic_data[['Age']])
imputer_mode = SimpleImputer(strategy='most_frequent')
titanic_data['Embarked'] = imputer_mode.fit_transform(titanic_data[['Embarked']])

# Кодирование категориальных признаков
le_gender = LabelEncoder()
titanic_data['Gender'] = le_gender.fit_transform(titanic_data['Gender'])
onehot_columns = ['Embarked']
onehot_transformer = ColumnTransformer(transformers=[('onehot', OneHotEncoder(), onehot_columns)], remainder='passthrough')
titanic_data = pd.DataFrame(onehot_transformer.fit_transform(titanic_data), columns=onehot_transformer.get_feature_names_out())

# Нормализация числовых данных
scaler = StandardScaler()
numerical_features = ['remainder__Age', 'remainder__Fare', 'remainder__SibSp', 'remainder__Parch']
titanic_data[numerical_features] = scaler.fit_transform(titanic_data[numerical_features])

# Разделение данных на признаки и целевую переменную
X = titanic_data.drop('remainder__Survived', axis=1)
y = titanic_data['remainder__Survived']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение моделей
# Логистическая регрессия
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)
y_pred_logistic = logistic_model.predict(X_test)
f1_logistic = f1_score(y_test, y_pred_logistic)

# K-ближайших соседей
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)
f1_knn = f1_score(y_test, y_pred_knn)

# Вывод результатов
print(f"F1 Score for Logistic Regression: {f1_logistic}") # 0.761
print(f"F1 Score for KNN: {f1_knn}") # 0.374

# Логистическая регрессия показала значительно лучшие результаты по сравнению с методом ближайших соседей