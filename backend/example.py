"""import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

from similarity import getSymptomList

print(getSymptomList("I have pain in my left arm and my left leg"))
"""

import iris

def main():
    connection_string = "k8s-d7176654-afae8894-57a73db878-d8159e8bf2c102ac.elb.us-east-1.amazonaws.com:1972/USER/"
    username = "SQLAdmin"
    password = "B!pM7XVUjuj11"

    connection = iris.connect(connection_string, username, password)

    irispy = iris.createIRIS(connection)
    print(irispy.getOREF())


    connection.close()


if __name__ == "__main__":
    main()