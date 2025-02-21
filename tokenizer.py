class BPE:
    # Byte Pair Encoding algorithm
    def __init__(self, vocab_size):
        self.vocab_size = vocab_size
        self.merges = {}
        
    def get_pairs(self, data):
        """
        Function that given a list of integers, returns a dictionary with the frequency of pairs of integers.
        """
        
        pairs = {}
        
        for i in range(len(data) - 1):
            pair = (data[i], data[i + 1])
            pairs[pair] = pairs.get(pair, 0) + 1
            
        return pairs
    
    def merge(self, pairs, most_frequent_pair, idx):
        """
        Function that given the list of pairs, the most frequent pair and how we want to rename it (idx),
        returns a new list of pairs with the most frequent pair merged.
        """
        new_pairs = []
        i = 0
            
        while i < len(pairs):
            if i < len(pairs) - 1 and pairs[i] == most_frequent_pair[0][0] and pairs[i + 1] == most_frequent_pair[0][1]:
                new_pairs.append(idx)
                i += 2
            else:
                new_pairs.append(pairs[i])
                i += 1
        
        return new_pairs
            
        
    def train(self, data):
        """
        Train the Byte Pair Encoding model on the given text data.
        
        """
        
        # 1. Convert to utf-8
        data_utf = data.encode("utf-8")
        
        # 2. Convert to integers
        data_int = list(map(int, data_utf)) # From 0 to 255
        
        # 3. Get the frequency of pairs of characters, e.g ((110, 101), 2)
        pairs_list = self.get_pairs(data_int)
        
        # 4. Sort the pairs by frequency
        pairs_sorted = sorted(pairs_list.items(), key=lambda x: x[1], reverse=True)
        
        # 5. Get the most frequent pair
        most_frequent_pair = pairs_sorted[0]
    
        # 6. Iterate trough the pairs and replace the top pair with a new character
        pairs_new = self.merge(data_int, most_frequent_pair, 256)
        
        num_merges = self.vocab_size - 256
        
        self.merges[256] = most_frequent_pair[0]
        
        for i in range(num_merges):
                        
            pairs_list = self.get_pairs(pairs_new)
            
            pairs_sorted = sorted(pairs_list.items(), key=lambda x: x[1], reverse=True)
            
            most_frequent_pair = pairs_sorted[0]
            
            pairs_new = self.merge(pairs_new, most_frequent_pair, 257 + i)
            
            self.merges[257 + i] = most_frequent_pair[0]
            
            # print(f'Merged pair {i + 1}: {most_frequent_pair[0]}, into {257 + i}')

        #Print the stats of the final vocabulary
        print('Initial number of bits:', len(data_int) * 8)
        print('Final number of bits:', len(pairs_new) * 8)
        print('Compression ratio:', len(data_int) / len(pairs_new))
        
    
    def decode_token(self, token):
        """
        Recursively decode a single token into its byte sequence.
        
        If the token is less than 256, it represents a single byte.
        Otherwise, the token is a merged token, so we recursively decode
        its constituent tokens from the merges dictionary.
        """
        if token < 256:
            # Token is a basic byte; convert it directly to a byte string.
            return bytes([token])
        elif token in self.merges:
            # Retrieve the constituent tokens (a tuple of integers).
            left, right = self.merges[token]
            # Recursively decode each constituent token and concatenate.
            return self.decode_token(left) + self.decode_token(right)
        else:
            raise ValueError(f"Token {token} not found in merges dictionary.")

    def decode(self, data):
        """
        Decode a list of tokens into a UTF-8 string.
        
        Each token is recursively decoded into its byte representation.
        The resulting bytes are then decoded using UTF-8 to produce the final string.
        
        Parameters:
        data (list of int): The tokenized data (a list of integers).
        
        Returns:
        str: The decoded UTF-8 string.
        """
        # Decode each token in the list and join the resulting bytes.
        decoded_bytes = b"".join(self.decode_token(token) for token in data)
        # Convert the byte sequence to a string 
        return decoded_bytes.decode("utf-8", errors="replace")
    
    def encode(self, data):
        """
        Encode a UTF-8 string into a list of tokens.
        
        Each byte in the UTF-8 string is encoded as a token.
        If a byte sequence is found in the merges dictionary, it is replaced with a single token.
        
        Parameters:
        data (str): The input UTF-8 string.
        
        Returns:
        list of int: The tokenized data (a list of integers).
        """
        # Encode each byte in the UTF-8 string as a token.
        tokens = list(map(int, data.encode("utf-8")))
        # Replace merged tokens with a single token.
        return [token for token in tokens if token < 256 or token in self.merges]
                
                
                
        

            

        
    
       
        
        
