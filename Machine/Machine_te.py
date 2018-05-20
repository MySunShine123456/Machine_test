#datatset为数据库svm支持向量机的分类器
from sklearn import svm,datasets
class Dataset:
    #我们创造一个dataset的类，这个类会帮我们下载相关的数据集，
    # 并给我们分类好x,y,x为input,y为output
    def __init__(self,name):
        # 告诉类，我们需要哪一个数据集
        # 我们有两个选择，一个是'iris'一个是'digits'
        self.name=name
    def download_data(self):
        # 从sklearn的自带集中下载我们指定的数据集
        if self.name=='iris':
            # 这里是sklearn自带的数据集下载方法,并用变量存储数据集
            self.download_data=datasets.load_iris()
        elif self.name=='digits':
            self.download_data=datasets.load_digits()
        else:
            print('Dataset Error:No named datasets')
    def generete_xy(self):
        #将原始数据集分成X和y
        #  通过这个过程来把我们的数据集分为原始数据以及他们的label
        # 我们先把数据下载下来
        self.download_data()#获取上面的属性download_data
        x=self.download_data.data#data为x
        y=self.download_data.target#target为Y
        print('\nOriginal data looks like this: \n', x)
        print('\nLabels looks like this: \n', y)
        return x,y#使用return来传参数而不是使用的self来传递参数

    def get_train_test_set(self, ratio):#ratio以多少比例分割测试集和训练集
        # 这里，我们把所有的数据分成训练集和测试集,在训练集上做数据训练，在测试集上做数据测试，测试sklearn模块好不好
        # 一个参数要求我们告知，我们以多少的比例来分割训练和测试集
        # 首先，我们把XY给generate出来：
        x, y = self.generete_xy()

        # 有个比例，我们首先得知道 一共有多少的数据
        n_samples = len(x)
        # 于是我们知道，有多少应该是训练集，多少应该是测试集
        n_train =int(n_samples * ratio)
        print(type(n_train))
        # 好了，接下来我们分割数据e
        # n_train前多少个数据是X_train
        X_train = x[:n_train]
        y_train = y[:n_train]
        # n_train后多少个数据是x_test
        X_test = x[n_train:]
        y_test = y[n_train:]
        # 好，我们得到了所有想要的玩意儿
        return X_train, y_train, X_test, y_test
if __name__=='__main__':
    # 比如，我们使用digits数据集
    data = Dataset('digits')
    # 接着，我们可以用0.7的分割率把xy给分割出来
    X_train, y_train, X_test, y_test = data.get_train_test_set(0.7)