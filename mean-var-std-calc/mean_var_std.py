import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    arr_flattened = np.array(list)
    arr = np.reshape(arr_flattened, (3,3))
    calculations = {
        'mean': [np.mean(arr, axis=0).tolist(),np.mean(arr, axis=1).tolist(),np.mean(arr_flattened)],
        'variance': [np.var(arr, axis=0).tolist(),np.var(arr, axis=1).tolist(),np.var(arr_flattened)],
        'standard deviation': [np.std(arr, axis=0).tolist(),np.std(arr, axis=1).tolist(),np.std(arr_flattened)],
        'max': [np.max(arr, axis=0).tolist(),np.max(arr, axis=1).tolist(),np.max(arr_flattened)],
        'min': [np.min(arr, axis=0).tolist(),np.min(arr, axis=1).tolist(),np.min(arr_flattened)],
        'sum': [np.sum(arr, axis=0).tolist(),np.sum(arr, axis=1).tolist(),np.sum(arr_flattened)],
    }
    return calculations