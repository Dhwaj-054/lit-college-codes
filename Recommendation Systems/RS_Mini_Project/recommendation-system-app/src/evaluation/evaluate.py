def evaluate_model(predictions, true_labels):
    from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score

    mse = mean_squared_error(true_labels, predictions)
    mae = mean_absolute_error(true_labels, predictions)
    accuracy = accuracy_score(true_labels, predictions)

    evaluation_results = {
        'Mean Squared Error': mse,
        'Mean Absolute Error': mae,
        'Accuracy': accuracy
    }

    return evaluation_results

def evaluate_recommendations(model, test_data):
    predictions = model.predict(test_data)
    true_labels = test_data['true_labels']  # Assuming true_labels are part of the test_data

    results = evaluate_model(predictions, true_labels)

    return results