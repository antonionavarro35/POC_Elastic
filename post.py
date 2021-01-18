from elasticsearch import Elasticsearch
import json
import sys


if __name__ == "__main__":
    
    try: 
        host= sys.argv[1]
        port= int(sys.argv[2])
        path=sys.argv[3]

    except:
        print("error en linea de comandos")   

    es = Elasticsearch([host], port=port)

    def form_json(i_json):
            try: return json.loads(i_json)['index']['_id']  #i_json es un str hay quetransformarlo en dict
            except: return i_json
    def index_loader(path):
        myFile=open(path,'r', encoding='utf=').read()
        splitFile=myFile.splitlines()
        ids=[form_json(splitFile[i]) for i in range(0,len(splitFile)) if i%2==0]
        data=[form_json(splitFile[i]) for i in range(0,len(splitFile)) if i%2!=0]
        for i in range(0, len(ids)):
            res=es.index(index="books_1", id=ids[i], body=json.loads(data[i]))
            if res['_shards']['failed']!=0:
                print(res)
            else: print(res['_id']+'----> loaded')
    index_loader(path)