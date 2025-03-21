from math import sqrt
import gensim.downloader as api
import numpy as np

# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
# 25, 50, 100 or 200. The larger the number, the more accurate, but the longer it runs.
model = api.load("glove-twitter-25")
word = "beautiful"
vector = model[word]
print(vector)
# [-1.5578   -0.99442   0.30093   0.055712  0.096052  0.29998   2.1864
#   0.38417  -1.0875   -0.63333  -0.73723   0.40719  -4.343     0.062952
#  -1.08     -0.27538   0.32506  -0.31789  -0.19544   0.64269  -0.021329
#  -0.32933  -0.76828  -0.054674 -0.41345 ]
print(type(vector))
# <class 'numpy.ndarray'>
def demo():
    print("1----------")
    result = model.most_similar(word, topn=10)
    print(result)
    # [('gorgeous', 0.933364748954773), ('lovely', 0.9279096722602844), ('amazing', 0.9218392968177795), ('love', 0.9173233509063721), ('wonderful', 0.9150214195251465), ('loving', 0.9093380570411682), ('dream', 0.9086582660675049), ('pretty', 0.9071912169456482), ('perfect', 0.9066720604896545), ('little', 0.9064547419548035)]
    
    print("2----------")
    result = model.most_similar(positive=["january", "february"], topn=10)
    print(result)
    # [('march', 0.970687747001648), ('october', 0.9691615104675293), ('june', 0.9538877010345459), ('december', 0.9475950002670288), ('august', 0.9452325701713562), ('july', 0.9375306963920593), ('november', 0.9197095632553101), ('dec', 0.8917481303215027), ('monday', 0.8903120756149292), ('wednesday', 0.8874314427375793)]
    
    print("3----------")
    result = model.similarity("man", "woman")
    print(result)
    # 0.76541775

    print("4----------")
    result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
    print(result)
    # [('meets', 0.8841923475265503)]

    print("5----------")
    result = model.most_similar(positive=["berlin", "vietnam"], negative=["hanoi"], topn=1)
    print(result)
    # [('york', 0.8029431104660034)]


    print("6----------")
    result = model.similarity("marriage", "happiness")
    print(result)
    # 0.6507987
    

# demo()

#TODO: Các bạn thử viết 2 cách khác nhau để tính cosine similarity
# giữa 2 vector nhé. Kết quả giống với khi dùng model.similarity() là được
# 1 cách là dùng numpy, 1 cách là không dùng numpy nhé
def cosine_similarity(word1, word2):
    vec1 = model[word1]
    vec2 = model[word2]
    # vec1*vec2/||vec1||*||vec2||
    # vec1_x_vec2 = sum([x*y for x,y in zip(vec1, vec2)])
    dot_product = sum(vec1*vec2)
    vec1_norm = sqrt(sum(vec1**2))
    vec2_norm = sqrt(sum(vec2**2))
    return dot_product / (vec1_norm * vec2_norm)
    

print(cosine_similarity("marriage", "happiness"))
# 0.6507986582164231
print(cosine_similarity("man", "woman"))
# 0.7654177233486418


def cosine_similarity_np(word1, word2):
    vec1 = model[word1]
    vec2 = model[word2]
    dot_product = np.dot(vec1, vec2)
    # function to compute the Euclidean norm.
    vec1_norm = np.linalg.norm(vec1)
    vec2_norm = np.linalg.norm(vec2)
    return dot_product / (vec1_norm * vec2_norm)

print(cosine_similarity_np("marriage", "happiness"))
# 0.6507986
print(cosine_similarity_np("man", "woman"))
# 0.7654177


