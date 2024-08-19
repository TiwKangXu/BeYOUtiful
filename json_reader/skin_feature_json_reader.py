import json
from utils.utils import Utils

class SkinFeatureJsonReader:

    def __init__(self, json_file):
        self.json_file = json_file
        self.skin_types = { 0: "oily skin", 1: "dry skin", 2: "normal skin", 3: "mixed skin" }
    
    def sort_dic_by_confidence(self, dic):
        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]['confidence'], reverse=True))
        return sorted_dic
    
    def get_top_confidence_features(self, dic, count=3, confidence_threshold=0.8):
        top_confidence_features = []
        sorted_items = list(self.sort_dic_by_confidence(dic).items())
        for i in range(min(len(sorted_items), count)):
            if sorted_items[i][1]['confidence'] >= confidence_threshold:
                # print(f"Feature {i}: {sorted_items[i][0]} (confidence: {sorted_items[i][1]['confidence']})")
                top_confidence_features.append(sorted_items[i][0])
            else:
                break
        if not top_confidence_features:
            print("All features have insufficient confidence.")
        return top_confidence_features

    def get_pos_features(self, dic):
        pos_features = {key: subitem for key, subitem in dic.items() if subitem['value'] == 1}
        # print("Features with value = 1: ", pos_features)
        return pos_features

    def get_neg_features(self, dic):
        neg_features = {key: subitem for key, subitem in dic.items() if subitem['value'] == 0}
        # print("Features with value = 0: ", neg_features)
        return neg_features

    def extract_result(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        face_analysis = {}

        result = data['result']
        skin_type = self.skin_types[result['skin_type']['skin_type']]
        face_analysis['skin_type'] = skin_type
        result.pop('skin_type')

        pos_features = self.get_pos_features(result)
        top_pos_features = self.get_top_confidence_features(pos_features)
        face_analysis['top_pos_features'] = top_pos_features

        neg_features = self.get_neg_features(result)
        top_neg_features = self.get_top_confidence_features(neg_features)
        face_analysis['top_neg_features'] = top_neg_features
        
        Utils.print_dic(face_analysis)
        return face_analysis

    def run(self):
        self.extract_result()

