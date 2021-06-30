from elasticsearchquerygenerator.elasticsearchquerygenerator import ElasticSearchQuery
import json

def main():
    # Looking for 100 objects
    helper = ElasticSearchQuery(size=100, BucketName="MyBuckets")
    print(json.dumps(helper.baseQuery, indent=3))

if __name__ == "__main__":
    main()