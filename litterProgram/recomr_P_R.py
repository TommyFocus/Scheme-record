# 评分预测的准确度计算

"""
DATA:
records[i] = [u, i, rui, pui]，其中的元素皆为列向量
u:用户
i:物品
rui:算法预测的用户u对物品i的评分
pui:用户的真实评分
"""

# RMSE:均方根误差
def RMSE(records):
	return math.sqrt(
			sum([(rui - pui) ** 2 for u, i, rui, pui in records])
		) / float(len(records))

#RMSE加大了对预测不准的用户物品评分的惩罚（平方向的惩罚）

# MAE:平均绝对误差
def MAE(records):
	return sum([abs(rui - pui) for u, i, rui, pui in records]) / float(len(records))

#评分系统是基于整数建立的，对预测的结果取整会降低MAE的误差

#TopN推荐

"""
R(u)根据用户在训练集上的给出的用户推荐表
T(u)是用户在测试集上的行为表
"""
def PrecisionRecall(test, N):
	hit = 0
	n_recall = 0
	n_precision = 0
	for user, items in test.items():
		rank = Recommend(user, N)
		hit += len(rank & items)
		n_recall += len(items)
		n_precision += N
	return [hit / (1.0 * n_recall), hit / (1.0 * n_precision)]

#TopN更符合实际的需求，即给出用户可能感兴趣的电影的列表，而不是关注用户会给予多少的评分


