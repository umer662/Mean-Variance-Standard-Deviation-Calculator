import numpy as np
def calculate(list):
  if len(list) == 9:
    list_np = np.array([list[:3], list[3:6], list[6:9]])
    calculations = {
      "mean": [],
      "variance": [],
      "standard deviation": [],
      "max": [],
      "min": [],
      "sum": []
    }
    calculations["mean"].append((np.mean(list_np, axis=0)).tolist())
    calculations["mean"].append((np.mean(list_np, axis=1)).tolist())
    calculations["mean"].append(np.mean(list))
    calculations["variance"].append((np.var(list_np, axis=0)).tolist())
    calculations["variance"].append((np.var(list_np, axis=1)).tolist())
    calculations["variance"].append(np.var(list))
    calculations["standard deviation"].append((np.std(list_np, axis=0)).tolist())
    calculations["standard deviation"].append((np.std(list_np, axis=1)).tolist())
    calculations["standard deviation"].append(np.std(list))
    calculations["max"].append((np.max(list_np, axis=0)).tolist())
    calculations["max"].append((np.max(list_np, axis=1)).tolist())
    calculations["max"].append(np.max(list))
    calculations["min"].append((np.min(list_np, axis=0)).tolist())
    calculations["min"].append((np.min(list_np, axis=1)).tolist())
    calculations["min"].append(np.min(list))
    calculations["sum"].append((np.sum(list_np, axis=0)).tolist())
    calculations["sum"].append((np.sum(list_np, axis=1)).tolist())
    calculations["sum"].append(np.sum(list))
    return calculations
  else:
    raise ValueError("List must contain nine numbers.")
