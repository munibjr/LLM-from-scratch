import json
from collections import defaultdict

class BPETokenizer:
    def __init__(self, vocab_size=10000):
        self.vocab_size = vocab_size
        self.vocab = {}
        self.merges = {}
        
    def train(self, texts, vocab_size):
        freq = defaultdict(int)
        for text in texts:
            words = text.split()
            for word in words:
                freq[' '.join(word) + ' </w>'] += 1
        
        self.vocab = {token: idx for idx, token in enumerate(freq.keys())}
        
    def encode(self, text):
        tokens = text.split()
        return [self.vocab.get(token, 0) for token in tokens]
    
    def decode(self, tokens):
        return ' '.join([k for k, v in self.vocab.items() if v in tokens])
