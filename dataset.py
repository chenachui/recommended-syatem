from collections import defaultdict
import Trainset


# 从文件中加载数据并创建训练集
def construct_train_set(data_set):
    raw_users_id = dict()
    raw_items_id = dict()
    ur = defaultdict(list)
    ir = defaultdict(list)
    u_index = 0
    i_index = 0

    for ruid, riid, rating in data_set:
        # 外部userid到内部userid的映射
        try:
            uid = raw_users_id[ruid]
        except KeyError:
            uid = u_index
            raw_users_id[ruid] = uid
            u_index += 1
        # 外部itemid到内部itemid的映射
        try:
            iid = raw_items_id[riid]
        except KeyError:
            iid = i_index
            raw_items_id[riid] = iid
            i_index += 1

        ur[uid].append([iid, rating])
        ir[iid].append([uid, rating])
    n_users = len(ur)
    n_items = len(ir)
    n_ratings = len(data_set)
    rating_scale = (0, 100)
    trainset = Trainset.Trainset(ur, ir, n_users, n_items, n_ratings, raw_users_id, raw_items_id, rating_scale)
    return trainset
