for i in range(16, 100, 5):
    print("""
if tries>={} and tries<={}:
    print("")
    """.format(i,i+4),end = "")