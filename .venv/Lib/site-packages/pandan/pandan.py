from collections import Counter

class Pandan(object):
    def __init__(self, decision_name, N, min_confidence):
        self.N = N
        self.decision_name = decision_name
        self.min_confidence = min_confidence
        self.evidences = []
        # decision = (belief, certainty)
        self.decision = (None, None)

    def get_decision(self):
        return self.decision

    def add_evidence(self, evidence):
        # do evidence accumulation if there's no decision
        if self.decision[0] == None:
            if len(self.evidences) == self.N:
                counter = Counter(self.evidences)
                #print("AH: ", counter.most_common(1))
                [(evidence, frequency)] = counter.most_common(1)
                certainty = frequency/float(self.N)
                #print("BH: ", certainty, " - ", self.min_confidence, " - ", self.N, " - ", len(self.evidences))
                if certainty < self.min_confidence:
                    self.N = self.N + 3
                    return self.decision
                else:
                    #print("Belief: {} = {}".format(evidence, (frequency/self.N)))
                    self.decision = (evidence, certainty)
                    return self.decision
            else:
                self.evidences.append(evidence)
        #print(self.N)
        return self.decision

p = Pandan("face_recognition", 10, 0.7)
print(p.add_evidence("user01"))
print(p.add_evidence("user02"))
print(p.add_evidence("user01"))
print(p.add_evidence("user03"))
print(p.add_evidence("user01"))
print(p.add_evidence("user02"))
print(p.add_evidence("user01"))
print(p.add_evidence("user03"))
print(p.add_evidence("user01"))
print(p.add_evidence("user02"))
print(p.add_evidence("user01"))
print(p.add_evidence("user03"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
print(p.add_evidence("user01"))
