import Scores_dict
import numpy as np
import matplotlib.pyplot as plt
Scores = Scores_dict.scores.values();
lis=[];
for i in range(1,31):
    lis.append(i)
Days = np.array(lis);
plt.plot(Scores, Days)
plt.xlabel('Score');  
plt.ylabel('Days'); 
plt.title('Score vs. Days'); 
plt.show() 

mean = np.mean(list(Scores));
medium = np.median(list(Scores));
max_score = np.max(list(Scores));
min_score = np.min(list(Scores));

print("mean OF Scores: - ",mean)
print("median OF Scores: - ",medium)
print("maximum OF Scores: - ",max_score)
print("Minimum OF Scores: - ",min_score)