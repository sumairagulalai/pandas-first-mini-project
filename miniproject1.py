# student result 
import pandas as pd
csv = pd.read_csv("C:\\Users\\sumai\\OneDrive\\student2.csv")
print(csv)
# average 
csv["avg"]=(csv["math"]+csv["science"]+csv["english"])/3
print(csv)
csv["result"] = "Pass"
csv.loc[csv["avg"] < 50, "result"] = "Fail"

print(csv[["name", "avg", "result"]])

csv.to_csv("result.csv", index=False)
print("complete successfully ✅ ")