

from metrices.mse import mse
from metrices.mbe import mbe
from metrices.mbeperc import mean_absolute_percentage_error
from metrices.accuracyscore import accuracy_score

y_true = [2, 4, 6, 8]
y_pred = [1.5,2.3,7.8,9.9]
from metrices.accuracyscore import accuracy_score

y_true_cls = [0, 1, 1, 2]
y_pred_cls = [0, 1, 0, 0]

print("Accuracy:", accuracy_score(y_true_cls, y_pred_cls))


print("Mean squared error :", mse(y_true, y_pred))
print("Mean absolute error :", mbe(y_true, y_pred))         
print("Mean absolute percentage error:", mean_absolute_percentage_error(y_true, y_pred))





