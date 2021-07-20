
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)  #open file
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())  #reviews  
        labels.append(int(rating))      #label=rating; using 0&1 for the label hence int is used
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt') #1 doc in every line of the text file
rev_test,labels_test=loadData('reviews_test.txt')


#Build a counter based on the training dataset
#counter = TfidfVectorizer( min_df = 0, max_df = 0.8, sublinear_tf = True, use_idf = True, max_features = None, vocabulary = None, binary = True)
#counter.fit(rev_train)
counter = CountVectorizer() #count number of times the unique word occurs, word-its freq
counter.fit(rev_train)  #just take train words


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#clf = MultinomialNB()
#clf = ExtraTreesClassifier()
#clf =MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto')
#clf = GradientBoostingClassifier(n_estimators=1000,learning_rate=1.0,max_depth=1, random_state=0).fit(counts_train, labels_train)
clf = MLPClassifier( hidden_layer_sizes=(15,),max_iter=12, random_state=1,  warm_start=True)
#clf = RandomForestClassifier(n_estimators=2500, n_jobs=15,criterion="entropy",max_features='log2',random_state=150,max_depth=600,min_samples_split=163)
#clf = DecisionTreeClassifier(max_depth=10,min_samples_leaf=4,max_leaf_nodes=5,splitter="best")
#clf = LogisticRegression(random_state=100,solver='liblinear', max_iter=100, multi_class='ovr')
#clf = AdaBoostClassifier(n_estimators=1000)


#train all classifier on the same datasets
clf.fit(counts_train,labels_train)  #build model, doc,its lable

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))
